from django.shortcuts import render


def profile_detail(request):
    return render(request, 'placeholder.html', {'page_title': 'My Profile'})


def profile_edit(request):
    return render(request, 'placeholder.html', {'page_title': 'Edit Profile'})
