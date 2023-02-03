from django.contrib import admin
from app.models import *


# Register your models here.
admin.site.site_header = 'پنل مدیریتی'
admin.site.site_title  =  "مشاور املاک آنده"
admin.site.index_title  =  "مدیریت"
# Register your models here.
@admin.register(client)
class client_info(admin.ModelAdmin):
	def has_add_permission(self, request, obj=None):
		return True
	list_display = ('id','number','f_name','l_name')



@admin.register(zamin)
class zamin_info(admin.ModelAdmin):
	list_display 	= ('id','number','client','region','sk','sg','metr','price')
	search_fields 	= ('number', 'region','client')
	list_filter   	= ('region','client')
	choices_gender  =('region')
	advanced_filter_fields =('region','client')
	def has_change_permission(self, request, obj=None):
        
		return True
	def has_add_permission(self, request):
		return True

@admin.register(build)
class build_info(admin.ModelAdmin):
	def has_add_permission(self, request, obj=None):
		return True
	list_display = ('id','number','client','region','sk','sg','metr','price')
@admin.register(Garden)
class Garden_info(admin.ModelAdmin):
	def has_add_permission(self, request, obj=None):
		return True
	list_display = ('id','number','client','hektar_z','ls','gz','price')

@admin.register(lease)
class lease_info(admin.ModelAdmin):
	def has_add_permission(self, request, obj=None):
		return True
	list_display = ('id','number','client','region','hm')
@admin.register(requester)
class requester_info(admin.ModelAdmin):
	def has_add_permission(self, request, obj=None):
		return True
	list_display = ('id','req')

