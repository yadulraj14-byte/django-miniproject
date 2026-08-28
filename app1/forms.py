from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Job,Application,UserProfile

class LoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "class":"form-control"
      }
    )
  )
  password=forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        "class":"form-control"
      }
    )
  )


class SignUpForm(UserCreationForm):
  username= forms.CharField(
    widget=forms.TextInput(
      attrs={
        "class":"form-control"
      }
    )
  )
  password1 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        "class":"form-control"
      }
    )
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        "class":"form-control"
      }
    )
  )
  email = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "class":"form-control"
      }
    )
  )

  class Meta:
    model = User
    fields = ('username','email','password1','password2','is_admin','is_candidate','is_recruiter')


class Jobform(forms.ModelForm):
  class Meta:
    model=Job
    fields = "__all__"
    widgets = {
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Position'
            }),

            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Company Name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'details': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
        }
    
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = [
            "phone",
            "qualification",
            "experience",
            "skills",
            "resume",
            "cover_letter",
        ]

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),

            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. BCA'
            }),

            'experience': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Fresher'
            }),

            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Python, Django, HTML, CSS...'
            }),

            'resume': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write a short cover letter...'
            }),
        }
    
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            "phone",
            "qualification",
            "skills",
            "address",
            "profile_picture",
        ]

        widgets = {

            "phone": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "qualification": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "skills": forms.Textarea(attrs={
                "class":"form-control",
                "rows":4
            }),

            "address": forms.Textarea(attrs={
                "class":"form-control",
                "rows":3
            }),

            "profile_picture": forms.FileInput(attrs={
                "class":"form-control"
            }),

        }