from django.shortcuts import render


def progress_overview(request):
    return render(request, 'placeholder.html', {'page_title': 'Progress Tracking'})


def history(request):
    return render(request, 'placeholder.html', {'page_title': 'Re-evaluation History'})
