from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

def welcome_page(request):
    return render(request, 'landing.html')
# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'education.html')

def health(request):
    return render(request, 'health.html')

def justice(request):
    return render(request, 'justice.html')

def laworder(request):
    return render(request, 'laworder.html')

def publicworks(request):
    return render(request, 'publicworks.html')

def revenue(request):
    return render(request, 'revenue.html')

def next_page(request):
    return render(request, 'login.html')

'''

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
'''
# login page
def user_login(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('pass')
         print(username,password)
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request,user)         
            return redirect('/index.html/')
       
# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

