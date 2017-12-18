
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
    url(r'^(?!(?:api|admin)/)', views.MainView.as_view()),
]
