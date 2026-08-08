from django.shortcuts import render


def profile_detail(request):
    return render(request, 'placeholder.html', {'page_title': 'My Profile'})


def profile_edit(request):
    return render(request, 'placeholder.html', {'page_title': 'Edit Profile'})


def profile_setup(request):
    context = {
        'majors': [
            ('cs', 'Computer Science'),
            ('se', 'Software Engineering'),
            ('it', 'Information Technology'),
            ('ds', 'Data Science'),
            ('other', 'Other'),
        ],
        'grad_years': ['2024', '2025', '2026', '2027+'],
        'suggested_skills': ['Python', 'SQL', 'React'],
        'target_roles': [
            'Backend Developer', 'Frontend Developer', 'Data Analyst',
            'DevOps Engineer', 'Mobile Developer', 'ML Engineer',
        ],
        'internship_types': ['Remote', 'Hybrid', 'On-site'],
        'time_commitments': ['< 5 hrs/wk', '5-10 hrs/wk', '10+ hrs/wk'],
    }
    return render(request, 'profiles/setup.html', context)


def profile_upload(request):
    context = {
        'accepted_formats': ['PDF', 'DOCX'],
        'accepted_extensions': '.pdf,.doc,.docx',
        'max_file_size_mb': 5,
    }
    return render(request, 'profiles/upload.html', context)


def profile_skills(request):
    context = {
        'initial_skills': ['Java', 'Python', 'React'],
        'initial_projects': [
            {
                'name': 'Internship Readiness Portfolio',
                'url': 'https://github.com/student/readiness-portfolio',
                'description': 'Built a dashboard for tracking student readiness using React and Tailwind CSS.',
            },
        ],
        'initial_certs': [
            {'name': 'AWS Certified Cloud Practitioner', 'org': 'Amazon Web Services'},
        ],
    }
    return render(request, 'profiles/skills_form.html', context)
