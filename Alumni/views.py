from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.templatetags.static import static
from forms import SignInForm, SignUpForm
from models import Alumni
from util.get_data import get_first
import urllib
import uuid

def signin_1(request):
    if request.method == 'GET':
        return render(request, 'Alumni/signin_1.html')

# Function to signin user #
def signin(request):
    context = {}
    form = SignInForm(request.method)
    context['form'] = form
    return render(request, 'Alumni/signin.html', context)

# Function to signup user #
@transaction.atomic
def signup(request):
    
    # GET Request #
    if request.method == 'GET':
        form = SignUpForm(request.GET)
        return render(request, 'Alumni/signup.html', {'form' : form})
           
    # POST Request #
    if request.method == 'POST':
        errors = []
        context = {}
        form = SignUpForm(request.POST)

        # Check for the username in the DB #
        if len(User.objects.filter(username = request.POST['username'])) > 0:
            errors.append('Username already taken!')

        # Check if the passwords match #
        if request.POST['password1'] != request.POST['password2']:
            errors.append('Passwords do not match')    
        if len(errors) > 0:
            return render(request, 'Alumni/signup.html', context)

        if form.is_valid():
            # No errors i.e. Create User #
            user = User.objects.create_user(password = request.POST['password1'],
                                            username = request.POST['username'],
                                            first_name = request.POST['first_name'],
                                            last_name = request.POST['last_name'])
            user.save()
            alumni = Alumni(user = user,)

            #pledge_class = PledgeClass(


            alumni.save()
            authenticated_user = authenticate(username = request.POST['username'],
                                              password = request.POST['password1'])
            login(request, authenticated_user)
            return redirect('/home/')

# Function to displays the home screen #
@login_required
def home(request):
    context = {}
    context['file_name'] = str(request.user.first_name.lower() + '.' + request.user.last_name.lower() + '.jpg')
    context['user'] = request.user
    context['alumni'] = Alumni.objects.all() 
    return render(request, 'Alumni/home.html', context)

# Function that logs out the user #
@login_required
def logout_user(request):
    logout(request)
    form = SignUpForm(request.GET)
    return render(request, 'Alumni/signin.html', {'form' : form})

@login_required
@transaction.atomic
def update(request):
    brothers = get_first()
    for brother in brothers:
        first_name = str(brother[0])
        last_name = str(brother[1])
        employer = str(brother[2])
        current_city = str(brother[3])
        email = str(brother[4])
        phone = str(brother[5])
        major = str(brother[6])
        graduation_class = str(brother[7])
        hometown = str(brother[8])
        pledge_class = str(brother[9]).split(' ')[0]
        nickname = str(brother[11])
        family = str(brother[10])

        username = str(uuid.uuid4())[0:30]
        user = User(username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email)
        user.save()

        # Load the picture in the static folder by default #
        try:
            name_url = first_name.lower() + '.' + last_name.lower() + '.jpg' 
            url = 'Alumni/static/Alumni/images/' + name_url
            destination_url = 'Alumni/media/images/' + name_url 
            raw = urllib.urlopen(url)
            content_file = ContentFile(raw.read())

        except IOError:
            name_url = '404.jpg' 
            url = 'Alumni/static/Alumni/images/' + name_url
            destination_url = 'Alumni/media/images/' + name_url 
            raw = urllib.urlopen(url)
            content_file = ContentFile(raw.read())

        finally: 
            alumni = Alumni(user = user,
                            employer = employer,
                            current_city = current_city,
                            phone = phone,
                            major = major,
                            graduation_class = graduation_class,
                            hometown = hometown,
                            pledge_class = pledge_class,
                            nickname = nickname,
                            family = family)
            alumni.picture.save(destination_url, content_file)
            alumni.save()
    return redirect('/home/')

@login_required
def profile(request, id):
    if request.method == 'GET':
        context = {}
        check_user = User.objects.filter(id = id)

        # Id not found! #
        if len(check_user) == 0:
            four_oh_four(request)
        
        user = User.objects.get(id = id)
        current_user = User.objects.get(username = request.user.username)

        context['alumni'] = Alumni.objects.get(user = user)
        context['user'] = Alumni.objects.get(user = current_user)
        context['file_name'] = (str(user.first_name.lower() + '.' + 
                                user.last_name.lower() + '.jpg'))
        return render(request, 'Alumni/profile.html', context)

# Function to get the class view #
@login_required
def class_view(request, classname):
    context = {}

    if request.method == 'GET':
        # Creating the classname string to filter the pledge class #
        classname = classname.lower()
        classname = classname[0].upper() + classname[1:] 
        class_filter = Alumni.objects.filter(pledge_class = classname)
        
        if len(class_filter) < 1:
            four_oh_four(request)

        context['alumni'] = class_filter
        return render(request, 'Alumni/class.html', context)

@login_required
def family_view(request, family):
    pass

@login_required
def gallery_view(request):
    context = {}

    if request.method == 'GET':
        class_based_view = []
        distinct_classes = []

        pledge_classes = Alumni.objects.values_list('pledge_class').distinct()
        for pledge_class in pledge_classes:
            distinct_classes.append(pledge_class[0])
        
        for pledge_class in distinct_classes:
            class_based_view.append(Alumni.objects.filter(pledge_class = pledge_class))
         
        context['class_based_view'] = class_based_view
        return render(request, 'Alumni/gallery.html', context)

@login_required
def four_oh_four(request):
    return render(request, 'Alumni/404.html')
