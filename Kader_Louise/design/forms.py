from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm 
from django.contrib.auth import get_user_model
from design.models import *

#Formulaire de login
class loginForm(forms.Form): 
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
#Formulaire d'inscription
class signupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=('username','first_name','last_name','email','adresse','telephone')

class userUpdateForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=('username','first_name','last_name','email','adresse','telephone')
#Formulaire de post modele
class modeleForm(forms.ModelForm):    
    class Meta:
        model=Modele
        fields='__all__'

class accessoireForm(forms.ModelForm):
    class Meta:
        model=Accessoire
        fields='__all__'

class rdv_clientForm(forms.ModelForm):
    class Meta:
        model=Rdv
        fields=['date_rdv','objet']

class rdv_adminForm(forms.ModelForm):    
    class Meta:
        model=Rdv
        fields='__all__'

class cmdmodel_clientForm(forms.ModelForm):
    class Meta:
        model=Commandemodele
        fields=['modele','taille','reception']

class cmdaccessoire_clientForm(forms.ModelForm):
    class Meta:
        model=Commandeaccessoire
        fields=['accessoire','reception']

class cmdmodele_adminform(forms.ModelForm):
    class Meta:
        model=Commandemodele
        fields='__all__'

class cmdaccessoire_adminform(forms.ModelForm):
    class Meta:
        model=Commandeaccessoire
        fields='__all__'
        