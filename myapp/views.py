from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from myapp.models import member, question, transaction, product
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
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
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
        member.objects.create(account=uaccount, password=upassword, phone=uphone, email=uemail, name=uname, GPOINT=0)
        messages.success(request, "恭喜！註冊成功")
        return HttpResponseRedirect('/signin/')

def passbook(request):
    if 'account' in request.session:
        account = request.session['account']
        unit = member.objects.get(account=account)
        passbook = transaction.objects.filter(MEMID=account)
        return render(request, 'passbook.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')

def productlist(request):
    if 'account' in request.session:
        account = request.session['account']
        products = product.objects.all()
        return render(request, 'Redemption.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')

def products(request):
    if request.method == 'GET':
        return render(request, 'Redemption.html')
    elif request.method == 'POST':    
        if 'account' in request.session:
            account = request.session['account']
            mem = member.objects.get(account=account)
            productnum = request.POST.get('go')
            products = product.objects.get(productID=productnum)
            return render(request, 'commodity.html', locals())
        else:
            messages.error(request, "您還未登入！！")
            return HttpResponseRedirect('/signin/')

def report(request):
    if 'account' in request.session:
        account = request.session['account']
        if request.method == 'GET':
            return render(request, 'question.html')
        elif request.method == 'POST':
            content = request.POST.get('content')
            question.objects.create(account=account, question=content)
            messages.success(request, "已將您的問題回報了！會儘速解決您的問題")
            return render(request, 'question.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')

def signout(request):
    del request.session['account']
    messages.success(request, "您已登出")
    return HttpResponseRedirect('/signin/')
