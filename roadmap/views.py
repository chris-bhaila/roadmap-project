from django.shortcuts import render

# Fixed palette (kept within the existing indigo/green/amber/red system
# roles) so a given tag name always renders in the same color everywhere.
TAG_PALETTE = [
    {'bg': '#E2DFFF', 'text': '#3525CD', 'border': '#C3C0FF'},  # indigo
    {'bg': '#DFF7EA', 'text': '#006C49', 'border': '#9FE8C4'},  # green
    {'bg': '#FFE8C7', 'text': '#684000', 'border': '#FFC98A'},  # amber
    {'bg': '#FFDAD6', 'text': '#93000A', 'border': '#FFB4AB'},  # red
]


def _tag_style(name):
    color = TAG_PALETTE[sum(ord(c) for c in name) % len(TAG_PALETTE)]
    return {'name': name, **color}


def _styled_tags(names):
    return [_tag_style(name) for name in names]

TOP_MATCHES = [
    {
        'rank': 1,
        'title': 'Backend developer',
        'score': 87,
        'blurb': 'Strong in Python, SQL, and system design',
        'skills': ['Python', 'SQL', 'System Design'],
    },
    {
        'rank': 2,
        'title': 'Data analyst',
        'score': 79,
        'blurb': 'Good foundation in SQL and statistics',
        'skills': ['SQL', 'Statistics', 'Excel'],
    },
    {
        'rank': 3,
        'title': 'Frontend developer',
        'score': 74,
        'blurb': 'Solid JavaScript, growing in React',
        'skills': ['JavaScript', 'React', 'CSS'],
    },
    {
        'rank': 4,
        'title': 'DevOps engineer',
        'score': 68,
        'blurb': 'Some exposure to Linux and CI/CD',
        'skills': ['Linux', 'CI/CD', 'Docker'],
    },
    {
        'rank': 5,
        'title': 'Mobile developer',
        'score': 61,
        'blurb': 'Limited experience, worth exploring',
        'skills': ['Kotlin', 'Swift', 'Git'],
    },
]


def results(request):
    return render(request, 'roadmap/results.html', {'top_matches': TOP_MATCHES})


def roadmap_overview(request):
    # Steps are pre-ordered by a topological sort over the skill/prerequisite
    # DAG (e.g. "Data Structures" before "API Integration" before "React
    # Native App") — the template just renders the sequence it's given.
    context = {
        'path_title': 'Backend Developer',
        'steps': [
            {
                'type': 'Course',
                'title': 'Data Structures',
                'description': 'Mastered core algorithms and memory management.',
                'status': 'completed',
            },
            {
                'type': 'Project',
                'title': 'API Integration',
                'description': 'Built a robust RESTful API using Node.js.',
                'status': 'completed',
            },
            {
                'type': 'Project',
                'title': 'React Native App',
                'description': 'Deploying your first cross-platform mobile application.',
                'status': 'current',
                'progress': 60,
            },
            {
                'type': 'Assessment',
                'title': 'System Design',
                'description': 'Mock interview for scalable architecture.',
                'status': 'locked',
            },
            {
                'type': 'Certification',
                'title': 'AWS Cloud Practitioner',
                'description': 'Validate your cloud fundamentals knowledge.',
                'status': 'locked',
            },
        ],
    }
    return render(request, 'roadmap/roadmap.html', context)


def skill_gap(request):
    context = {
        'path_title': 'Backend Developer',
        'matched_skills': ['Python', 'SQL', 'Git', 'REST APIs', 'Linux Basics'],
        'missing_skills': [
            {
                'name': 'System Design',
                'proficiency': 20,
                'description': 'Backend roles expect you to reason about scalability and trade-offs at a system level, not just write working code.',
                'icon': 'account_tree',
                'resource_label': 'View system design course',
            },
            {
                'name': 'Docker & Containers',
                'proficiency': 10,
                'description': "Almost every backend job posting for this path lists containerization — you haven't logged any project using it yet.",
                'icon': 'deployed_code',
                'resource_label': 'View Docker fundamentals',
            },
            {
                'name': 'Testing & CI/CD',
                'proficiency': 35,
                'description': 'You have some exposure, but no project shows automated tests or a CI pipeline — a common bar for internship readiness.',
                'icon': 'rule',
                'resource_label': 'View testing resources',
            },
        ],
    }
    return render(request, 'roadmap/gap_report.html', context)


