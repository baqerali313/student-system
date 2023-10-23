from django.contrib import admin
from django.urls import path

from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<int:id>/', views.update, name='update')
]
