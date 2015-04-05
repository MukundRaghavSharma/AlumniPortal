from Alumni.forms import (SignInForm, SignUpForm, PersonalInformationForm, 
AKPsiInformationForm, ProfessionalInformationForm, CHOICES)
from Alumni.models import Alumni, PledgeClass, Family
from Alumni.util.class_dictionary import pledge_class_dictionary
from django.templatetags.static import static
from Alumni.util.get_data import get_first
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.core.mail import send_mail
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.templatetags.static import static
from itertools import chain
# from django.http import Http404
# from django.http import HttpResponse
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
        form = SignInForm(request.GET)
        context['request'] = request
        context['form'] = form
        return render(request, 'Alumni/signin.html', context)

# Sign in 1 #
# Function to signin user #
def signin_1(request):
    context = {}
    
    if request.method == 'GET':
        form = SignInForm()
        context['form'] = form
        context['request'] = request
        return render(request, 'Alumni/signin_1.html', context)
    
    # Post redirects to signin_2 #
    if request.method == 'POST':
        print(request.POST)
        form = SignInForm()
        context['form'] = form

        if 'confirmation' in request.POST:
            
            confirmation_code = request.POST['confirmation'] 
            print(len(Alumni.objects.filter(confirmation_code = confirmation_code)) < 1 and len(confirmation_code) == 0)
            if len(Alumni.objects.filter(confirmation_code = confirmation_code)) < 1 or len(confirmation_code) == 0:
                   context['reg_error'] = "Your registration code is invalid. Contact the VPA for assistance."
                   return render(request, 'Alumni/signin_1.html', context)
            else: 
                alumni = Alumni.objects.get(confirmation_code = confirmation_code)
                alumni.user.backend  = 'django.contrib.auth.backends.ModelBackend'
                alumni.save()
                login(request, alumni.user)
                return redirect('/signin_2')

        if 'email' in request.POST and 'password1' in request.POST:
            email = request.POST['email']
            password = request.POST['password1']
            form = SignInForm(request.POST)

            if form.is_valid():
                if len(User.objects.filter(email = email)) < 1:
                    context['error'] = "Your email and password don't match!"
                    context['form'] = form
                    return render(request, 'Alumni/signin_1.html',context)
                else:
                    user = User.objects.all().get(email=email);
                    u = authenticate(username=user.username, password=password)
                    if u is not None:
                        login(request, u)
                        return redirect("/dashboard/")

                # return redirect('/signin_2')
            context['form'] = form
        return render(request, 'Alumni/signin_1.html',context)

# Sign in 2 #
@login_required
@transaction.atomic
def signin_2(request):
    context = {}

    if request.method == 'GET':
        user = User.objects.get(username = request.user.username)
        alumni = Alumni.objects.get(user = user)
        print (alumni.facebook_url)
        initial = {'first_name' : user.first_name,
                   'last_name' : user.last_name,
                   'email' : user.email,
                   'facebook' : alumni.facebook_url,
                   'phone' : alumni.phone} 
        form = PersonalInformationForm(initial = initial)
        context['form'] = form
        context['alumni'] = alumni 
        return render(request, 'Alumni/signin_2.html', context) 

    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, request.FILES)
        alumni = Alumni.objects.get(user = request.user)

        if form.is_valid():
            alumni = Alumni.objects.get(user = request.user)
            user = alumni.user
            alumni.user.first_name = form.cleaned_data.get('first_name')
            alumni.user.last_name = form.cleaned_data.get('last_name')
            alumni.facebook_url = form.cleaned_data.get('facebook')
            alumni.user.email = form.cleaned_data.get('email')
            alumni.user.set_password(form.cleaned_data.get('password2'))
            alumni.user.backend  = 'django.contrib.auth.backends.ModelBackend'
            alumni.user.save()
            alumni.save()
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
        if len(alumni.graduation_class) < 2:
            alumni.graduation_class = ''
        else:
            alumni.graduation_class = alumni.graduation_class.split(' ')[2]
        for choice in CHOICES:
            if choice == alumni.graduation_class:
                class_choice = choice 

        pledge_class = alumni.pledge_class
        if alumni.graduation_class == '':
            class_choice = CHOICES[[0]][1]
        else:
            class_choice = CHOICES[2][1]

        class_choice = 0 
        for choice in CHOICES:
            if str(choice[1]) == str(alumni.graduation_class):
                class_choice = choice[0] 
                
        initial = {'major' : alumni.major,
                   'graduation_year' : class_choice,
                   'hometown' : alumni.hometown,
                   'pledge_class' : alumni.pledge_class } 
        form = AKPsiInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_3.html', context)

    if request.method == 'POST':
        form = AKPsiInformationForm(request.POST)
        user = request.user
        alumni = Alumni.objects.get(user = user)
        class_choice = str(CHOICES[int(request.POST['graduation_year'])][1])
        if form.is_valid():
            alumni.major = form.cleaned_data['major']
            alumni.graduation_class = "Class of " + class_choice 
            alumni.pledge_class = form.cleaned_data['pledge_class']
            alumni.hometown = form.cleaned_data['hometown']
            alumni.save()
            return redirect('/signin_4')

        # Invalid form #
        context['form'] = form
        return render(request, 'Alumni/signin_3.html', context)  