def recommended_projects(request):
    context = {
        'path_title': 'Backend Developer',
        'projects': [
            {
                'title': 'Design a URL Shortener at Scale',
                'description': 'Practice reasoning about sharding, caching, and load balancing in a project you can talk through in interviews.',
                'closes_skill': 'System Design',
                'icon': 'account_tree',
                'tech': ['System Design', 'Redis', 'Load Balancing'],
                'difficulty': 'Intermediate',
                'estimated_time': '~1 week',
            },
            {
                'title': 'Containerize Your Portfolio API',
                'description': 'Wrap an existing project in Docker and deploy it, so you have hands-on containerization experience to point to.',
                'closes_skill': 'Docker & Containers',
                'icon': 'deployed_code',
                'tech': ['Docker', 'Docker Compose'],
                'difficulty': 'Beginner',
                'estimated_time': '~3 days',
            },
            {
                'title': 'Add a CI Pipeline to an Existing Repo',
                'description': "Set up automated tests and a GitHub Actions pipeline on a project you've already built.",
                'closes_skill': 'Testing & CI/CD',
                'icon': 'rule',
                'tech': ['GitHub Actions', 'Pytest', 'CI/CD'],
                'difficulty': 'Beginner',
                'estimated_time': '~4 days',
            },
            {
                'title': 'Build a Rate Limiter Microservice',
                'description': 'A focused, interview-relevant project that demonstrates distributed systems thinking without a huge time investment.',
                'closes_skill': 'System Design',
                'icon': 'account_tree',
                'tech': ['System Design', 'Node.js', 'Redis'],
                'difficulty': 'Advanced',
                'estimated_time': '~1 week',
            },
            {
                'title': 'Deploy a Multi-Container App',
                'description': 'Wire up a database, reverse proxy, and app server together with Docker Compose and deploy it.',
                'closes_skill': 'Docker & Containers',
                'icon': 'deployed_code',
                'tech': ['Docker Compose', 'Nginx', 'PostgreSQL'],
                'difficulty': 'Intermediate',
                'estimated_time': '~1 week',
            },
        ],
    }
    for project in context['projects']:
        project['tech'] = _styled_tags(project['tech'])
    return render(request, 'roadmap/projects.html', context)


def _fit_score_colors(score):
    if score >= 90:
        return {'ring_hex': '3525CD', 'text_class': 'text-[#3525CD]'}
    if score >= 75:
        return {'ring_hex': '006C49', 'text_class': 'text-[#006C49]'}
    return {'ring_hex': '684000', 'text_class': 'text-[#684000]'}


def internships(request):
    raw_listings = [
        {
            'title': 'Software Engineer Intern, Backend',
            'company': 'TechNova Systems',
            'location': 'Remote',
            'type': 'Full-time',
            'tags': ['Java', 'Spring Boot', 'SQL'],
            'score': 96,
        },
        {
            'title': 'Data Science Intern',
            'company': 'DataMetrics Inc.',
            'location': 'San Francisco',
            'type': 'Summer',
            'tags': ['Python', 'Pandas', 'ML'],
            'score': 88,
        },
        {
            'title': 'Frontend Developer Co-op',
            'company': 'CloudScape',
            'location': 'Remote',
            'type': 'Co-op',
            'tags': ['React', 'TypeScript', 'CSS'],
            'score': 82,
            'top_recommendation': True,
        },
        {
            'title': 'Backend Engineer Intern',
            'company': 'Ledger Labs',
            'location': 'New York',
            'type': 'Summer',
            'tags': ['Node.js', 'PostgreSQL', 'Docker'],
            'score': 74,
        },
        {
            'title': 'Platform Engineering Intern',
            'company': 'Northwind Cloud',
            'location': 'Remote',
            'type': 'Full-time',
            'tags': ['Kubernetes', 'Go', 'AWS'],
            'score': 69,
        },
        {
            'title': 'Mobile Developer Intern',
            'company': 'Appsphere',
            'location': 'San Francisco',
            'type': 'Co-op',
            'tags': ['Kotlin', 'Swift', 'Git'],
            'score': 65,
        },
    ]
    listings = []
    for item in raw_listings:
        item.update(_fit_score_colors(item['score']))
        item['tags'] = _styled_tags(item['tags'])
        listings.append(item)

    context = {
        'listings': listings,
        'locations': ['Remote', 'San Francisco', 'New York'],
        'types': ['Full-time', 'Summer', 'Co-op'],
    }
    return render(request, 'roadmap/internships.html', context)
