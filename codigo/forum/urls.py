from django.urls import path
from .views import home, detail, forums, criar_forum, \
                    latest_forums

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("forums/<slug>/", forums, name="forums"),
    path("criar_forum", criar_forum, name="criar_forum"),
    path("latest_forums", latest_forums, name="latest_forums"),
]
