from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('forum/', include('forum.urls')),
    path('', include('atuacao_profissional.urls')),
    path('formacao/', include('formacao.urls')),
    path('trabalhosAcademicos/', include('trabalhos_academicos.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
