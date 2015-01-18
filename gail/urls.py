from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gail.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # adding my nutrients stuff
    url(r'^nutrients/', include('nutrients.urls')),
)

urlpatterns += patterns('',
 (r'^static/(.*)$', 'django.views.static.serve', 
     {'document_root': settings.STATIC_ROOT}),
)

from .views import HomePageView
#from gail import HomePageView

url('^$', HomePageView.as_view(), name='home'), 
