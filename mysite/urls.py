from django.conf.urls import include, url
from django.contrib import admin
from.import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('blog.urls')),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^admin/', include(admin.site.urls)),
]
