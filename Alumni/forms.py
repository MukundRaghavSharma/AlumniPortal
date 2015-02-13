from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(label = 'First Name',

                                 required = True,
                                 max_length = 100,)
    
    last_name = forms.CharField(label = 'Last Name',
                                 required = True,
                                 max_length = 100,)
    
    username = forms.CharField(label = 'Last Name',
                               required = True,
                               max_length = 100,)
    
    email = forms.EmailField(label = 'Email',
                             max_length = 100,)
    
    password1 = forms.CharField(label = 'Enter your password',
                               widget = forms.PasswordInput())

    password2 = forms.CharField(label = 'Re-enter your password',
                               widget = forms.PasswordInput()) 

# Not used but can be activated! #
class SignInForm(forms.Form):

    username = forms.CharField(label = 'Last Name',
                               required = True,
                               max_length = 100,)
    
    password = forms.CharField(label = 'Password',
                               widget = forms.PasswordInput())
