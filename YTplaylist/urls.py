from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'YTplaylist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^addVideo/', include('addVideo.urls')),
    url(r'^searchVideo/', include('searchVideo.urls')),
]
