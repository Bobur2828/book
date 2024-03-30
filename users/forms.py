from django import forms
from users.models import User
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Login', 'class': 'form-control w-100'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email kiriting', 'class': 'form-control w-100'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Parol', 'class': 'form-control w-100'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Parolni tasdiqlash', 'class': 'form-control w-100'}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Ism kiriting', 'class': 'form-control w-100'}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Familiyangizni kiriting', 'class': 'form-control w-100'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2!=password:
            raise forms.ValidationError("Passwords don't match")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError("Username 5 va 30 orasida bo'lishi kerak")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email bazada mavjud")
        return email
# class RegisterForm(forms.ModelForm):
#     username=forms.CharField(label='Login kiriting')
#     password=forms.CharField(label='Parol yarating', widget=forms.PasswordInput )
#     password2=forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput )

#     class Meta:
#         model= User
#         fields=['username' ,'email','password','password2','first_name','last_name']

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password']!= cd['password2']:
           
#             raise forms.ValidationError('Parollar bir biriga mos emas')
        
#         else:
#             return cd['password2']
        
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError('Bunday email allaqachon mavjud')
#         return email
class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control w-100'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control w-100'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username)<5 or len(username)>30:
            raise forms.ValidationError("Username 5 va 30 orasida bo'lishi kerak")
        return username
    
# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username kiriting')
#     password = forms.CharField(label='Parolingizni kiriting',widget=forms.PasswordInput)