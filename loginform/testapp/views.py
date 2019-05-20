from django.shortcuts import render
from testapp.forms import LoginForm
def logn_view(request):
    sent =False
    if (request.method=='POST'):
        form=LoginForm(request.POST)
        if(form.is_valid()):
            name=form.cleaned_data['name']
            pwd=form.cleaned_data['password']
            print(name)
            print(pwd)
            sent=True
    form=LoginForm()
    return render(request,'testapp/login.html',{'form':form,'sent':sent})
# Create your   views here.
