from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Event, Plot, Resource, Transaction

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'photo']


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y', attrs={'type': 'date'}))
    class Meta:
        model = Event
        fields = ['title', 'date', 'description', 'photo']


class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['owner', 'plot_number', 'area', 'photo']

class EditPlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['owner', 'plot_number', 'area', 'photo']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'content', 'resource_type']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['membership_fee']

    def clean_membership_fee(self):
        membership_fee = self.cleaned_data.get('membership_fee')
        if membership_fee < 0:
            raise forms.ValidationError("Membership fee cannot be negative.")
        return membership_fee
