from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import SignInForm, SignUpForm
from models import Alumni
from util.get_data import get_first

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

@login_required
def save_10(request):
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

@login_required
def profile(request, username):
    


    return render(request, 'Alumni/home.html')

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
        ''' 
        if request.POST['search_pledge_class'] != '':
            filtered_alumni = Alumni.objects.filter(Q(pledge_class__icontains = request.POST['search_pledge_class']))
            context['alumni'] += filtered_alumni
        ''' 
        return render(request, 'Alumni/search.html', context)
