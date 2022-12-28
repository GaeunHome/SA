from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import member
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        account = request.POST.get('username')
        password = request.POST.get('password')
        try:
            unit = member.objects.get(account=account)
            if unit.password==password:
                request.session['account'] = unit.account
                return HttpResponseRedirect('/member/')
            else:
                return render(request, 'signin.html', locals())
        except ObjectDoesNotExist:
            return HttpResponse("此帳號未被註冊")

def vip(request):
    if 'account' in request.session:
        account = request.session['account']
        unit = member.objects.get(account=account)
        return render(request, 'member.html', locals())
    else:
        return HttpResponseRedirect( '/signin/')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        uaccount = request.POST.get('account')
        upassword = request.POST.get('password')
        upassword2 = request.POST.get('password2')
        uphone = request.POST.get('phone')
        uemail = request.POST.get('email')
        uname = request.POST.get('name')
        if upassword!=upassword2:
            return render(request, 'signup.html', locals())
        member.objects.create(account=uaccount, password=upassword, phone=uphone, email=uemail, name=uname)
        return HttpResponse("資料已被填入") 
        
def passbook(request):
    return render(request, 'passbook.html')
