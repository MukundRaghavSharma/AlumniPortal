from Alumni.forms import SignInForm, SignUpForm, PersonalInformationForm
from Alumni.models import Alumni, PledgeClass
from Alumni.util.get_data import get_first
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.templatetags.static import static
import os
import sys
if sys.version_info >= (3, 0):
    import urllib.request
else:
    import urllib

import uuid

'''
def signin(request):
    if request.method == 'GET':
        return render(request, 'Alumni/signin.html')
'''
# Sign in 1 #
# Function to signin user #
def signin_1(request):
    context = {}
    
    if request.method == 'GET':
        form = SignInForm(request.method)
        context['form'] = form
        return render(request, 'Alumni/signin_1.html', context)

# Sign in 2 #
@transaction.atomic
def signin_2(request):
    context = {}

    # Get Request #
    if request.method == 'GET':
        form = PersonalInformationForm(request.GET)
        context['form'] = form
        return render(request, 'Alumni/signin_2.html', context) 

    # Post Request #
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        context['forms'] = form
        return render(request, 'Alumni/signin_2.html', context)

# Sign in 3 #
# Function to signin user #
def signin_3(request):
    context = {}
    
    if request.method == 'GET':
        form = SignInForm(request.method)
        context['form'] = form
        return render(request, 'Alumni/signin_3.html', context)

# Sign in 4 #
# Function to signin user #
def signin_4(request):
    context = {}
    
    if request.method == 'GET':
        form = SignInForm(request.method)
        context['form'] = form
        return render(request, 'Alumni/signin_4.html', context)



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

            name_url = '404.jpg' 
            url = ('file://' + os.path.dirname(os.path.realpath(__file__)) + 
                '/static/Alumni/images/' + name_url)
            destination_url = 'Alumni/media/images/' + name_url 
            if sys.version_info >= (3, 0):
                raw = urllib.request.urlopen(url)
            else:
                raw = urllib.urlopen(url)
            content_file = ContentFile(raw.read())
            pledge_class = PledgeClass(name = 'Boss Class',
                                       season = 'Spring')
            
            pledge_class.save()
            alumni = Alumni(user = user, pledge_class = pledge_class)
            alumni.picture.save(destination_url, content_file)
            alumni.save()
            authenticated_user = authenticate(username = request.POST['username'],
                                              password = request.POST['password1'])
            login(request, authenticated_user)
            return redirect('/dashboard/')

# Function to displays the home screen #
@login_required
def home(request):
    context = {}
    context['current_user'] = Alumni.objects.get(user = request.user)
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
        employer = str(brother[3])
        current_city = str(brother[4])
        email = str(brother[5])
        phone = str(brother[6])
        major = str(brother[7])
        graduation_class = str(brother[8])
        hometown = str(brother[9])
        class_name = str(brother[10]).split(' ')[0]
        nickname = str(brother[12])
        family = str(brother[11])
        season = str(brother[13]) 
        year = str(brother[14])
        number = str(brother[2])

        print (brother)

        username = str(uuid.uuid4())[0:30]
        user = User(username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email)
        user.save()

        pledge_class = PledgeClass(name = class_name,
                                    season = season,
                                    year = year)

        pledge_class.save()

        try: 
            name_url = first_name.lower() + '.' + last_name.lower() + '.jpg' 

            #url = 'file://Alumni/static/Alumni/images/' + name_url
            url = ('file://' + os.path.dirname(os.path.realpath(__file__)) + 
                '/static/Alumni/images/' + name_url)
            destination_url = 'Alumni/media/images/' + name_url 
            if sys.version_info >= (3, 0):
                raw = urllib.request.urlopen(url)
            else:
                raw = urllib.urlopen(url)
            content_file = ContentFile(raw.read())

        except IOError:
                name_url = '404.jpg' 
                url = ('file://' + os.path.dirname(os.path.realpath(__file__)) + 
                    '/static/Alumni/images/' + name_url)
                destination_url = 'Alumni/media/images/' + name_url 
                if sys.version_info >= (3, 0):
                    raw = urllib.request.urlopen(url)
                else:
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
                            family = family,
                            number = number)
            alumni.picture.save(destination_url, content_file)
            alumni.save()
    return redirect('/dashboard/')

@login_required
def profile(request, id):
    if request.method == 'GET':
        context = {}
        check_user = User.objects.filter(id = id)

        # Id not found! #
        if len(check_user) == 0:
            four_oh_four(request)
        
        user = User.objects.get(id = id)
        context['alumni'] = Alumni.objects.get(user = user)
        context['current_user'] = Alumni.objects.get(user = request.user)
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
        sorting_classes = []

        pledge_classes = PledgeClass.objects.all()
        pledge_classes = pledge_classes.extra(order_by = ['year'])

        for pledge_class in pledge_classes:
            sorting_classes.append(pledge_class)

        # Flip! #
        #for i in range(0, len(sorting_classes) - 1):
        #    # Remove if Boss Class not there #
        #    if i == 0:
        #        continue
        #    
        #    temp = sorting_classes[i]
        #    sorting_classes[i] = sorting_classes[i + 1]
        #    sorting_classes[i + 1] = temp

        # Hacky way of sorting the last names #
        #for pledge_class in sorting_class:
            #for 
            #last_names = pledge

        for pledge_class in sorting_classes:
            filtered_class = Alumni.objects.filter(pledge_class = pledge_class)
            #filtered_class
            sorted_by_number = filtered_class.extra(order_by = ['number'])
            class_based_view.append(filtered_class)

        # for pledge_class in class_based_view
        context['class_based_view'] = class_based_view
        context['current_user'] = Alumni.objects.get(user = request.user)
        return render(request, 'Alumni/gallery.html', context)

@login_required
def search(request):
    pass

@login_required
def four_oh_four(request):
    response = render_to_response('Alumni/404.html', {}, 
                                  context_instance = RequestContext(request))
    response.status_code = 404
    return response 
