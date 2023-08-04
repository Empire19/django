"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bankapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login,name=''),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('emp/', views.emp),
    path('bnk/', views.bnk),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('change/<int:id>', views.change),
    path('modify/<int:id>', views.modify),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('destroy/<int:id>', views.destroy),
]
