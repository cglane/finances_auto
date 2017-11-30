"""finances URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import views

api_patterns = [
    url(r'^sheets_list/$', views.sheets_list, name='sheets_list'),
    url(r'^add_data', views.UpdateData.as_view()),
    url(r'^authorize/$', views.authorize, name='authorize'),
    url(r'^read_csv', views.ReadCSV.as_view())
]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_patterns, namespace='rest_framework')),
    # url(r'^(?!(?:api|admin)/)', views.MainView.as_view()),
]
