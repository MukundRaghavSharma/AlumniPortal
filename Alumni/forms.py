from Alumni.models import Alumni, PledgeClass
from django import forms
from django.contrib.auth.models import User
import datetime
import re

CHOICES = [ x for x in range(2004, datetime.date.today().year + 2) ]
CHOICES[0] = (0, 'Select your graduation year')
for i in range(1, len(CHOICES)):
    CHOICES[i] = (i, CHOICES[i])
CHOICES = tuple(CHOICES)

class SignUpForm(forms.Form):
    first_name = forms.CharField(label = 'First Name',
                                 required = True,
                                 max_length = 100,)
    
    last_name = forms.CharField(label = 'Last Name',
                                 required = True,
                                 max_length = 100,)
    
    username = forms.CharField(label = 'Username',
                               required = True,
                               max_length = 100,)
    
    email = forms.EmailField(label = 'Email',
                             max_length = 100,)
    
    password1 = forms.CharField(label = 'Password',
                               widget = forms.PasswordInput())

    password2 = forms.CharField(label = 'Re-enter your password',
                               widget = forms.PasswordInput()) 

    class Meta:
        model = Alumni
        fields = [ ]


        def clean(self):
            pass

        def save(self):
            pass


class SignInForm(forms.ModelForm):
    username = forms.CharField(label = 'Username',
                               required = True,
                               max_length = 100,)
    
    password1 = forms.CharField(label = 'Password',
                               widget = forms.PasswordInput())

    '''
    class Meta:
    model = User
    fields = ['username', 'password']

    def clean(self):
    cleaned_data = super(SignInForm, self).clean()
    if 'password' not in self.cleaned_data:
    raise forms.ValidationError("Enter the password!")
    return self.cleaned_data

    def save(self, commit = True):
    user = super(SignInForm, self).save(commit = False)
    user.set_password(self.cleaned_data['password'])
    if commit:
    user.save()
    return user
    '''

# Personal - AKPsi - Professional Information #
class PersonalInformationForm(forms.Form):

    # First Name #
    first_name = forms.CharField(label = 'First Name',
                            max_length = 100,
                            required = True,
                            widget = forms.TextInput(
                                attrs = { 'id' : 'first_name', 'class' : 'form-control', 'placeholder': 'First Name' }))

    # Last name #
    last_name = forms.CharField(label = 'Last Name',
                                max_length = 100,
                                required = True,
                                widget = forms.TextInput(
                                    attrs = { 'id' : 'last_name', 'class' : 'form-control', 'placeholder': 'Last Name' }))

    # Email #
    email = forms.EmailField(label = 'Email',
                             max_length = 100,
                             required = True,
                             widget = forms.TextInput(
                                attrs = { 'id' : 'email', 'class' : 'form-control', 'placeholder': 'Email' }))

    # Phone Number #
    phone = forms.CharField(label = 'Phone',
                            required = True,
                            max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'phone', 'class' : 'form-control', 'placeholder': 'Phone Number' }))

    # Password 1 #
    password1 = forms.CharField(label = 'Password',
        required = True,
                               widget = forms.PasswordInput(attrs = { 'id' : 'password', 'class' : 'form-control', 'placeholder': 'Password' }))

    # Password 2 #
    password2 = forms.CharField(label = 'Re-enter your password', required = True,
                               widget = forms.PasswordInput(attrs = { 'id' : 'password_confirmation', 'class' : 'form-control', 'placeholder': 'Re-type Password' })) 

    def clean(self):
        #phone_regex = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
        email_regex = re.compile("^[-!#$%&'*+/0-9=?A-Z^_a-z{|}~](\.?[-!#$%&'*+/0-9=?A-Z^_a-z{|}~])*@[a-zA-Z](-?[a-zA-Z0-9])*(\.[a-zA-Z](-?[a-zA-Z0-9])*)+$")
        form_data = self.cleaned_data
        print(form_data)
        #isValidPhone = phone_regex.search(form_data['phone'])
        isValidEmail = email_regex.search(form_data['email'])


        if 'password1' not in form_data:
            self._errors["password1"] = ["A Password is Required."] # Will raise a error message
        elif 'password2' not in form_data:
            self._errors["password2"] = ["A Password is Required."] # Will raise a error message
        elif form_data['password1'] != form_data['password2']:
            self._errors["password2"] = ["Passwords do not match"] # Will raise a error message
            self._errors["password1"] = ["Passwords do not match"] # Will raise a error message
            del form_data['password1']
            del form_data['password2']
        if isValidEmail is None:
            self._errors["email"] = ["A Valid Email Address is Required."] # Will raise a error message
        #if isValidPhone is None:
        #    print(145)
        #    self._errors["phone"] = ["A Valid Phone Number is Required."] # Will raise a error message
        return form_data



class AKPsiInformationForm(forms.Form):

    # Pledge Class #
    pledge_class = forms.ModelChoiceField(queryset = PledgeClass.objects.all().
                                          order_by('class_number'),
                                          empty_label = "Select your pledge class",
                                          widget=forms.Select(attrs={'class':'form-control', 'id' : 'pledge_class'})) 

    CHOICES = [ x for x in range(2004, datetime.date.today().year + 2) ]
    CHOICES[0] = (0, 'Select your graduation year')
    for i in range(1, len(CHOICES)):
        CHOICES[i] = (i, CHOICES[i])
    CHOICES = tuple(CHOICES)

    # Graduation Year #
    graduation_year = forms.ChoiceField(choices = CHOICES, widget =
            forms.Select(attrs={'class':'form-control', 'id' : 'graduation_year'}), required = True)

    # Hometown #
    hometown = forms.CharField(label = 'Hometown',
                               required = True,
                               max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'hometown', 'class' : 'form-control', 'placeholder': 'Hometown' }))

    # Major # 
    major = forms.CharField(label = 'Major',
                            required = True,
                            max_length = 100,widget = forms.TextInput(attrs = { 'id' : 'major', 'class' : 'form-control', 'placeholder': 'Major' }))

class ProfessionalInformationForm(forms.Form):
    
    # Current Employer #
    current_employer = forms.CharField(label = 'Current Employer',
                            required = True,
                            max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'current_employer', 'class' : 'form-control', 'placeholder': 'Current Employer' }))

    # Current Role in the Company #
    role = forms.CharField(label = 'Role',
                           required = True,
                           max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'role', 'class' : 'form-control', 'placeholder': 'Role' }))
    # Current City #
    current_city = forms.CharField(label = 'Current City',    
                                   required = True,
                                   max_length = 100,widget = forms.TextInput(attrs = { 'id' : 'current_city', 'class' : 'form-control', 'placeholder': 'Current City' }))

