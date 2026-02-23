from django.shortcuts import render

def home_view(request):
    return render(request, 'common/home.html')

def about_view(request):
    return render(request, 'common/about.html')

def custom_404_view(request, exception):
    return render(request, 'common/404.html', status=404)
