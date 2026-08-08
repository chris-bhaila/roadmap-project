from django.shortcuts import render


def _compute_ema(values, alpha=0.4):
    ema = [float(values[0])]
    for v in values[1:]:
        ema.append(alpha * v + (1 - alpha) * ema[-1])
    return ema


def progress_overview(request):
    labels = ['Wk 1', 'Wk 3', 'Wk 5', 'Wk 7', 'Wk 9', 'Wk 11', 'Wk 13', 'Wk 15', 'Wk 17', 'Wk 19']
    raw_scores = [58, 66, 59, 71, 67, 77, 72, 81, 78, 87]
    ema_scores = _compute_ema(raw_scores, alpha=0.4)

    points = [
        {'label': label, 'raw': raw, 'ema': round(ema, 1)}
        for label, raw, ema in zip(labels, raw_scores, ema_scores)
    ]

    current_score = round(ema_scores[-1])
    previous_score = round(ema_scores[-2])
    delta = current_score - previous_score

    context = {
        'points': points,
        'current_score': current_score,
        'current_label': labels[-1],
        'delta': delta,
        'insights': [
            {
                'icon': 'trending_up' if delta >= 0 else 'trending_down',
                'title': f"{'Up' if delta >= 0 else 'Down'} {abs(delta)} pts since {labels[-2]}",
                'description': 'Consistent engagement with technical modules is paying off.',
            },
            {
                'icon': 'task_alt',
                'title': 'Project completions boosted your score',
                'description': 'Your latest submitted project added measurable readiness gains.',
            },
        ],
    }
    return render(request, 'progress/tracker.html', context)


def history(request):
    # Stored oldest-first so the EMA and trend deltas are computed in real
    # chronological order, then reversed for the newest-first display list.
    checkins_chronological = [
        {
            'date': 'Apr 15, 2024',
            'raw': 68,
            'changes': [
                {'icon': 'flag', 'text': 'Initial assessment completed.'},
                {'icon': 'build', 'text': 'Identified core focus areas: Java, Systems Design'},
            ],
        },
        {
            'date': 'May 3, 2024',
            'raw': 72,
            'changes': [
                {'icon': 'update', 'text': 'Completed Data Structures review module'},
                {'icon': 'edit_document', 'text': 'Updated resume with recent class project'},
            ],
        },
        {
            'date': 'May 28, 2024',
            'raw': 65,
            'changes': [
                {'icon': 'menu_book', 'text': 'Light activity this cycle — one course module completed'},
                {'icon': 'schedule', 'text': 'No new projects logged since last check-in'},
            ],
        },
        {
            'date': 'Jun 12, 2024',
            'raw': 78,
            'changes': [
                {'icon': 'add', 'text': 'Added 2 new skills: Docker, Kubernetes'},
                {'icon': 'trending_up', 'text': 'Advanced Python proficiency from Intermediate to Advanced'},
            ],
        },
        {
            'date': 'Jul 9, 2024',
            'raw': 83,
            'changes': [
                {'icon': 'deployed_code', 'text': 'Shipped a containerized side project using Docker Compose'},
                {'icon': 'quiz', 'text': 'Scored in the 90th percentile on the algorithms assessment'},
            ],
        },
        {
            'date': 'Aug 1, 2024',
            'raw': 80,
            'changes': [
                {'icon': 'menu_book', 'text': 'Reviewed system design fundamentals'},
                {'icon': 'schedule', 'text': 'Slower month — one module in progress, not yet complete'},
            ],
        },
    ]

    raw_scores = [c['raw'] for c in checkins_chronological]
    ema_scores = _compute_ema(raw_scores, alpha=0.4)

    entries = []
    for i, (checkin, ema) in enumerate(zip(checkins_chronological, ema_scores)):
        if i == 0:
            status, status_class, icon = 'Initial Baseline', 'bg-[#DEE8FF] text-[#464555]', None
        else:
            delta = ema - ema_scores[i - 1]
            if delta > 1:
                status, status_class, icon = 'Improved', 'bg-[#6CF8BB] text-[#006C49]', 'trending_up'
            elif delta < -1:
                status, status_class, icon = 'Declined', 'bg-[#FFDAD6] text-[#93000A]', 'trending_down'
            else:
                status, status_class, icon = 'Steady', 'bg-[#DEE8FF] text-[#464555]', 'trending_flat'
        entries.append({
            'date': checkin['date'],
            'raw': checkin['raw'],
            'ema': round(ema, 1),
            'status': status,
            'status_class': status_class,
            'status_icon': icon,
            'changes': checkin['changes'],
        })

    context = {'entries': list(reversed(entries))}
    return render(request, 'progress/history.html', context)
