from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
# Create your views here.
from client.models import  client_info 

def create_account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            password = request.POST.get('password')
            user = User.objects.create(
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                username = request.POST.get('username'),
                email = request.POST.get('email')
            )
            user.set_password(password)
            user.save()
        return render(request,"create_account.html")
    else:
         return redirect('/%s?next=%s' % ('admin/login/', request.path))

def login_view(request):
    form = AuthenticationForm()
    error = None
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('admin_panel:dashboard')
            else:
                error = "Invalid login"
        else:
            error = "Invalid login"
    return render(request, "login.html",{"form":form, "error":error})

def dashboard(request):
    if request.user.is_authenticated:
        context = None
        info = client_info.objects.filter(status="Not Generated")
        context = {
            "infos":info
        }
        return render(request,"dashboard.html",context)
    else:
        return redirect('admin_panel:login')

def logout_view(request):
    logout(request)
    return redirect('admin_panel:login_view')

def update_into_generated(request):
    if request.method == 'POST':
        ids = request.POST.get("infos")
        for id in ids:
            info = client_info.objects.get(id.id)
            info.status = "Genarated"
            response = info.save()
        if response:
            return HttpResponse("Updated successfully")
        else:
            return HttpResponse("Not updated")
   