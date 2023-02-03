"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from app import views
from adds import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', views.logout_view, name="logout"),
    path('panel/', include('adds.urls')),
    path('delete/<int:ID>',v.Delete_zamin,name='delete-zamin'),
    
    path('',views.index,name="home"),
    path('panel',views.Panel,name="panel"),
    path('zamins',views.zamins,name="zamins"),
    path('builds',views.builds,name="builds"),
    path('leases',views.lease_view,name="lease"),
    path('add-zamin',views.add_zamin,name="addZamin"),
    path('add-build',views.add_build,name="addBuild"),
]
