import datetime
from datetime import datetime
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.
def index(request):
    try:
        notice = Notice.objects.filter(type=1).values()

    except User.DoesNotExist:
        return HttpResponse('报错！')
    data = {"notice": notice}
    return render(request, 'index/index.html', data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            user_ = User.objects.filter(name=name, password=password).values()
            user = User.objects.get(name=name, password=password)
        except Exception as E:
            data = {"msg": "用户名或密码错误！"}
            return render(request, 'login.html', data)
        if user_:
            request.session['name'] = {'name': user.name, "photo": str(user.photo), "type": user.type,
                                       "phone": user.phone}
            return HttpResponseRedirect('/')
        else:
            data = {"msg": "用户名或密码错误！"}
            return render(request, 'login.html', data)
    return None


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':

        name = request.POST['name']
        gender = request.POST['gender']
        photo = request.FILES.get('photo')
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        ss = User.objects.filter(name=name)
        if ss:
            data = {"msg": "用户已存在！"}
            return render(request, 'register.html', data)
        else:
            user = User.objects.create(name=name,
                                       gender=gender,
                                       photo=photo,
                                       email=email,
                                       phone=phone,
                                       password=password,
                                       )

    return HttpResponseRedirect('/login/')


def password_update(request):
    if request.method == 'GET':
        return render(request, 'password_update.html')
    elif request.method == "POST":
        name = request.session['name']
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]

        try:
            stu = User.objects.get(name=name['name'])
        except Exception as e:
            print(e)
        if stu.password == password_1:
            stu.password = password_2
            # print(stu.password,password_2)
            stu.save()
            return HttpResponseRedirect("/logout/")
        else:
            msg = "密码错误！"
            return render(request, 'password_update.html', {"msg": msg})


def add_repair(request):
    if request.method == 'GET':
        return render(request, 'add_repair.html')
    elif request.method == 'POST':
        # try:
        title = request.POST['title']
        flor = request.POST['flor']
        content = request.POST['content']
        photo = request.FILES.get('photo')
        user = request.session['name']['name']
        user = User.objects.get(name=user)
        single = 'B' + datetime.now().strftime("%H%M%S")

        Repair.objects.create(
            user=user,
            title=title,
            flor=flor,
            content=content,
            photo=photo,
            single=single

        )
        # except Exception as E:
        #     print(E)
        #     data = {"msg": "请完成填写！"}
        #     return render(request, 'add_repair.html', data)
    return HttpResponseRedirect('/record/')


def record(request):
    """记录"""
    try:
        user = request.session.get('name')['name']
        # print(user)
        if request.session['name']['type'] != 1:
            record = Repair.objects.all().order_by('-time')
        else:
            record = Repair.objects.filter(user__name=user).order_by('-time')
    except Exception as E:
        print(E)
    data = {"record": record}
    return render(request, 'record.html', data)


def logout(request):
    if 'name' in request.session:
        del request.session['name']
        # print('session  del....')

    return HttpResponseRedirect('/login/')


def audit(request, pk):
    audit = int(request.GET['audit'])
    try:
        repair = Repair.objects.get(pk=pk)

    except Repair.DoesNotExist as E:
        return HttpResponseRedirect('/record/')
    if audit == 2:
        repair.type = 3

    else:
        repair.type = 5
    repair.save()
    return HttpResponseRedirect('/record/')
