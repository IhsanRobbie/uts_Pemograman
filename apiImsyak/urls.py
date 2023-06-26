from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiApp.urls')),
]

handler404 ='apiApp.views.error_404'
