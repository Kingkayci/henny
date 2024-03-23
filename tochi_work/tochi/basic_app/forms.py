from django_countries.fields import CountryField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here
from django import forms
from .models import UploadedImage, UploadKYC

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['username', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "type":"text", 
            "class":"receipt-input",  
            "maxlength":"16", 
            "minlength":"5",
        })



class KYCUploadForm(forms.ModelForm):
    class Meta:
        model = UploadKYC
        fields = ['card', 'imagePassport']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["card"].widget.attrs.update({
            "class":"card-input",  
        })

        self.fields["imagePassport"].widget.attrs.update({
            "class":"passport-input",  
        })

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    
    referral = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "phone", "referral")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another one.")
        return username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "type":"text", 
            "id":"firstname", 
            "class":"form-input", 
            "placeholder":"Enter First Name", 
            "maxlength":"16", 
            "minlength":"5",
        })


        self.fields["last_name"].widget.attrs.update({
            "type":"text", 
            "id":"lastname", 
            "class":"form-input", 
            "placeholder":"Enter Last Name", 
            "maxlength":"16", 
            "minlength":"5",
        })

        self.fields["username"].widget.attrs.update({
            "type":"text", 
            "id":"username", 
            "class":"form-input", 
            "placeholder":"Enter Unique Username", 
            "maxlength":"16", 
            "minlength":"5",
        })

    
        self.fields["email"].widget.attrs.update({
            "type":"email", 
            "id":"email", 
            "class":"form-input", 
            "placeholder":"name@example.com", 
            "maxlength":"30", 
            "minlength":"6",
        })
        
        self.fields["phone"].widget.attrs.update({
            "type":"number", 
            "id":"phone", 
            "class":"form-input", 
            "placeholder":"Enter Phone No.", 
            "maxlength":"30", 
            "minlength":"6",
        })

        
        self.fields["referral"].widget.attrs.update({
            "type":"text", 
            "id":"referral", 
            "class":"form-input", 
            "placeholder":"Enter Optional Referral Code", 
            "maxlength":"16", 
            "minlength":"5",
        })



        self.fields["password1"].widget.attrs.update({
            "type":"password", 
            "id":"password1", 
            "class":"form-input", 
            "placeholder":"Enter Password", 
            "maxlength":"30", 
            "minlength":"6",
        })


        self.fields["password2"].widget.attrs.update({
            "type":"password", 
            "id":"password2", 
            "class":"form-input", 
            "placeholder":"Confirm Password", 
            "maxlength":"30", 
            "minlength":"6",
        })


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user