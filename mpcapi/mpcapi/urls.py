from django.conf.urls import url, patterns, include
from django.contrib import admin
from api import urls as api_urls

admin.autodiscover()

urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', admin.site.urls),
]

