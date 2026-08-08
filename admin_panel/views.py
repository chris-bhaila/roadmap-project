from functools import wraps

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


def staff_required(view_func):
    """staff_member_required, but redirecting to the site's own login page
    instead of Django admin's."""
    return wraps(view_func)(staff_member_required(view_func, login_url=settings.LOGIN_URL))


@staff_required
def dashboard(request):
    return render(request, 'placeholder.html', {'page_title': 'Admin Panel'})
