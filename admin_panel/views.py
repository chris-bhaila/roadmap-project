import itertools
import json
from functools import wraps

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

_new_path_ids = itertools.count(1000)


def staff_required(view_func):
    """staff_member_required, but redirecting to the site's own login page
    instead of Django admin's."""
    return wraps(view_func)(staff_member_required(view_func, login_url=settings.LOGIN_URL))


@staff_required
def dashboard(request):
    return render(request, 'placeholder.html', {'page_title': 'Admin Panel'})


TAXONOMY_PATHS = [
    {
        'id': 1,
        'name': 'Full-Stack Developer',
        'category': 'Web & Application',
        'status': 'active',
        'skills': ['React', 'Node.js', 'PostgreSQL', 'Docker', 'REST APIs', 'Git'],
    },
    {
        'id': 2,
        'name': 'Data Scientist',
        'category': 'Analytics & AI',
        'status': 'active',
        'skills': ['Python', 'SQL', 'Machine Learning'],
    },
    {
        'id': 3,
        'name': 'Backend Developer',
        'category': 'Web & Application',
        'status': 'active',
        'skills': ['Python', 'SQL', 'System Design', 'Docker', 'Testing & CI/CD'],
    },
    {
        'id': 4,
        'name': 'DevOps Engineer',
        'category': 'Infrastructure',
        'status': 'draft',
        'skills': ['Docker', 'Kubernetes', 'CI/CD', 'AWS'],
    },
]


@staff_required
def taxonomy(request):
    return render(request, 'admin_panel/taxonomy.html', {
        'page_title': 'Path Management',
        'paths': TAXONOMY_PATHS,
    })


@staff_required
@require_POST
def taxonomy_save(request):
    path_id = request.POST.get('id')
    name = request.POST.get('name', '').strip()
    category = request.POST.get('category', '').strip()
    status = request.POST.get('status', 'active')
    skills = [s.strip() for s in request.POST.get('skills', '').split(',') if s.strip()]

    if not name:
        return JsonResponse({'error': 'Pathway name is required.'}, status=400)

    return JsonResponse({
        'id': path_id or next(_new_path_ids),
        'name': name,
        'category': category,
        'status': status,
        'skills': skills,
    })


LEARNING_RESOURCES = [
    {
        'id': 1,
        'name': 'React Basics',
        'description': 'Introduction to functional components and hooks.',
        'category': 'Frontend',
        'provider': 'Coursera',
        'skills': ['React', 'JSX', 'Hooks'],
    },
    {
        'id': 2,
        'name': 'AWS Cloud Practitioner',
        'description': 'Foundational cloud concepts and AWS services overview.',
        'category': 'Cloud',
        'provider': 'AWS Training',
        'skills': ['AWS', 'Cloud Architecture'],
    },
    {
        'id': 3,
        'name': 'Advanced SQL Optimization',
        'description': 'Techniques for improving database query performance.',
        'category': 'Database',
        'provider': 'Udemy',
        'skills': ['SQL', 'Query Optimization'],
    },
    {
        'id': 4,
        'name': 'Node.js API Design',
        'description': 'Building REST APIs with Express and middleware patterns.',
        'category': 'Backend',
        'provider': 'Udemy',
        'skills': ['Node.js', 'REST APIs', 'Express'],
    },
    {
        'id': 5,
        'name': 'Python for Data Analysis',
        'description': 'Pandas, NumPy, and data wrangling fundamentals.',
        'category': 'Data Science',
        'provider': 'Coursera',
        'skills': ['Python', 'Pandas', 'NumPy'],
    },
    {
        'id': 6,
        'name': 'Docker & Containers Deep Dive',
        'description': 'Building, shipping, and running containerized applications.',
        'category': 'DevOps',
        'provider': 'Pluralsight',
        'skills': ['Docker', 'Containers'],
    },
    {
        'id': 7,
        'name': 'Machine Learning Foundations',
        'description': 'Core supervised and unsupervised learning algorithms.',
        'category': 'Data Science',
        'provider': 'edX',
        'skills': ['Machine Learning', 'Python'],
    },
    {
        'id': 8,
        'name': 'System Design Interview Prep',
        'description': 'Scalability, load balancing, and distributed systems basics.',
        'category': 'Backend',
        'provider': 'Educative',
        'skills': ['System Design'],
    },
    {
        'id': 9,
        'name': 'Kubernetes for Developers',
        'description': 'Deploying and scaling applications with Kubernetes.',
        'category': 'DevOps',
        'provider': 'Pluralsight',
        'skills': ['Kubernetes', 'Docker', 'CI/CD'],
    },
    {
        'id': 10,
        'name': 'Git & Version Control',
        'description': 'Branching strategies, rebasing, and collaborative workflows.',
        'category': 'Backend',
        'provider': 'Udemy',
        'skills': ['Git'],
    },
    {
        'id': 11,
        'name': 'CSS Grid & Flexbox Mastery',
        'description': 'Modern layout techniques for responsive interfaces.',
        'category': 'Frontend',
        'provider': 'Frontend Masters',
        'skills': ['CSS', 'Responsive Design'],
    },
    {
        'id': 12,
        'name': 'Testing & CI/CD Pipelines',
        'description': 'Automated testing strategies and continuous deployment.',
        'category': 'DevOps',
        'provider': 'edX',
        'skills': ['Testing & CI/CD', 'Git'],
    },
]

RESOURCE_CATEGORIES = ['Frontend', 'Backend', 'Cloud', 'Data Science', 'Database', 'DevOps']


@staff_required
def resources(request):
    return render(request, 'admin_panel/resources.html', {
        'page_title': 'Resource Library',
        'resources': LEARNING_RESOURCES,
        'categories': RESOURCE_CATEGORIES,
    })


ANALYTICS_SUMMARY = {
    'total_students': 1248,
    'most_common_path': 'Full-Stack Developer',
    'most_common_path_percent': 42,
    'avg_compatibility': 78,
}

# Average cohort readiness score (%) by month, for each chart range toggle.
READINESS_TREND = {
    '3m': [
        {'label': 'Dec', 'value': 58},
        {'label': 'Jan', 'value': 66},
        {'label': 'Feb', 'value': 78},
    ],
    '6m': [
        {'label': 'Sep', 'value': 35},
        {'label': 'Oct', 'value': 44},
        {'label': 'Nov', 'value': 51},
        {'label': 'Dec', 'value': 58},
        {'label': 'Jan', 'value': 66},
        {'label': 'Feb', 'value': 78},
    ],
    '1y': [
        {'label': 'Mar', 'value': 18},
        {'label': 'Apr', 'value': 22},
        {'label': 'May', 'value': 27},
        {'label': 'Jun', 'value': 30},
        {'label': 'Jul', 'value': 33},
        {'label': 'Aug', 'value': 38},
        {'label': 'Sep', 'value': 35},
        {'label': 'Oct', 'value': 44},
        {'label': 'Nov', 'value': 51},
        {'label': 'Dec', 'value': 58},
        {'label': 'Jan', 'value': 66},
        {'label': 'Feb', 'value': 78},
    ],
}


@staff_required
def analytics(request):
    return render(request, 'admin_panel/analytics.html', {
        'page_title': 'Student Analytics',
        'summary': ANALYTICS_SUMMARY,
        'trend_json': json.dumps(READINESS_TREND),
        'trend_default': READINESS_TREND['6m'],
    })
