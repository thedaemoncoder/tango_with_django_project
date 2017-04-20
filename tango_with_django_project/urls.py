from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),  # added this to see rango's urls
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
                            )

#print urlpatterns
# At this point,
#  urlpatterns = [<RegexURLResolver <RegexURLPattern list> (admin:admin) ^admin/>,
#                 <RegexURLResolver <module 'rango.urls' from 'e:\code\tango_with_django_project\rango\urls.py'> (None:None) ^rango/>,
#                  <RegexURLResolver <module 'rango.urls' from 'e:\code\tango_with_django_project\rango\urls.py'> (None:None) ^rango/about/>,
#                  <RegexURLPattern None ^media/(?P<path>.*)>]
