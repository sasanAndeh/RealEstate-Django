# Generated by Django 2.2.5 on 2022-12-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='gz',
            field=models.CharField(choices=[('1', 'خیابان'), ('2', 'کوچه')], max_length=20, verbose_name='زمین - باغ'),
        ),
        migrations.AlterField(
            model_name='garden',
            name='ls',
            field=models.CharField(choices=[('1', 'خیابان'), ('2', 'کوچه')], max_length=20, verbose_name='اجاره - خرید'),
        ),
        migrations.AlterField(
            model_name='informations',
            name='sg',
            field=models.CharField(blank=True, choices=[('1', 'سند'), ('2', 'قرار داد')], max_length=20, verbose_name='س - ق'),
        ),
        migrations.AlterField(
            model_name='informations',
            name='sk',
            field=models.CharField(blank=True, choices=[('1', 'خیابان'), ('2', 'کوچه')], max_length=20, verbose_name='خ - ک'),
        ),
    ]