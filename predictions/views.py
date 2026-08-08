from django.shortcuts import render

PATHS = {
    'full-stack-developer': {
        'title': 'Full-Stack Developer',
        'score': 94,
        'alignment_label': 'Excellent Alignment',
        'summary': "Your current skill profile strongly matches the requirements for a Full-Stack Developer role based on market data.",
        'contributors': [
            {
                'icon': 'code_blocks',
                'icon_bg_class': 'bg-[#3525CD]/10',
                'icon_text_class': 'text-[#3525CD]',
                'title': 'Strong React Foundation',
                'description': "Your recent 'E-commerce Platform' project demonstrated advanced state management and component architecture.",
            },
            {
                'icon': 'database',
                'icon_bg_class': 'bg-[#006C49]/10',
                'icon_text_class': 'text-[#006C49]',
                'title': 'Database Proficiency',
                'description': 'High scores in SQL and MongoDB modules confirm your ability to handle complex data structures.',
            },
            {
                'icon': 'api',
                'icon_bg_class': 'bg-[#885500]/30',
                'icon_text_class': 'text-[#684000]',
                'title': 'RESTful API Design',
                'description': 'Successfully deployed 3 projects utilizing robust API integrations and custom endpoint creation.',
            },
            {
                'icon': 'psychology',
                'icon_bg_class': 'bg-[#FFDAD6]',
                'icon_text_class': 'text-[#93000A]',
                'title': 'Problem Solving',
                'description': 'Consistent performance in algorithm challenges indicates strong analytical thinking required for this role.',
            },
        ],
    },
}


def predict(request):
    return render(request, 'placeholder.html', {'page_title': 'Career Prediction'})


def prediction_result(request):
    return render(request, 'placeholder.html', {'page_title': 'Prediction Result'})


def path_detail(request, role_slug='full-stack-developer'):
    context = PATHS.get(role_slug, PATHS['full-stack-developer'])
    return render(request, 'predictions/path_detail.html', context)
