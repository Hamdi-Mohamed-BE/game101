"""app URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include


from core.swagger import app_swagger_view

admin.site.site_header = 'Games 101'
admin.site.index_title = 'Games 101'
admin.site.site_title = 'Games 101'
admin.site.site_url = ''

games_api_urlpatterns = path('api/games' , include('games.urls'))


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        "docs/$",
        app_swagger_view(
            urls_patterns=(
                # Add documented patterns here
                games_api_urlpatterns,
            ),
            title="Games 101 API",
        )
    ),
    games_api_urlpatterns,
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
