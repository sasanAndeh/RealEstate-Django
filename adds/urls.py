
from django.urls import path 
from adds import views

urlpatterns = [

    path('addz',views.addz,name="addz"),
    path('add-build',views.add_build,name="addBuild"),
]
