"""jfkwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from main.views import *
from board.views import OldYearPage, memberTemplate



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),

    path('hakkimizda', about_view),
    path('hakkimizda/biz_kimiz', about_view),
    path('hakkimizda/misyon_vizyon', about_view),
    path('hakkimizda/kurul', memberTemplate.as_view(), name="kurul"),

    path('etkinliklerimiz', etkinlik_list_view),
    path('etkinliklerimiz/<int:id>', etkinlik_detay_view),

    path('gecmis/<int:year>/', OldYearPage.as_view(), name='oldyear'),

    path('iletisim', iletisim_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
