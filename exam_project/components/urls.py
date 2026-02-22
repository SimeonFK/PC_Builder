from django.urls import path

from .views import ComponentListView,ComponentDetailView,ComponentCreateView,ComponentUpdateView,component_delete

app_name = 'components'
urlpatterns = [
    path('', ComponentListView.as_view(), name='component-list'),
    path('create/', ComponentCreateView.as_view(), name='component-create'),
    path('<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('<int:pk>/edit/', ComponentUpdateView.as_view(), name='component-edit'),
    path('<int:pk>/delete/', component_delete, name='component-delete'),
]