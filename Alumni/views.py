from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import SignInForm, SignUpForm
from util.get_data import get_first
from models import Alumni

# Function to signin user #
def signin(request):
    context = {}
    form = SignInForm(request.GET)
    if request.method == 'GET':
        return render(request, 'Alumni/signin.html', {'form' : form})

    if request.method == 'POST':
        if form.is_valid():
            authenticated_user = authenticate(username = request.POST['username'],
                                              password = request.POST['password'])
            login(request, authenticated_user)
            return redirect('/home/')

# Function to signup user #
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
            user = User.objects.create_user(username = request.POST['username'],
                                            email = request.POST['email'],
                                            password = request.POST['password1'],
                                            first_name = request.POST['first_name'],
                                            last_name = request.POST['last_name'])
            user.save()
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

def save_10(request):
    brothers = get_first()
    first_name = ''
    last_name = ''
    employer = ''
    current_city = ''
    email = ''
    phone = ''
    major = ''
    graduation_class = ''
    hometown = ''
    pledge_class = ''

    for brother in brothers:
        first_name = str(brother[0])
        last_name = str(brother[1])
        employer = str(brother[2])
        current_city = str(brother[3])
        email = str(brother[4])
        phone = str(brother[5])
        graduation_class = str(brother[6])
        hometown = str(brother[7])
        pledge_class = str(brother[8])
        
        alumni = Alumni(first_name = first_name,
                last_name  = last_name,
                employer = employer,
                current_city = current_city,
                email = email,
                phone = phone,
                major = major,
                graduation_class = graduation_class,
                hometown = hometown,
                pledge_class = pledge_class)
        alumni.save()
    return redirect('/home/')

def profile(request):
    return render(request, 'Alumni/home.html')
