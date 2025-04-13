from django.shortcuts import render, redirect
from django.core.cache import cache
from proj_astron import db_stars
from proj_astron.db_stars import create_questions


def index(request):
    return render(request, "index.html")

def stars_list(request):
    stars = db_stars.db_get_stars_for_table()
    return render(request, "stars_list.html", context={"stars": stars})

def add_star(request):
    return render(request, "star_add.html")

def send_star(request):
    cache.clear()
    star_name = request.POST.get("star_name")
    star_type = request.POST.get("type")
    magnitude = request.POST.get("magnitude")
    constellation = request.POST.get("constellation")
    if magnitude.isdigit():
        context = {"success": True, "comment": "Звезда добавлена"}
        db_stars.db_write_star(star_name, star_type, magnitude, constellation)
    else:
        context = {"success": False, "comment": "Величина должна быть числом"}
    return render(request, "star_request.html", context)

def show_stats(request):
    return render(request, "stats.html", context={'stats': db_stars.db_get_star_stats()})

def quiz_view(request):
    if request.method == 'GET':
        questions = create_questions()
        request.session['questions'] = questions
        return render(request, 'quiz.html', {'questions': questions})

    if request.method == 'POST':
        questions = request.session['questions']
        for q_id in questions:
            user_answer = request.POST.get(q_id, '').strip()
            questions[q_id]['user_answer'] = user_answer

        request.session['quiz_results'] = questions
        return redirect('/results')

def results_view(request):
    results = request.session.get('quiz_results', {})

    correct_count = sum(
        1 for q in results.values()
        if q['user_answer'].lower() == q['correct_answer'].lower()
    )

    context = {
        'results': results,
        'total': len(results),
        'correct': correct_count,
        'percentage': int(correct_count / len(results) * 100) if results else 0
    }

    return render(request, 'results.html', context)
