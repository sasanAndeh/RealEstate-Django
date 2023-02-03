from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect ,Http404
from django.template import loader
from app.models import *
from app import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
@login_required(login_url='/admin/login/?next=/add-zamin')
def addz(request):
    x = request.POST
    if request.POST:
        number  = x['number']
        metr    = x['metr']
        area    = x['area']
        reg     = x['region']
        sk      = x['sk']
        sg      = x['sg']
        faz     = x['faz']
        napsh   = x['napsh']
        tawn    = x['tawn']
        price   = x['price']
        des     = x['des']
        cli     = x['client']
        c       = client.objects.get(id=cli)
        z    = zamin(number=number,metr=metr,area=area,
            region=reg,sk=sk,sg=sg,faz=faz,napsh=napsh,
            tawn=tawn,price=price,descripton=des,client=c)
        z.save()
        success_msg = True
        Template = loader.get_template('panel/add_zamin.html')
        context = {'success_msg':success_msg} 
        return HttpResponse(Template.render(context,request))
    else:
        raise  Http404()

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
@login_required(login_url='/admin/login/?next=/add-zamin')
def Delete_zamin(request,ID):
    z = zamin.objects.get(id=ID).delete()
    
    return HttpResponseRedirect('/zamins')

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
