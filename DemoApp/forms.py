from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class DemandeDemoForm(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    date_naissance = forms.DateField()
    profession = forms.CharField(max_length=100)
    sexe = forms.ChoiceField(choices=(('M', 'Masculin'), ('F', 'Féminin')))
    raison_pret = forms.CharField(widget=forms.Textarea)
    montant_pret = forms.DecimalField(min_value=0)
    temps_remboursement = forms.IntegerField(min_value=1)
    carte_identite = forms.FileField()


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)