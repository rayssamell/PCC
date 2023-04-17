from django.urls import path

from .views import ForumListView, ForumDetailView

app_name = 'recipe'

urlpatterns = [
    path('', ForumListView.as_view(), name='listar'),
    path('detail/<slug:recipe_slug>/', ForumDetailView.as_view(), name='detail'), # noqa E501
    path('category/<slug:category_slug>/', ForumListView.as_view(), name='tema'), # noqa E501
]
