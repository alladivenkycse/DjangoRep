from testapp.models import Movie
from django import forms
from  testapp.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"
