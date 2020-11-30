from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def egister(request):
    if request.method != 'POST':
        form = UserCreationForm() #blank form
    else:
        form = UserCreationForm(data=request.POST) 

            if form.is.valid():
                new_user = form.save()
                login(requset, new_user)
                return redirect('learning_logs:index')
    
    context = {'form': form}
    return render(reqeust, 'registration/register.html')