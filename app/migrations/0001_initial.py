# Generated by Django 2.2.5 on 2022-12-23 17:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='نام')),
                ('l_name', models.CharField(max_length=50, null=True, verbose_name='نام خانوداگی')),
                ('number', models.CharField(max_length=13, verbose_name='شماره همراه')),
            ],
            options={
                'verbose_name': 'مالک',
                'verbose_name_plural': 'مالکین',
            },
        ),
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='قطعه')),
                ('metr', models.FloatField(blank=True, null=True, verbose_name='متراژ زمین')),
                ('area', models.IntegerField(blank=True, null=True, verbose_name='دهنه')),
                ('region', models.CharField(choices=[('شهرک کارمندان', 'شهرک کارمندان'), ('کویی بهداری', 'کویی بهداری'), ('سپاه نور', 'سپاه پیام نور'), ('بهارستان', 'بهارستان'), ('قلقلاغ', 'قلقلاغ'), ('شهرک معراج', 'شهرک معراج'), ('فاز 3 پیام', 'فاز 3 پیام'), ('شهرک خانی', 'شهرک خانی'), ('شهرک نور', 'شهرک نور'), ('فاز 2 پیام', 'فاز دو پیام'), ('فرمانداری', 'فرمانداری'), ('گلستان', 'گلستان'), ('سپاه هنرستان قدیم', 'سپاه هنرستان قدیم'), ('کوی دادگستری', 'کوی دادگستری'), ('نهضت', 'نهضت'), ('بهزیستی', 'بهزیستی'), ('کارکنان شهرداری', 'کارکنان شهرداری'), ('تاناکورا', 'تاناکورا'), ('گوی هه ژار', 'کوی هه ژار'), ('باغ گولان', 'باغ گولان'), ('بسیج', 'بسیج'), ('تپه هما', 'تپه هما'), ('شهرک فجر', 'شهرک فجر'), ('بهار 1', 'بهار1'), ('بهار 2', 'بهار2'), ('بنیاد شهید فاز 1', 'بنیاد شیهد فاز1'), ('بنیاد شهید فاز 2', 'بنیاد شهید فاز2'), ('بنیاد شهید فاز 3', 'بنیاد شهید فاز3'), ('شهرک پیشوا', 'شهرک پیشوا'), ('شهرک خیام', 'شهرک خیام'), ('خبازان', 'خبازان'), ('کارکنان شهرداری', 'کارکنان شهردای'), ('صداوسیما', 'صداوسیما'), ('کوی فرهنیگان', 'کوی فرهنگیان'), ('مکریان', 'مکریان'), ('زمین شهری', 'زمین شهری'), ('کوی استادان', 'کوی استادان'), ('شهرک پویا', 'شهرک پویا'), ('شهرک نیاوران', 'شهرک نیاوران'), ('پتو بافی تارا', 'پتوبافی تارا'), ('جانبازان', 'جانبازان'), ('آزادگان', 'آزادگان'), ('صبح مکریان', 'صبح مکریان'), ('نیرو انتظامی', 'نیرو انتظامی'), ('شهرک صنفی', 'شهرک صنفی'), ('شهرک صبا', 'شهرک صبا'), ('شهرک صنعتی', 'شهرک صنعتی'), ('روستایی', ' روستایی')], default='کویی بهداری', max_length=100, verbose_name='منطقه')),
                ('tawn', models.CharField(blank=True, max_length=100, null=True, verbose_name='شهر')),
                ('faz', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=20, verbose_name='فاز')),
                ('napsh', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, verbose_name='نپش')),
                ('sk', models.CharField(blank=True, choices=[('خیابان', 'خیابان'), ('کوچه', 'کوچه')], max_length=20, verbose_name='خ - ک')),
                ('sg', models.CharField(blank=True, choices=[('سند دار', 'سند'), ('قرارداد', 'قرار داد')], max_length=20, verbose_name='س - ق')),
                ('price', models.CharField(blank=True, max_length=100, null=True, verbose_name='قیمت')),
                ('priced', models.BooleanField(default=False, verbose_name='وضعت فروش : ')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('descripton', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.client', verbose_name='مشتری')),
            ],
        ),
        migrations.CreateModel(
            name='build',
            fields=[
                ('informations_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Informations')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='تعداد طبقه')),
                ('rooms', models.IntegerField(blank=True, null=True, verbose_name='تعداد اتاق')),
                ('parking', models.BooleanField(default=False, verbose_name='پارکینگ دارد : ')),
                ('metr_b', models.FloatField(blank=True, null=True, verbose_name='زیربنا ساختمان')),
                ('finished', models.BooleanField(default=False, verbose_name='پایانه کار : ')),
            ],
            options={
                'verbose_name': 'ساختمان',
                'verbose_name_plural': 'ساختمان ها',
            },
            bases=('app.informations',),
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('informations_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Informations')),
                ('hektar_z', models.FloatField(blank=True, null=True, verbose_name=' هکتار زمین')),
                ('inch', models.IntegerField(blank=True, null=True, verbose_name='اینج آب')),
                ('ls', models.CharField(choices=[('خیابان', 'خیابان'), ('کوچه', 'کوچه')], max_length=20, verbose_name='اجاره - خرید')),
                ('gz', models.CharField(choices=[('خیابان', 'خیابان'), ('کوچه', 'کوچه')], max_length=20, verbose_name='زمین - باغ')),
                ('chaeh', models.BooleanField(default=False, verbose_name='چاه دارد؟')),
            ],
            options={
                'verbose_name': 'باغ',
                'verbose_name_plural': 'باغ ها',
            },
            bases=('app.informations',),
        ),
        migrations.CreateModel(
            name='lease',
            fields=[
                ('informations_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Informations')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='تعداد طبقه')),
                ('rooms', models.IntegerField(blank=True, null=True, verbose_name='تعداد اتاق')),
                ('parking', models.BooleanField(default=False, verbose_name='پارکینگ دارد : ')),
                ('hm', models.CharField(choices=[('مغازه', 'مغازه'), ('خانه', 'خانه')], max_length=20, verbose_name='خ - م')),
                ('leas', models.BigIntegerField(blank=True, null=True, verbose_name='اجاره')),
                ('mortgae', models.BigIntegerField(blank=True, null=True, verbose_name='رهن')),
            ],
            options={
                'verbose_name': 'اجاره رهن',
                'verbose_name_plural': 'اجاره رهن',
            },
            bases=('app.informations',),
        ),
        migrations.CreateModel(
            name='zamin',
            fields=[
                ('informations_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Informations')),
            ],
            options={
                'verbose_name': 'زمین',
                'verbose_name_plural': 'زمین ها',
            },
            bases=('app.informations',),
        ),
        migrations.CreateModel(
            name='requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req', models.CharField(choices=[('1', 'خرید خانه'), ('2', 'اجاره خانه'), ('3', 'خرید زمین')], max_length=20, verbose_name='نیاز : ')),
                ('region', models.CharField(choices=[('شهرک کارمندان', 'شهرک کارمندان'), ('کویی بهداری', 'کویی بهداری'), ('سپاه نور', 'سپاه پیام نور'), ('بهارستان', 'بهارستان'), ('قلقلاغ', 'قلقلاغ'), ('شهرک معراج', 'شهرک معراج'), ('فاز 3 پیام', 'فاز 3 پیام'), ('شهرک خانی', 'شهرک خانی'), ('شهرک نور', 'شهرک نور'), ('فاز 2 پیام', 'فاز دو پیام'), ('فرمانداری', 'فرمانداری'), ('گلستان', 'گلستان'), ('سپاه هنرستان قدیم', 'سپاه هنرستان قدیم'), ('کوی دادگستری', 'کوی دادگستری'), ('نهضت', 'نهضت'), ('بهزیستی', 'بهزیستی'), ('کارکنان شهرداری', 'کارکنان شهرداری'), ('تاناکورا', 'تاناکورا'), ('گوی هه ژار', 'کوی هه ژار'), ('باغ گولان', 'باغ گولان'), ('بسیج', 'بسیج'), ('تپه هما', 'تپه هما'), ('شهرک فجر', 'شهرک فجر'), ('بهار 1', 'بهار1'), ('بهار 2', 'بهار2'), ('بنیاد شهید فاز 1', 'بنیاد شیهد فاز1'), ('بنیاد شهید فاز 2', 'بنیاد شهید فاز2'), ('بنیاد شهید فاز 3', 'بنیاد شهید فاز3'), ('شهرک پیشوا', 'شهرک پیشوا'), ('شهرک خیام', 'شهرک خیام'), ('خبازان', 'خبازان'), ('کارکنان شهرداری', 'کارکنان شهردای'), ('صداوسیما', 'صداوسیما'), ('کوی فرهنیگان', 'کوی فرهنگیان'), ('مکریان', 'مکریان'), ('زمین شهری', 'زمین شهری'), ('کوی استادان', 'کوی استادان'), ('شهرک پویا', 'شهرک پویا'), ('شهرک نیاوران', 'شهرک نیاوران'), ('پتو بافی تارا', 'پتوبافی تارا'), ('جانبازان', 'جانبازان'), ('آزادگان', 'آزادگان'), ('صبح مکریان', 'صبح مکریان'), ('نیرو انتظامی', 'نیرو انتظامی'), ('شهرک صنفی', 'شهرک صنفی'), ('شهرک صبا', 'شهرک صبا'), ('شهرک صنعتی', 'شهرک صنعتی'), ('روستایی', ' روستایی')], default='کویی بهداری', max_length=100, verbose_name='منطقه')),
                ('amount', models.CharField(blank=True, max_length=100, null=True, verbose_name='مبلغ دارایی')),
                ('reant', models.CharField(blank=True, max_length=100, null=True, verbose_name='میزان اجاره')),
                ('leas', models.CharField(blank=True, max_length=100, null=True, verbose_name='میزان رهن')),
                ('descripton', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='تعداد طبقه')),
                ('rooms', models.IntegerField(blank=True, null=True, verbose_name='تعداد اتاق')),
                ('parking', models.BooleanField(default=False, verbose_name='پارکینگ دارد : ')),
                ('Client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.client', verbose_name='مشتری')),
            ],
            options={
                'verbose_name': 'خواهان',
                'verbose_name_plural': 'خواهان',
            },
        ),
    ]
