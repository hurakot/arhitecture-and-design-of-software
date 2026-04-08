"""
URL configuration for lab1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

#urls.py - это главный файл маршрутов в проекте. 
#В нём прописано, какой URL вызывает какой код.

from django.contrib import admin
from django.urls import path

from rest_framework import routers

from mainapp.views import *

#urlpatterns - это список маршрутов (URL-путей)
#'admin/' - URL-путь, admin.site.urls - вызываемый обработчик маршрута

urlpatterns = [
    path('admin/', admin.site.urls),  #Админская панель
    path('create/', create, name="create"), #Путь к созданию страницы 
    path('', watch_all, name="watch_all"), #Путь к просмотру всех страниц
    path('watch_one/<int:id>/', watch_one, name="watch_one"), #Путь к просмотру одной страницы
    path('change/<int:id>/', change, name="change"), #Путь к изменению страницы
    path('delete/<int:id>/', delete, name="delete"), #Путь к удалению страницы
    path('json/', nerf_json), #Использование сериализатора JSON

    # path('airplane', AiplaneViewSet.as_view({'post': 'create'})),  
   
]
