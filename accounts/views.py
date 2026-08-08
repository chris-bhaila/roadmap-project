from django.shortcuts import render


def login_view(request):
    return render(request, 'accounts/login.html', {'initial_tab': 'login'})


def register_view(request):
    return render(request, 'accounts/login.html', {'initial_tab': 'register'})


def logout_view(request):
    return render(request, 'placeholder.html', {'page_title': 'Logout'})


def dashboard(request):
    return render(request, 'placeholder.html', {'page_title': 'Dashboard'})
