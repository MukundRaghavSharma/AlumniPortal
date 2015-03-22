from Alumni.forms import (SignInForm, SignUpForm, PersonalInformationForm, AKPsiInformationForm, ProfessionalInformationForm)
from Alumni.models import Alumni, PledgeClass
from Alumni.util.get_data import get_first
from Alumni.util.class_dictionary import pledge_class_dictionary
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.templatetags.static import static
import os
import sys
import uuid
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
    
    # Post redirects to signin_2 #
    if request.method == 'POST':
        confirmation_code = request.POST['confirmation'] 

        if len(Alumni.objects.filter(confirmation_code = confirmation_code)) < 1:
               context['is_error'] = True
               return render(request, 'Alumni/signin_1.html', context)
        else: 
            alumni = Alumni.objects.get(confirmation_code = confirmation_code)
            alumni.user.backend  = 'django.contrib.auth.backends.ModelBackend'
            alumni.save()
            login(request, alumni.user)
            return redirect('/signin_2')
            context['username'] = alumni.user.username
            return render(request, 'Alumni/signin_2.html')

# Sign in 2 #
@login_required
@transaction.atomic
def signin_2(request):
    context = {}

    # Get Request #
    if request.method == 'GET':
        user = User.objects.get(username = request.user.username)
        alumni = Alumni.objects.get(user = user)
        initial = {'first_name' : user.first_name,
                   'last_name' : user.last_name,
                   'email' : user.email,
                   'phone' : alumni.phone} 
        form = PersonalInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_2.html', context) 

    # Post Request #
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, request.FILES)
        alumni = Alumni.objects.get(user = request.user)

        if form.is_valid():
            alumni = Alumni.objects.get(user = request.user)
            user = alumni.user
            alumni.user.first_name = form.cleaned_data.get('first_name')
            alumni.user.last_name = form.cleaned_data.get('last_name')
            alumni.user.email = form.cleaned_data.get('email')
            alumni.user.set_password(form.cleaned_data.get('password2'))
            alumni.user.backend  = 'django.contrib.auth.backends.ModelBackend'
            alumni.user.save()
            alumni = Alumni.objects.filter(user = request.user) 
            alumni.update(phone = form.cleaned_data.get('phone'))
            login(request, user)
            return redirect('/signin_3')

        context['form'] = form
        return render(request, 'Alumni/signin_2.html', context)

# Sign in 3 #
# Function to signin user #
@login_required
@transaction.atomic
def signin_3(request):
    context = {}
    
    if request.method == 'GET':
        alumni = Alumni.objects.get(user = request.user)
        pledge_class = alumni.pledge_class
        initial = {'major' : alumni.major,
                   'graduation_year' : alumni.graduation_class,
                   'hometown' : alumni.hometown,
                   'pledge_class' : alumni.pledge_class } 
        form = AKPsiInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_3.html', context)

    if request.method == 'POST':
        form = AKPsiInformationForm(request.POST)
        user = request.user
        alumni = Alumni.objects.get(user = user)
        if form.is_valid():
            alumni.major = form.cleaned_data['major']
            alumni.graduation_class = form.cleaned_data['graduation_year']
            print (form.cleaned_data['graduation_year'])
            alumni.hometown = form.cleaned_data['hometown']
            alumni.save()
            return redirect('/signin_4')

        # Invalid form #
        context['form'] = form
        return render(request, 'Alumni/signin_3.html', context)  

# Sign in 4 #
# Function to signin user #
@transaction.atomic
def signin_4(request):
    context = {}
    user = request.user
    alumni = Alumni.objects.get(user = request.user)
    
    if request.method == 'GET':
        print ("Alumni Employer ", alumni.employer)
        print ("Alumni role", alumni.position)
        print ("Alumni city", alumni.current_city)
        initial = {'current_employer' : alumni.employer,
                   'role' : alumni.position,
                   'current_city' : alumni.current_city}
        form = ProfessionalInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_4.html', context)

    if request.method == 'POST':
        print ("IN POST FOR PROFESSIONAL INFO")
        form = ProfessionalInformationForm(request.POST)
        alumni = Alumni.objects.get(user = request.user)
        print ("Alumni Employer ", alumni.employer)
        print ("Alumni role", alumni.position)
        print ("Alumni city", alumni.current_city)
        alumni = Alumni.objects.get(user = request.user)
        if form.is_valid():
            print ("PROFESSIONAL FORM VALID")
            alumni.employer = form.cleaned_data.get('current_employer')
            alumni.role = form.cleaned_data.get('role')
            alumni.current_city = form.cleaned_data.get('current_city')
            alumni.save()
            return redirect('/dashboard/')

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
    return redirect('/')

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
        big = str(brother[15])

        password = str(uuid.uuid4()) 
        username = first_name + last_name + email
        username = username[0:30]
        user = User.objects.create_user(username = username,
                                        first_name = first_name,
                                        last_name = last_name,
                                        email = email,
                                        password = password)
        user.is_active = False 
        user.save()

        class_number = 14444 # Default bullshit 
        if class_name in pledge_class_dictionary:
            class_number = pledge_class_dictionary[class_name] 

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
                            confirmation_code = password,
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
def family_trees(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'Alumni/family_trees.html', context)

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
def edit_profile(request):
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

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

@login_required
def donations(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'Alumni/donations.html', context)