# Sign in 4 #
# Function to signin user #
@login_required
@transaction.atomic
def signin_4(request):
    context = {}
    user = request.user
    alumni = Alumni.objects.get(user = request.user)
    
    if request.method == 'GET':
        initial = {'current_employer' : alumni.employer,
                   'role' : alumni.position,
                   'current_city' : alumni.current_city,
                   'linkedin_link': alumni.linkedin_url }
        form = ProfessionalInformationForm(initial = initial)
        context['form'] = form
        return render(request, 'Alumni/signin_4.html', context)

    if request.method == 'POST':

        form = ProfessionalInformationForm(request.POST)
        user = request.user
        alumni = Alumni.objects.get(user = request.user)
        if form.is_valid():
            alumni.employer = form.cleaned_data.get('current_employer')
            alumni.position = form.cleaned_data.get('role')
            alumni.current_city = form.cleaned_data.get('current_city')
            alumni.linkedin_url = form.cleaned_data.get('linkedin_link')
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
            family = Family(name = "Boss")
            family.save()
            pledge_class.save()
            alumni = Alumni(user = user, 
                            pledge_class = pledge_class, 
                            family = family, 
                            graduation_class = 'Class of 666',
                            number = 14444)
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
def send_email(request):
    easy_mode = True
    if easy_mode == False:
        brothers = get_first()
        for brother in brothers:
            first_name = str(brother[0])
            last_name = str(brother[1]) 
            user = User.objects.get(first_name = first_name, last_name = last_name)
            alumni = Alumni.objects.get(user = user)
            email = str(brother[5])
            email_body = '''
    Dear %s %s,

    The following is your confirmation code: %s!

    Have a good day..

    Sincerely,
    Mog San
    ''' % (alumni.user.first_name, alumni.user.last_name, alumni.confirmation_code)
        send_mail(subject="AKPsi Alumni Code",
          message= email_body,
          from_email="mrsharma@andrew.cmu.edu",
          recipient_list=[alumni.user.email])

    else:
        alumni = Alumni.objects.all()[2]
        email_body = '''
    Dear %s %s,

    The following is your confirmation code: %s!

    Have a good day..

    Sincerely,
    Mog San
    ''' % (alumni.user.first_name, alumni.user.last_name, alumni.confirmation_code)
        send_mail(subject="AKPsi Alumni Code",
          message= email_body,
          from_email="mrsharma@andrew.cmu.edu",
          recipient_list=["mrsharma@andrew.cmu.edu"])

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
        is_alumni = str(brother[16])
        is_active = str(brother[17])

        if is_alumni == 'TRUE':
            is_alumni = True
        else:
            is_alumni = False

        if is_active == 'TRUE':
            is_active = True
        else:
            is_active = False

        if len(big) != 0:
            big_first_name = big.split(' ')
            big_last_name = big.split(' ')
            if len(big_first_name) > 2:
                big_first_name = big_first_name[0]
                big_last_name = big_last_name[2]
            else:
                big_first_name = big_first_name[0]
                big_last_name = big_last_name[1]

        password = str(uuid.uuid4()) 
        username = first_name + last_name + email
        username = username[0:30]
        user = User.objects.create_user(username = username,
                                        first_name = first_name,
                                        last_name = last_name,
                                        email = email,
                                        password = password)
        user.save()
        if len(big) != 0:
            big_user = User.objects.get(first_name = big_first_name,
                                        last_name = big_last_name)
        else:
            big_user = None
        user.is_active = False 

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
            url = ('file://' + os.path.dirname(os.path.realpath(__file__)) + '/static/Alumni/images/' + name_url)
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
            if big_user == None:
                big_alumni = None
            else:
                big_alumni = Alumni.objects.get(user = big_user)

            family_model = Family(name = family)
            family_model.save()
            alumni = Alumni(user = user,
                            employer = employer,
                            current_city = current_city,
                            phone = phone,
                            major = major,
                            graduation_class = graduation_class,
                            hometown = hometown,
                            pledge_class = pledge_class,
                            nickname = nickname,
                            family = family_model,
                            confirmation_code = password,
                            big = big_alumni,
                            is_active = is_active,
                            is_alumni = is_alumni,
                            number = number)
            alumni.picture.save(destination_url, content_file)
            alumni.save()
    return redirect('/dashboard/')

