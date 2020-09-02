
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include,path, re_path
from globernaut.views import Login
urlpatterns = [
    path(r'', Login.as_view()),
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #path('admin/', admin.site.urls),
    path('globernaut/', include('globernaut.urls')),
    path('globernautup/', include('globernautup.urls')),
    #re_path(r'^$', include('webapp.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)