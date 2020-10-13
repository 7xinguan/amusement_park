from django.http import JsonResponse

# from django.db.utils import IntegrityError
# from django.shortcuts import render

# Create your views here.
from manager.models import Tourist


def log_in(request):
    if request.method == "POST":
        data_getter = request.POST
    elif request.method == "GET":
        data_getter = request.GET
    else:
        return JsonResponse({"success": 0, "msg": "注册失败"})

    username = data_getter.get('username')
    password = data_getter.get('password')
    name = data_getter.get('name')
    sex = data_getter.get('sex')
    Tourist.create(username=username, password=password, name=name, sex=sex)
    # return JsonResponse({"status": 1, "msg": "注册成功"})
    # except IntegrityError:
    # return JsonResponse({"success": 0, "msg": "注册失败"})
