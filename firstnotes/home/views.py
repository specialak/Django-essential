from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # return HttpResponse("<h1>Welcome to the Home Page</h1>")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    context = {
        'current_time': current_time,
    }
    return render(request, 'home/welcome.html', context)

@login_required(login_url='/admin')
def authorized(request):
    # return HttpResponse("<h1>Welcome to the Authorized Page</h1>")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    context = {
        'current_time': current_time,
        'user': request.user,  # Assuming you have user authentication set up
    }
    return render(request, 'home/authorized.html', context)
