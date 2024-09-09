from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header ="Login to Heirs Holding Registration Portal"
admin.site.site_title ="Welcome to HEIRS HOLDING Dashboard"
admin.site.index_title ="Welcome to HEIRS HOLDING Dashboard"

urlpatterns = [
    path('', views.register, name="register"),
]