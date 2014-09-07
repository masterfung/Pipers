from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'person.views.home', name='home'),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^logout/$', 'person.views.logout', name='logout'),

    url(r'^login/$', 'person.views.login', name='login'),

    url(r'^profile/$', 'person.views.profile', name='profile'),

)
