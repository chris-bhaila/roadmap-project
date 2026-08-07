from django.shortcuts import render


def roadmap_overview(request):
    return render(request, 'placeholder.html', {'page_title': 'Learning Roadmap'})


def skill_gap(request):
    return render(request, 'placeholder.html', {'page_title': 'Skill Gap Analysis'})


def recommended_projects(request):
    return render(request, 'placeholder.html', {'page_title': 'Recommended Projects'})


def internships(request):
    return render(request, 'placeholder.html', {'page_title': 'Internship Recommendations'})
