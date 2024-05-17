
from django.contrib import admin
from django.urls import path
from bombapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.liverpool),
    path('mat/', views.mat),
    path('muscle/', views.muscle),
]
