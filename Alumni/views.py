from Alumni.forms import (SignInForm, SignUpForm, PersonalInformationForm, AKPsiInformationForm, ProfessionalInformationForm, EditForm)
from Alumni.models import Alumni, PledgeClass
from Alumni.util.class_dictionary import pledge_class_dictionary
from Alumni.util.get_data import get_first
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.templatetags.static import static
import os
import sys

if sys.version_info >= (3, 0):
    import urllib.request
else:
    import urllib

def signin(request):
    if request.method == 'GET':
        context = {}
        form = SignInForm(request.method)
        context['request'] = request
        context['form'] = SignInForm(request.GET)
        return render(request, 'Alumni/signin.html', context)

# Sign in 1 #
# Function to signin user #
def signin_1(request):
    context = {}
    
    if request.method == 'GET':
        context['request'] = request
        return render(request, 'Alumni/signin_1.html', context)

# Sign in 2 #
@transaction.atomic
@login_required
def signin_2(request):
    context = {}

    # Get Request #
    if request.method == 'GET':
        user = request.user
        user = User.objects.get(username = request.user)
        alumni = Alumni.objects.get(user = user)
        initial = {'first_name' : user.first_name,
                   'last_name' : user.last_name,
                   'email' : user.email} 
        form = PersonalInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_2.html', context) 

    # Post Request #
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password2 = form.cleaned_data['password2']

        if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                    return HttpResponseRedirect('/signin_3')
        else :
            context['forms'] = form
            return render(request, 'Alumni/signin_2.html', context)

# Sign in 3 #
# Function to signin user #
@login_required
def signin_3(request):
    context = {}
    
    if request.method == 'GET':
        user = request.user
        alumni = Alumni.objects.get(user = user)
        pledge_class = alumni.pledge_class
        initial = {'major' : alumni.major,
                   'hometown' : alumni.hometown,
                   'email' : user.email,
                   'phone' : alumni.phone } 
        form = AKPsiInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_3.html', context)

    if request.method == 'POST':
        pass

# Sign in 4 #
# Function to signin user #
def signin_4(request):
    context = {}
    
    if request.method == 'GET':
        user = request.user
        alumni = Alumni.objects.get(user = user)
        initial = {'current_employer' : alumni.employer,
                   'role' : alumni.position,
                   'city' : alumni.current_city}
        form = ProfessionalInformationForm(initial = initial)
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
                                       season = 'Spring',
                                       class_number = 14444)
            
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

        username = first_name + last_name + email
        username = username[0:30]
        user = User(username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email)
        user.save()

        class_number = 14444 # Default bullshit 
        if class_name in pledge_class_dictionary:
            class_number = pledge_class_dictionary[class_name] 

        if class_name not in pledge_class_dictionary:
            print (first_name)
            print (last_name)
            print (number)

        pledge_class = PledgeClass(name = class_name,
                                   season = season,
                                   year = year,
                                   class_number = class_number)

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
        print (id)
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
        pledge_classes = pledge_classes.extra(order_by = ['class_number'])

        # Edge case: Charters #
        charters = PledgeClass.objects.filter(name = 'Charter').order_by('number')
        sorting_classes.append(charters)

        for pledge_class in pledge_classes:
            sorting_classes.append(pledge_class)

        for pledge_class in sorting_classes:
            filtered_class = Alumni.objects.filter(pledge_class = pledge_class)
            sorted_by_number = filtered_class.extra(order_by = ['number'])
            class_based_view.append(filtered_class)

        context['class_based_view'] = class_based_view
        context['current_user'] = Alumni.objects.get(user = request.user)
        return render(request, 'Alumni/gallery.html', context)

@login_required
def search(request):
    if request.method == 'POST':
        pass


@login_required
def edit_profile(request, id):
    context = {}
    alumni = Alumni.objects.get(user = request.user)

    if request.method == 'GET':
        initial = {'first_name' : request.user.first_name,
                   'last_name' : request.user.last_name,
                   'email' : request.user.email,
                   'phone' : alumni.phone,
                   'hometown' : alumni.hometown,
                   'major' : alumni.major,
                   'current_employer' : alumni.employer,
                   'role' : alumni.position,
                   'current_city' : alumni.current_city,
                   'password1' : request.user.password,
                   'password2' : request.user.password,
        } 

        context['form'] = EditForm(initial = initial) 
        return render(request, 'Alumni/edit.html', context)

    if request.method == 'POST':
        alumni_data = request.POST

        # User Info Change #
        if (alumni_data['password1'] != alumni_data['password2'] and alumni_data['password1'] != '' and
            alumni_data['password2'] != ''):
            raise ValidationError("PASSWORDS SHOULD MATCH!")
        else:
            alumni.user.set_password(alumni_data['password1'])

        # Alumni Info Change #
        alumni.phone = alumni_data['phone']
        alumni.hometown = alumni_data['hometown']
        alumni.major = alumni_data['major']
        alumni.employer = alumni_data['current_employer']
        alumni.position = alumni_data['role']
        alumni.current_city = alumni_data['current_city']

        alumni.save()
        return redirect('/edit/' + id)


@login_required
def four_oh_four(request):
    response = render_to_response('Alumni/404.html', {}, 
                                  context_instance = RequestContext(request))
    response.status_code = 404
    return response 

def social_auth_to_profile(backend, details, response, is_new=False, *args, **kwargs):

    # Stuff to parse from LinkedIn:
    # 1. Employer
    # 2. Summary 
    # 3. Position
    # 4. LinkedIn Public Page URL
    # 5. Picture URL

    # Check for each field.. some could be None #
    first_name = details['first_name']
    last_name = details['last_name']
    email = details['email']

    # If user is not in the DB #
    # - Create the user object 
    # - Create the Alumni object 
    
    # If user is in the DB #
    # - Get the user object  
    # - Get the alumni object

    username = first_name + last_name + email
    username = username[0:30]
    is_new = len(User.objects.filter(first_name = first_name, 
             last_name = last_name,
             email = email, 
             username = username)) == 0
    user = None
        
    if is_new:
        # Create new profile here #
            user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email)
            alumni = Alumni(user = user)
            user.save()
            alumni.save()

    else:
        # Not new -> link to already created profile #
        user = User.objects.get(username = username, first_name = first_name, last_name = last_name, email = email)

    alumni = Alumni.objects.get(user = user)
    if kwargs.get('social') != None:
        print (kwargs)
        print (kwargs.get('social').extra_data)
        linkedin_info = kwargs['social'].extra_data
        alumni.role = linkedin_info['headline']
        alumni.current_city = linkedin_info['location']
        #alumni.position_description = linkedin_info['summary'] 
        #alumni = social_user.extra_data['positions']['position'][0]['title']
        alumni.save()
