from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from myapp.models import member, question, transaction, product, rankinfo
from django.core.exceptions import ObjectDoesNotExist
from myapp.serializers import myappSerializer
from rest_framework import viewsets


# Create your views here.
# 登入已完成優化 # 會員編號尚未完成
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
# 登出
def signout(request):
    del request.session['account']
    messages.success(request, "您已登出")
    return HttpResponseRedirect('/signin/')
# 會員介面
def vip(request):
    if 'account' in request.session:
        account = request.session['account']
        unit = member.objects.get(account=account)
        rank = rankinfo.objects.all()
        if unit.GPOINT >= 50000:
            present = rankinfo.objects.get(rankname="環保大師")
        elif unit.GPOINT < 50000 & unit.GPOINT >= 20000:
            present = rankinfo.objects.get(rankname="環保鑽石鬥士")
        elif unit.GPOINT < 20000 & unit.GPOINT >= 10000:
            present = rankinfo.objects.get(rankname="環保白金鬥士")
        else:
            present = rankinfo.objects.get(rankname="環保黃金鬥士")
        return render(request, 'member.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 碳權存摺
def passbook(request):
    if 'account' in request.session:
        account = request.session['account']
        unit = member.objects.get(account=account)
        passbook = transaction.objects.filter(MEMID=account)
        return render(request, 'passbook.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 碳權點數商城
def productlist(request):
    if 'account' in request.session:
        account = request.session['account']
        products = product.objects.all()
        return render(request, 'shoppingmall.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 「食」頁面
def daily(request):
    if 'account' in request.session:
        account = request.session['account']
        pro = product.objects.filter(productkind="食")
        return render(request, 'dailylife.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 「行」頁面
def travel(request):
    if 'account' in request.session:
        account = request.session['account']
        pro = product.objects.filter(productkind="行")
        return render(request, 'travel.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 碳權點數商品
def products(request):
    if request.method == 'POST':
        if 'account' in request.session:
            account = request.session['account']
            mem = member.objects.get(account=account)
            productnum = request.POST.get('go')
            products = product.objects.get(productID=productnum)
            if mem.GPOINT < products.productlimit:
                messages.error(request, "您的段位未到達，請努力累積碳權點數")
                return redirect('/productlist/')
            else:
                return render(request, 'commodity.html', locals())
        else:
            messages.error(request, "您還未登入！！")
            return HttpResponseRedirect('/signin/')
# 問題回報
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
# 購買
def buy(request):
    if 'account' in request.session:
        account = request.session['account']
        if request.method == 'GET':
            return render(request, 'Redemption.html')
        elif request.method == 'POST':
            pro = product.objects.get(productID=request.POST.get('pro'))
            info = member.objects.get(account=account)
            number = int(request.POST.get('number'))
            if (info.GPOINT - pro.productpoint*number) < 0:
                messages.error(request, "對不起！您的碳權點數不夠買該商品")
                return HttpResponseRedirect('/productlist/')
            total = info.GPOINT - pro.productpoint*number
            member.objects.update(GPOINT=total)
            transaction.objects.create(
                PROID=pro.productID, MEMO=pro.productname+"兌換", PRONAME=pro.productname,
                MEMID=account, CDATE=timezone.now(), GPOINT=pro.productpoint*number, 
                AMOUNT=0, TIME=number, BALANCE=total, APPID=10)
            messages.success(request, "兌換成功！！")
            return HttpResponseRedirect('/productlist/')
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 兌換條碼
def qrcode(request):
    if 'account' in request.session:
        account = request.session['account']
        qr = transaction.objects.filter(MEMID=account)
        pro = product.objects.all()
        return render(request, 'voucher.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 修改會員資料介面
def memberset(request):
    if 'account' in request.session:
        account = request.session['account']
        mem = member.objects.get(account=account)
        return render(request, 'memberset.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 修改會員資料
def modify(request):
    if 'account' in request.session:
        account = request.session['account']
        mem = member.objects.get(account=account)
        if request.method == 'POST':
            member.objects.update(
                name=request.POST.get('name'), phone=request.POST.get('phone'),
                nname=request.POST.get('nname'), email=request.POST.get('email'))
            messages.success(request, "修改成功")
            return HttpResponseRedirect('/memberset/')

    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 排位詳細介面
def ranklist(request):
    if 'account' in request.session:
        account = request.session['account']
        mem = member.objects.get(account=account)
        rank = rankinfo.objects.all()
        if mem.GPOINT >= 50000:
            present = rankinfo.objects.get(rankname="環保大師")
        elif mem.GPOINT < 50000 & mem.GPOINT >= 20000:
            present = rankinfo.objects.get(rankname="環保鑽石鬥士")
        elif mem.GPOINT < 20000 & mem.GPOINT >= 10000:
            present = rankinfo.objects.get(rankname="環保白金鬥士")
        else:
            present = rankinfo.objects.get(rankname="環保黃金鬥士")
        return render(request, 'leaderboard.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 對接頁面
def service(request):
    if 'account' in request.session:
        account = request.session['account']
        return render(request, 'service.html', locals())
    else:
        messages.error(request, "您還未登入！！")
        return HttpResponseRedirect('/signin/')
# 對接測試
class myappViewSet(viewsets.ModelViewSet):
    queryset = transaction.objects.all()
    serializer_class = myappSerializer