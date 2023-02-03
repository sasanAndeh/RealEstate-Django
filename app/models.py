
from django.db import models
from django.utils import timezone
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

BORDER_CHOICES4 = (('1','خیابان'),('2','کوچه'),)  
BORDER_CHOICES5 = (('1','سند'),('2','قرار داد'),)     
STATUS_CHOICES = (
        ('1','published'),
        ('2','unpublished'),
        ('3','skip') )
FAZ_CHOICES2 = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),)
NAPSH_CHOICES3 = (
        ('1','1'),('2','2'),('3','3'),('4','4'))

# Create your models here.


class client(models.Model):
    f_name = models.CharField("نام", max_length=50)
    l_name = models.CharField("نام خانوداگی", max_length=50,null=True)
    number = models.CharField(max_length=13,verbose_name='شماره همراه')
    def __str__(self):
        return self.f_name +' '+ self.l_name
    class Meta():
        app_label           = 'app'
        verbose_name        = 'مالک'
        verbose_name_plural = 'مالکین'
     
class Informations(models.Model):
    number      = models.CharField(max_length=9,verbose_name='قطعه',null=True,blank=True)
    metr        = models.CharField(max_length=9,verbose_name='متراژ زمین',null=True,blank=True)
    area        = models.CharField(max_length=3,verbose_name='دهنه',null=True,blank=True)
    region      = models.CharField(choices=REGION_CHOICES,max_length=100,verbose_name='منطقه', default='کویی بهداری')
    tawn        = models.CharField(max_length=20,verbose_name='شهر',null=True,blank=True)
    faz         = models.CharField(choices=FAZ_CHOICES2,verbose_name='فاز',max_length=20,blank=True)
    napsh       = models.CharField(choices=NAPSH_CHOICES3,verbose_name='نپش',max_length=10,blank=True)
    sk          = models.CharField(choices=BORDER_CHOICES4,verbose_name='خ - ک', max_length=20,blank=True)
    sg          = models.CharField(choices=BORDER_CHOICES5,verbose_name='س - ق', max_length=20,blank=True)
    price       = models.CharField(max_length=100,verbose_name='قیمت',null=True,blank=True)
    priced      = models.BooleanField(default=False,verbose_name='وضعت فروش : ')
    client      = models.ForeignKey(client,verbose_name='مشتری',null=True,on_delete=models.DO_NOTHING,blank=True)
    status      = models.BooleanField(default=False,verbose_name='وضعیت انتشار: ')
    descripton  = models.TextField(verbose_name='توضیحات',null=True,blank=True)
    time        = models.DateTimeField(default=timezone.now)
    class meta:
        abstract = True

class zamin(Informations):
    def __str__(self):
        return self.region
    class Meta():
        app_label           = 'app'
        verbose_name        = 'زمین'
        verbose_name_plural = 'زمین ها'


class build(Informations):
    floor       = models.CharField(max_length=3,verbose_name='تعداد طبقه',null=True,blank=True)
    rooms       = models.CharField(max_length=3,verbose_name='تعداد اتاق',null=True,blank=True)
    parking     = models.BooleanField(default=False,verbose_name='پارکینگ دارد : ')
    metr_b       = models.CharField(max_length=10,verbose_name='زیربنا ساختمان',null=True,blank=True)
    finished    = models.BooleanField(default=False,verbose_name='پایانه کار : ')
    def __str__(self):
        return self.region
    class Meta():
        app_label           = 'app'
        verbose_name        = 'ساختمان'
        verbose_name_plural = 'ساختمان ها'

class Garden(Informations):
    hektar_z    = models.CharField(max_length=100,verbose_name=' هکتار زمین',null=True,blank=True)
    inch        = models.CharField(max_length=5,verbose_name='اینج آب',null=True,blank=True)
    ls          = models.CharField(choices=BORDER_CHOICES4,verbose_name='اجاره - خرید', max_length=20)
    gz          = models.CharField(choices=BORDER_CHOICES4,verbose_name='زمین - باغ', max_length=20) 
    chaeh       = models.BooleanField(default=False,verbose_name='چاه دارد؟')
    def __str__(self):
        return self.hm
    class Meta():
        app_label           = 'app'
        verbose_name        = 'باغ'
        verbose_name_plural = 'باغ ها'

class lease(Informations):
    BORDER_CHOICES5 = (
        ('مغازه','مغازه'),('خانه','خانه'),) 
    floor       = models.CharField(max_length=3,verbose_name='تعداد طبقه',null=True,blank=True)
    rooms       = models.CharField(max_length=5,verbose_name='تعداد اتاق',null=True,blank=True)
    parking     = models.BooleanField(default=False,verbose_name='پارکینگ دارد : ')
    hm          = models.CharField(choices=BORDER_CHOICES5,verbose_name='خ - م', max_length=20)
    leas        = models.CharField(max_length=30,verbose_name='اجاره',null=True,blank=True)
    mortgae     = models.CharField(max_length=30,verbose_name='رهن',null=True,blank=True)
    def __str__(self):
        return self.hm
    class Meta():
        app_label           = 'app'
        verbose_name        = 'اجاره رهن'
        verbose_name_plural = 'اجاره رهن'


class requester(models.Model):
    REQUEST_CHOICES = (
        ('1','خرید خانه'),
        ('2','اجاره خانه'),
        ('3','خرید زمین'), )
    req         = models.CharField(choices=REQUEST_CHOICES,verbose_name='نیاز : ', max_length=20)
    region      = models.CharField( choices=REGION_CHOICES,max_length=100,verbose_name='منطقه', default='کویی بهداری')
    amount      = models.CharField(max_length=100,verbose_name='مبلغ دارایی',null=True,blank=True)
    reant       = models.CharField(max_length=100, verbose_name='میزان اجاره',null=True,blank=True)
    leas        = models.CharField(max_length=100, verbose_name='میزان رهن',null=True,blank=True)
    descripton  = models.TextField(verbose_name='توضیحات',null=True,blank=True)
    Client      = models.ForeignKey(client,verbose_name='مشتری',on_delete=models.DO_NOTHING,null=True,blank=True)
    floor       = models.CharField(max_length=3,verbose_name='تعداد طبقه',null=True,blank=True)
    rooms       = models.CharField(max_length=3,verbose_name='تعداد اتاق',null=True,blank=True)
    parking     = models.BooleanField(default=False,verbose_name='پارکینگ دارد : ')
    def __str__(self):
        return self.req
    class Meta():
        app_label           = 'app'
        verbose_name        = 'خواهان'
        verbose_name_plural = 'خواهان'