from django import forms
class LoginForm(forms.Form):
    name=forms.CharField(label="Enter Name",max_length=20,)
    password=forms.CharField(widget=forms.Textarea,rows=40)
