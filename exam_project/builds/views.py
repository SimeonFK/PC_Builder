from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import PCBuild
from .forms import PCBuildForm

class BuildListView(ListView):
    model = PCBuild
    template_name = 'builds/list.html'
    context_object_name = 'builds'

class BuildDetailView(DetailView):
    model = PCBuild
    template_name = 'builds/detail.html'
    context_object_name = 'build'

class BuildCreateView(CreateView):
    model = PCBuild
    form_class = PCBuildForm
    template_name = 'builds/form.html'
    success_url = reverse_lazy('builds:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create PC Build'
        return context

class BuildUpdateView(UpdateView):
    model = PCBuild
    form_class = PCBuildForm
    template_name = 'builds/form.html'
    success_url = reverse_lazy('builds:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit PC Build'
        return context

def build_delete(request, pk):
    build = get_object_or_404(PCBuild, pk=pk)

    if request.method == 'POST':
        build.delete()
        return redirect('builds:list')

    return render(
        request,
        'builds/confirm_delete.html',
        {'build': build}
    )