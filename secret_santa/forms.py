from django import forms

class SignUpForm(forms.Form):
	name = forms.CharField(required=True)
	budget = forms.IntegerField(required=True)
	like = forms.CharField(required=True)
	dislike = forms.CharField(required=True)	
	address = forms.CharField(required=True)
	email = forms.EmailField(required=True)