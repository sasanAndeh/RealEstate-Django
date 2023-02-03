from django.shortcuts import render ,HttpResponse
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from app.models import *
from app import models
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

REGION_CHOICES = (
        ('شهرک کارمندان','شهرک کارمندان'),('کویی بهداری','کویی بهداری'),('سپاه نور','سپاه پیام نور'),('بهارستان','بهارستان'),('قلقلاغ','قلقلاغ'),
        ('شهرک معراج','شهرک معراج'),('فاز 3 پیام','فاز 3 پیام'),('شهرک خانی','شهرک خانی'),('شهرک نور','شهرک نور'),('فاز 2 پیام','فاز دو پیام'),
        ('فرمانداری','فرمانداری'),('گلستان','گلستان'),('سپاه هنرستان قدیم','سپاه هنرستان قدیم'),('کوی دادگستری','کوی دادگستری'),('نهضت','نهضت'),
        ('بهزیستی','بهزیستی'),('کارکنان شهرداری','کارکنان شهرداری'),('تاناکورا','تاناکورا'),('گوی هه ژار','کوی هه ژار'),('باغ گولان','باغ گولان'),
        ('بسیج','بسیج'),('تپه هما','تپه هما'),('شهرک فجر','شهرک فجر'),('بهار 1','بهار1'),('بهار 2','بهار2'),('بنیاد شهید فاز 1','بنیاد شیهد فاز1'),
        ('بنیاد شهید فاز 2','بنیاد شهید فاز2'),('بنیاد شهید فاز 3','بنیاد شهید فاز3'),('شهرک پیشوا','شهرک پیشوا'),('شهرک خیام','شهرک خیام'),('خبازان','خبازان'),
        ('کارکنان شهرداری','کارکنان شهردای'),('صداوسیما','صداوسیما'),('کوی فرهنیگان','کوی فرهنگیان'),('مکریان','مکریان'),('زمین شهری','زمین شهری'),
        ('کوی استادان','کوی استادان'),('شهرک پویا','شهرک پویا'),('شهرک نیاوران','شهرک نیاوران'),('پتو بافی تارا','پتوبافی تارا'),('جانبازان','جانبازان'),
        ('آزادگان','آزادگان'),('صبح مکریان','صبح مکریان'),('نیرو انتظامی','نیرو انتظامی'),('شهرک صنفی','شهرک صنفی'),('شهرک صبا','شهرک صبا'),
        ('شهرک صنعتی','شهرک صنعتی'),('روستایی',' روستایی'))
# Create your views here.


def index(request):
    Template = loader.get_template('index.html')
    return HttpResponse(Template.render(request=request))



def Panel(request):
    Template = loader.get_template('panel/index.html')
    zamins = zamin.objects.all()[::-1]#zamin.objects.latest('id')
    builds = build.objects.all()[::-1]#build.objects.latest('id')
    context = {'zamin':zamins,
    'build':builds } 
    return HttpResponse(Template.render(context,request))

def zamins(request):
    Template = loader.get_template('panel/zamins.html')
    zamins = zamin.objects.all()
    context = {'zamins':zamins,
    'regs':REGION_CHOICES,} 
    return HttpResponse(Template.render(context,request))

def builds(request):
    Template = loader.get_template('panel/builds.html')
    builds = build.objects.all()
    context = {'builds':builds,
    'regs':REGION_CHOICES,} 
    return HttpResponse(Template.render(context,request))


def lease_view(request):
    Template = loader.get_template('panel/lease.html')
    leases = lease.objects.all()
    context = {'leases':leases} 
    return HttpResponse(Template.render(context,request))



@login_required(login_url='/admin/login/?next=/add-zamin')
def add_zamin(request):
    Template = loader.get_template('panel/add_zamin.html')
    context = {'regs':REGION_CHOICES,
    'sk' : models.BORDER_CHOICES4,
    'sg' : models.BORDER_CHOICES5,
    'clients' : client.objects.all(),
    'range': range(1,10),
    'Nrange': range(1,4),
    } 
    return HttpResponse(Template.render(context,request))




@login_required(login_url='/admin/login/?next=/add-build')
def add_build(request):
    Template = loader.get_template('panel/add_build.html')
    context = {'regs':REGION_CHOICES,
    'sk' : models.BORDER_CHOICES4,
    'sg' : models.BORDER_CHOICES5,
    'clients' : client.objects.all(),
    'range': range(1,10),
    'Nrange': range(1,4),
    } 
    return HttpResponse(Template.render(context,request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/','test')