
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Component
from .forms import ComponentForm


class ComponentListView(ListView):
    model = Component
    template_name = 'components/list.html'
    context_object_name = 'components'

    def get_queryset(self):
        queryset = super().get_queryset()
        order = self.request.GET.get('order')

        if order in ['price', '-price']:
            queryset = queryset.order_by(order)

        return queryset

class ComponentDetailView(DetailView):
    model = Component
    template_name = 'components/detail.html'
    context_object_name = 'component'

class ComponentCreateView(CreateView):
    model = Component
    form_class = ComponentForm
    template_name = 'components/form.html'
    success_url = reverse_lazy('components:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Component'
        return context

class ComponentUpdateView(UpdateView):
    model = Component
    form_class = ComponentForm
    template_name = 'components/form.html'
    success_url = reverse_lazy('components:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Component'
        return context

def component_delete(request, pk):
    component = get_object_or_404(Component, pk=pk)

    if request.method == 'POST':
        component.delete()
        return redirect('components:list')

    return render(
        request,
        'components/confirm_delete.html',
        {'component': component}
    )