from django.conf.urls import patterns, include, url
from nutrients.views import StartView

# defines http://localhost:8000/nutrients/stuff/ with the registration in gail/urls.py
urlpatterns = patterns('',
    url(r'^stuff/$', StartView.as_view(), name='start-view'),
)

