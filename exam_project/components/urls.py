from django.urls import path
from .views import ComponentListView,ComponentDetailView,ComponentCreateView,ComponentUpdateView,component_delete
app_name = 'components'
urlpatterns = [
    path('', ComponentListView.as_view(), name='list'),
    path('create/', ComponentCreateView.as_view(), name='create'),
    path('<int:pk>/', ComponentDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ComponentUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', component_delete, name='delete'),
]