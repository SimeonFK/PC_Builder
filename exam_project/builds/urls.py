from django.urls import path
from builds.views import BuildListView, BuildCreateView, BuildDetailView, BuildUpdateView, build_delete

app_name = 'builds'
urlpatterns = [
    path('', BuildListView.as_view(), name='list'),
    path('create/', BuildCreateView.as_view(), name='create'),
    path('<int:pk>/', BuildDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', BuildUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', build_delete, name='delete'),
]