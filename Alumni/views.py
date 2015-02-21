from django.contrib.auth import login, authenticate, logout
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import SignInForm, SignUpForm
from models import Alumni
from util.get_data import get_first

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
            alumni.save()
            authenticated_user = authenticate(username = request.POST['username'],
                                              password = request.POST['password1'])
            login(request, authenticated_user)
            return redirect('/home/')

# Function to displays the home screen #
@login_required
def home(request):
    context = {}
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
    count = 0
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
        pledge_class = str(brother[9])
        
        user = User(username = count,
                    first_name = first_name,
                    last_name = last_name,
                    email = email)
        user.save()
        alumni = Alumni(user = user,
                        employer = employer,
                        current_city = current_city,
                        phone = phone,
                        major = major,
                        graduation_class = graduation_class,
                        hometown = hometown,
                        pledge_class = pledge_class)
        alumni.save()
    return redirect('/home/')

@login_required
def profile(request, id):
    if request.method == 'GET':
        context = {}
        check_user = User.objects.filter(id = id)

        # Id not found! #
        if len(check_user) == 0:
            return HttpResponse('<h1>No Page Here</h1>') 
        
        user = User.objects.get(id = id)
        context['alumni'] = Alumni.objects.get(user = user)
        context['file_name'] = str(user.first_name.lower() + '.' + user.last_name.lower() + '.jpg')
        return render(request, 'Alumni/profile.html', context)

@login_required
def class_view(request, classname):
    context = {}
    classname = classname[0].upper() + classname[1:]
    query = classname + ' Class'
    class_filter = Alumni.objects.filter(pledge_class = classname)
    return render(request, 'Alumni/classview.html', context)

@login_required
def family_view(request, family):
    pass

'''
@login_required
def search(request):
    context = {}
    context['alumni'] = []
    if request.method == 'GET':
        return render(request, 'Alumni/search.html')

    
    if request.method == 'POST':
        
        if request.POST['search_name'] != '':
            filtered_alumni = Alumni.objects.filter(Q(first_name__icontains = request.POST['search_name']) | Q(last_name__icontains = request.POST['search_name'])) 
            context['alumni'] += filtered_alumni
        
        if request.POST['search_company'] != '':
            filtered_alumni = Alumni.objects.filter(Q(employer__icontains = request.POST['search_company']))
            context['alumni'] += filtered_alumni
        return render(request, 'Alumni/search.html', context)
'''
