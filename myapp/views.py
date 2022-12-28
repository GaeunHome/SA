from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from myapp.models import member
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# 登入已完成優化
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
                messages.error(request, "密碼錯誤")
                return render(request, 'signin.html', locals())
        except ObjectDoesNotExist:
            messages.error(request, "帳號不存在")
            return render(request, 'signin.html', locals())

def vip(request):
    if 'account' in request.session:
        account = request.session['account']
        unit = member.objects.get(account=account)
        return render(request, 'member.html', locals())
    else:
        return HttpResponseRedirect( '/signin/')
# 註冊已完成優化
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        uaccount = request.POST.get('account')
        check_account = member.objects.filter(account=uaccount).first()
        if check_account!= None:
            messages.error(request, "此帳號已被註冊過")
            return render(request, 'signup.html', locals())
        upassword = request.POST.get('password')
        upassword2 = request.POST.get('password2')
        uphone = request.POST.get('phone')
        uemail = request.POST.get('email')
        uname = request.POST.get('name')
        if upassword!=upassword2:
            messages.error(request, "兩次密碼不正確")
            return render(request, 'signup.html', locals())
        member.objects.create(account=uaccount, password=upassword, phone=uphone, email=uemail, name=uname)
        messages.success(request, "恭喜！註冊成功")
        return HttpResponseRedirect('/signin/')
        
def passbook(request):
    return render(request, 'passbook.html')
