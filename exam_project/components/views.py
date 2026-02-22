
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Component
from .forms import ComponentForm


class ComponentListView(ListView):
    model = Component
    template_name = 'components/list.html'
    context_object_name = 'components'

    def get_query(self):
        components_q = Component.objects.all()

        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        order = self.request.GET.get('order')

        if category:
            components_q = components_q.filter(category__id=category)

        if tag:
            components_q = components_q.filter(tags__id=tag)

        if order == 'price':
            components_q = components_q.order_by('price')
        elif order == '-price':
            components_q = components_q.order_by('-price')

        return components_q

class ComponentDetailView(DetailView):
    model = Component
    template_name = 'components/detail.html'
    context_object_name = 'component'

class ComponentCreateView(CreateView):
    model = Component
    form_class = ComponentForm
    template_name = 'components/form.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Component'
        return context

class ComponentUpdateView(UpdateView):
    model = Component
    form_class = ComponentForm
    template_name = 'components/form.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Component'
        return context

def component_delete(request, pk):
    component = get_object_or_404(Component, pk=pk)

    if request.method == 'POST':
        component.delete()
        return redirect('list')

    return render(request, 'components/confirm_delete.html', {
        'component': component
    })