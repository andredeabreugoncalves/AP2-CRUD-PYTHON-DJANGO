"""project URL Configuration

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
from django.contrib import admin
from django.urls import path
from app.views import home, pagcliente, pagvenda, pagvendacliente,  form, formcliente, create, createcliente, view, viewcliente, edit, editcliente, update, updatecliente, delete, deletecliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pagcliente/', pagcliente, name='pagcliente'),
    path('pagvenda/', pagvenda, name='pagvenda'),
    path('pagvendacliente/', pagvendacliente, name='pagvendacliente'),

    path('form/', form, name='form'),
    path('formcliente/', formcliente, name='formcliente'),

    path('create/', create, name='create'),
    path('createcliente/', createcliente, name='createcliente'),

    path('view/<int:pk>/', view, name='view'),
    path('viewcliente/<int:pk>/', viewcliente, name='viewcliente'),

    path('edit/<int:pk>/', edit, name='edit'),
    path('editcliente/<int:pk>/', editcliente, name='editcliente'),

    path('update/<int:pk>/', update, name='update'),
    path('updatecliente/<int:pk>/', updatecliente, name='updatecliente'),

    path('delete/<int:pk>/', delete, name='delete'),
    path('deletecliente/<int:pk>/', deletecliente, name='deletecliente'),

]