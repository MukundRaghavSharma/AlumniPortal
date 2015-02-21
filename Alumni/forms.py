from django import forms
from django.contrib.auth.models import User
from Alumni.models import Alumni

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
    email = forms.EmailField(label = "Email",
                            widget = forms.TextInput( 
                                attrs = { 'id' : 'email' }),)

    password = forms.CharField(label = 'Enter your Password', 
                                max_length = 100,
                                widget = forms.PasswordInput(
                                    attrs = {'id' : 'password'}))

    class Meta:
        model = User
        fields = ['email', 'password']

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
