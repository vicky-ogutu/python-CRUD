"""CRUD_operation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from xml.etree.ElementInclude import include
from django import urls
from django.contrib import admin
from django.urls import path, include
from .import views
from CRUD_operation.router import router

urlpatterns =[

    path('admin/', admin.site.urls),
    path('vicky/', views.showClients, name="showClients"),
    path('instat/', views.insertData, name="insertData"),
    path('editData/<int:client_id>', views.editData, name="editData"),
    path('Update/<int:client_id>', views.updateClt, name="updateClt"),
    path('Delete/<int:client_id>', views.delClt, name="delClt"),
    path('api/', include(router.urls)),
   
]
