from django.conf.urls import include, url
from django.contrib import admin
from beeApp import views
from bee import urls_tag

urlpatterns = [
    # Examples:
    # url(r'^$', 'bee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tag/', include(urls_tag)),
    url(r'^admin/', include(admin.site.urls)),
]
