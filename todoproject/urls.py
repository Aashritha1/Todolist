"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf.urls import url
import django.contrib.auth.urls
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url


from todoapp import urls as online_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^online/',include(online_urls.urlpatterns,namespace='todoapp')),
    url(r'^auth/',include(django.contrib.auth.urls))
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns