from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import SignInForm, SignUpForm

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
           
    if request.method == 'POST':
        errors = []
        context = {}

        # Check for the username in the DB #
        if len(User.objects.filter(username = request.POST['username'])) > 0:
            errors.append('Username already taken!')

        # Check if the passwords match #
        if request.POST['password1'] != request.POST['password2']:
            errors.append('Passwords do not match')    
        if len(errors) > 0:
            return render(request, 'Alumni/signup.html', context)

        # No errors i.e. Create User #
        user = User.objects.create_user(username = request.POST['username'],
                                        email = request.POST['email'],
                                        password = request.POST['password1'],
                                        first_name = request.POST['firstname'],
                                        last_name = request.POST['lastname'])
        user.save()
        authenticated_user = authenticate(username = request.POST['username'],
                                          password = request.POST['password1'])
        login(request, authenticated_user)
        return redirect('/home/')

# Function to displays the home screen #
@login_required
def home(request):
    return render(request, 'Alumni/home.html')

# Function that logs out the user #
@login_required
def logout_user(request):
    logout(request)
    return render(request, 'Alumni/signin.html')
        
'''
# Function to import the CSV file's contents # 
# and get the information to the user #
def get_data():
    pass

# Logging out the user #
def signout(request):
    pass

# Function to parse the CSV file and save the information to the DB #
def __save_information__():
    pass
'''
