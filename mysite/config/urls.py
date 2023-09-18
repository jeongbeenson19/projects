from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'), # / 페이지에 해당하는 urlpatterns
]
