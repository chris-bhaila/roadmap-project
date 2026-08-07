from django.shortcuts import render


def login_view(request):
    return render(request, 'placeholder.html', {'page_title': 'Login'})


def register_view(request):
    return render(request, 'placeholder.html', {'page_title': 'Register'})


def logout_view(request):
    return render(request, 'placeholder.html', {'page_title': 'Logout'})


def dashboard(request):
    return render(request, 'placeholder.html', {'page_title': 'Dashboard'})
