from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token # <-- NEW
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', include('home.urls')),
    path('', include('staffs.urls')),
    path('', include('profiles.urls')),
    path('', include('clients.urls')),
    path('', include('company.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_datta.urls')),
    path('', include('django_dyn_dt.urls')), # <-- NEW: Dynamic_DT Routing   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append( path("api/"      , include("api.urls"))    )
    urlpatterns.append( path("login/jwt/", view=obtain_auth_token) )
   
except:
    pass
