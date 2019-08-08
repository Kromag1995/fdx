"Http response for each view"
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .forms import UserCreationForm

def regisuser(request):
    "Registration http response"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password1'])
            user.save()
            return HttpResponse('thanks :)')
        else:
            HttpResponse('something went wrong :(')
    else:
        form = UserCreationForm()
    return render(request, 'registration/form.html', {'form' : form})
