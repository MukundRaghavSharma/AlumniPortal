from Alumni.models import Alumni, PledgeClass
from django import forms
from django.contrib.auth.models import User
import datetime

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
                            widget = forms.TextInput(
                                attrs = { 'id' : 'first_name', 'class' : 'form-control', 'placeholder': 'First Name' }))

    # Last name #
    last_name = forms.CharField(label = 'Last Name',
                                max_length = 100,
                                widget = forms.TextInput(
                                    attrs = { 'id' : 'last_name', 'class' : 'form-control', 'placeholder': 'Last Name' }))

    # Email #
    email = forms.EmailField(label = 'Email',
                             max_length = 100,
                             widget = forms.TextInput(
                                attrs = { 'id' : 'email', 'class' : 'form-control', 'placeholder': 'Email' }))

    # Password 1 #
    password1 = forms.CharField(label = 'Password',
                               widget = forms.PasswordInput(attrs = { 'id' : 'password', 'class' : 'form-control', 'placeholder': 'Password' }))

    # Password 2 #
    password2 = forms.CharField(label = 'Re-enter your password',
                               widget = forms.PasswordInput(attrs = { 'id' : 'password_confirmation', 'class' : 'form-control', 'placeholder': 'Re-type Password' })) 

    def clean(self):
        if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            raise ValidationError("Passwords must match!")
        return self.cleaned_data

class AKPsiInformationForm(forms.Form):
    # Pledge Class #
    pledge_class = forms.ModelChoiceField(queryset = PledgeClass.objects.all().
                                          order_by('year'),
                                          empty_label = "Select your pledge class",
                               widget=forms.Select(attrs={'class':'form-control'})) 

    CHOICES = [ x for x in range(2004, datetime.date.today().year + 2) ]
    CHOICES[0] = (0, 'Select your graduation year')
    for i in range(1, len(CHOICES)):
        CHOICES[i] = (i, CHOICES[i])
    CHOICES = tuple(CHOICES)

    # Graduation Year #
    graduation_year = forms.ChoiceField(choices = CHOICES, widget =
            forms.Select(attrs={'class':'form-control'}), required = True)

    # Phone Number #
    phone = forms.CharField(label = 'Phone',
                            required = True,
                            max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'phone', 'class' : 'form-control', 'placeholder': 'Phone Number' }))

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

class EditForm(forms.Form):

    # First Name #
    first_name = forms.CharField(label = 'First Name',
                            max_length = 100,
                            widget = forms.TextInput(
                                attrs = { 'id' : 'first_name', 'class' : 'form-control', 'placeholder': 'First Name' }))

    # Last name #
    last_name = forms.CharField(label = 'Last Name',
                                max_length = 100,
                                widget = forms.TextInput(
                                    attrs = { 'id' : 'last_name', 'class' : 'form-control', 'placeholder': 'Last Name' }))

    # Password 1 #
    password1 = forms.CharField(label = 'Password',
                               widget = forms.PasswordInput(attrs = { 'id' : 'password', 'class' : 'form-control', 'placeholder': 'Password' }))

    # Password 2 #
    password2 = forms.CharField(label = 'Re-enter your password',
                               widget = forms.PasswordInput(attrs = { 'id' : 'password_confirmation', 'class' : 'form-control', 'placeholder': 'Re-type Password' })) 
    
    # Pledge Class #
    #pledge_class = forms.ModelChoiceField(queryset = PledgeClass.objects.all().
    #                                      order_by('year'),
    #                                      empty_label = "Select your pledge class",
    #                           widget=forms.Select(attrs={'class':'form-control'})) 
    # Graduation Year #
    #graduation_year = forms.ChoiceField(choices = CHOICES, widget =
    #        forms.Select(attrs={'class':'form-control'}), required = True)

    # Phone Number #
    phone = forms.CharField(label = 'Phone',
                            required = True,
                            max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'phone', 'class' : 'form-control', 'placeholder': 'Phone Number' }))

    # Hometown #
    hometown = forms.CharField(label = 'Hometown',
                               required = True,
                               max_length = 100, widget = forms.TextInput(attrs = { 'id' : 'hometown', 'class' : 'form-control', 'placeholder': 'Hometown' }))

    # Major # 
    major = forms.CharField(label = 'Major',
                            required = True,
                            max_length = 100,widget = forms.TextInput(attrs = { 'id' : 'major', 'class' : 'form-control', 'placeholder': 'Major' }))

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

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'no no no'))

        return self.cleaned_data