@login_required
def profile(request, brother_number):
    context = {}

    if request.method == 'GET':
        context['alumni'] = get_object_or_404(Alumni, number = brother_number)
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
        user = User.objects.get(username = request.user)
        alumni = Alumni.objects.get(user = user)
        context['current_user'] = alumni 
        return render(request, 'Alumni/family_trees.html', context)

def __create_family_trees__():
    # Parse File #
    file_names = ('kaleidoscope.txt', 'dynasty.txt', 'family.txt', 
            'reaganbrothers.txt', 'rocafellas.txt', 'incredibles.txt')
    for file_name in file_names:
        name = file_name.split('.')[0]
        name += '.js'
        read_file = open('./static/Families/' + file_name, 'r')
        write_file = open('./static/Alumni/js/' + name, 'w')
        js_starter = ''' <script type="text/javascript">
          google.load("visualization", "1", {packages:["orgchart"]});
          google.setOnLoadCallback(drawChart);
          function drawChart() {
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name');
            data.addColumn('string', 'Manager');
            data.addColumn('string', 'ToolTip');
            data.addRows('''

        #if big == '' or len(User.objects.filter(first_name = big_first_name, 
        #last_name = big_last_name):  
        for line in f:
            line.decode('utf-8', 'replace')
            # Big Info #
            big = line.split(',')[1].split('[')[0]
            big = big.replace("\xe2\x80\x99","").replace("'", "")
            big = big.replace("\xe2\x80\x98","")
            big_first_name = big.split(' ')[0]
            big_last_name = big.split(' ')[1]
            big_img = ''
            
            # Little Info #
            little = line.split(',')[0].split('[')[1]
            little = little.replace("\xe2\x80\x99","").replace("'","")
            little = little.replace("\xe2\x80\x98", "")

            # Search for the big #
            if big != '' or len(User.objects.filter(first_name = big_first_name, 
                last_name = big_last_name)) > 0:
                user = User.objects.get(first_name = big_first_name, last_name = big_last_name)
                alumni = Alumni.objects.get(user = user)

            else:
                pass
            
        read_file.close()
        write_file.close()

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
            filtered_class = Alumni.objects.filter(pledge_class = pledge_class, is_alumni = True, is_active = True)
            sorted_by_number = filtered_class.extra(order_by = ['number'])
            if len(sorted_by_number) > 0:
                class_based_view.append(sorted_by_number)

        # Year based view #
        year_based_view = []
        sorted_graduation_classes = []
        graduation_classes = Alumni.objects.values('graduation_class').distinct()
        graduation_classes = [item for item in graduation_classes]

        # Sort the graduation class #
        for grad_class in graduation_classes:
            sorted_graduation_classes.append(grad_class['graduation_class'])
        
        sorted_graduation_classes.sort()
        for graduation_class in sorted_graduation_classes:
            batch = Alumni.objects.filter(graduation_class = graduation_class, is_alumni = True, is_active = True)
            year_based_view.append(batch)

        context['year_based_view'] = year_based_view
        context['class_based_view'] = class_based_view
        context['current_user'] = Alumni.objects.get(user = request.user)
        return render(request, 'Alumni/gallery.html', context)

