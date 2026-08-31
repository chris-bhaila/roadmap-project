from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def login_view(request):
    return render(request, 'accounts/login.html', {'initial_tab': 'login'})


def register_view(request):
    return render(request, 'accounts/login.html', {'initial_tab': 'register'})


def logout_view(request):
    return render(request, 'placeholder.html', {'page_title': 'Logout'})


@login_required
def dashboard(request):
    """LOGIN_REDIRECT_URL target: routes each role to its own home."""
    if request.user.is_admin:
        return redirect('admin_panel:dashboard')
    return redirect('roadmap:results')
