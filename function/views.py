
# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


def index(request):
    return render(request, 'function/index.html')


def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'function/login.html', locals())

            if user.password == password:
                return redirect('/welcome/')
            else:
                message = '密码不正确！'
                return render(request, 'function/login.html', locals())
        else:
            return render(request, 'function/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'function/login.html', locals())

def logout(request):
    pass
    return redirect("/login")

def welcome(request):
    return render(request, 'function/welcome.html')


def tourist_info(request):
    return render(request, 'function/tourist_management/tourist_info.html')


def event_archiving(request):
    return render(request, 'function/tourist_management/event_archiving.html')


def notice_management(request):
    return render(request, 'function/notice_management.html')


def project_management(request):
    return render(request, 'function/project_management.html')