@login_required
def family_trees_create(request):
    INITIAL_SCRIPT = '''
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([\n\t'''
    
    families = Family.objects.all()
    for family in families:
        cwd = os.getcwd()
        file_name = family.name
        div_name = family.name.lower()

        div_name = div_name.replace(' ', '_')
        div_name = div_name.replace('-', '_')

        if family.name == 'Reagan Brothers':
            file_name = 'Reagan_Brothers' 
        file_name = family.name.replace('-', '_')
        file_name = family.name.replace(' ', '_')
        if family.name == 'Roc-a-Fellas':
            file_name = 'Roc_a_Fellas' 

        FINAL_SCRIPT = '''
        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('''+"\'"+ div_name+'''_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        '''

        family_file = open(cwd + '/Alumni/static/Alumni/js/Families/' + family.name.lower() + '.js', 'w')
        FUNCTION_HEADER = 'function ' + file_name + '() {'
        family_file.write(FUNCTION_HEADER + INITIAL_SCRIPT)
        for alumni in Alumni.objects.filter(family = family):
            big = alumni.big
            little_name = "'" + alumni.user.first_name + ' ' + alumni.user.last_name + "'"
            big_text = '' + '\'\',\'\'],'
            if big != None:
                big_name = "'" + big.user.first_name + ' ' + big.user.last_name
                #big_text = '<a href="/profile/' + big.number + '" class="pull-left" width=20> ' + big_name + "'', '']," 
                big_text = big_name + '\',' + '\'\'],' 
            #little_text = "['<a href=\"/profile/" + alumni.number + '" class=pull-left width=20> ' + alumni.user.first_name + ' ' + alumni.user.last_name + "','" 
            little_text = "[" + little_name + ","
            final_text = little_text + big_text + '\n'
            family_file.write(final_text)
        family_file.write(FINAL_SCRIPT)
        family_file.close()
    return redirect('/dashboard/')

@login_required
def four_oh_four(request):
    return render(request, 'Alumni/404.html', status=404)

@login_required
def donations(request):
    context = {}

    if request.method == 'GET':
        user = User.objects.get(username = request.user)
        alumni = Alumni.objects.get(user = user)
        context['current_user'] = alumni 
        return render(request, 'Alumni/donations.html', context)

@login_required
def search(request):
    context = {}

    if request.method == 'POST':
        search = str(request.POST['search'])

        # Fix the user case #
        # Add hyperlinks #
        user_results = User.objects.filter(Q(first_name__icontains=search) |
                                           Q(last_name__icontains=search) | 
                                           Q(email__icontains=search)).values_list() 

        alumni_results = Alumni.objects.filter(Q(employer__icontains=search) |
                                               Q(position__icontains=search) | 
                                               Q(current_city__icontains=search) | 
                                               Q(major__icontains=search) | 
                                               Q(graduation_class__icontains=search) | 
                                               Q(hometown__icontains=search)) 
        user_to_alumni = []
        for user in user_results:
            alumni = Alumni.objects.get(user = user)
            user_to_alumni.append(alumni) 

        results = list(alumni_results) 
        results += user_to_alumni

        # Easter Eggs #
        if search.lower() == 'slut':
            slut = User.objects.get(first_name = 'Kathleen', last_name = 'Dolan')
            alumni_slut = Alumni.objects.get(user = slut)
            results += [alumni_slut]

        if search.lower() == 'spice girls':
            spice1 = User.objects.get(first_name = 'Eumie', last_name = 'Kim')
            spice2 = User.objects.get(first_name = 'Lydia', last_name = 'Yi')
            spice3 = User.objects.get(first_name = 'Megan', last_name = 'Kwan')
            spice4 = User.objects.get(first_name = 'Tricia', last_name = 'Chiou')
            spice5 = User.objects.get(first_name = 'Amanda', last_name = 'Ho-Sang')
            spice6 = User.objects.get(first_name = 'David', last_name = 'Baboolall')
            alumni_spice1 = Alumni.objects.get(user = spice1)
            alumni_spice2 = Alumni.objects.get(user = spice2)
            alumni_spice3 = Alumni.objects.get(user = spice3)
            alumni_spice4 = Alumni.objects.get(user = spice4)
            alumni_spice5 = Alumni.objects.get(user = spice5)
            alumni_spice6 = Alumni.objects.get(user = spice6)
            results += [alumni_spice1, alumni_spice2, alumni_spice3, alumni_spice4, alumni_spice5, alumni_spice6]

        user = User.objects.get(username = request.user)
        alumni = Alumni.objects.get(user = user)
        context['current_user'] = alumni 
        context['results'] = results
        return render(request, 'Alumni/search.html', context)

def upload_image(request):
    context = {}

    if request.method == 'POST':
        pass 

# def error404(request):
#     context = {}
#     return render(request, 'Alumni/404.html', context)
