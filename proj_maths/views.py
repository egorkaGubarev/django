from django.shortcuts import render, redirect
from django.core.cache import cache
from proj_maths import db_stars
from proj_maths.db_stars import create_questions


def hello(request, name='Unknown User'):
    name_provided = False
    if request.method == 'GET' and 'my_input' in request.GET:
        name = request.GET['my_input']
        name_provided = True
    return render(request, 'hello.html', context={'name': name, 'name_provided': name_provided})

def index(request):
    return render(request, "index.html")


def terms_list(request):
    stars = db_stars.db_get_stars_for_table()
    return render(request, "term_list.html", context={"stars": stars})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    cache.clear()
    star_name = request.POST.get("star_name")
    star_type = request.POST.get("type")
    magnitude = request.POST.get("magnitude")
    constellation = request.POST.get("constellation")
    context = {"success": True, "comment": "Звезда добавлена"}
    db_stars.db_write_star(star_name, star_type, magnitude, constellation)
    return render(request, "term_request.html", context)

def show_stats(request):
    stats = db_stars.db_get_star_stats()
    return render(request, "stats.html", context={'stats': stats})

def result(request):
    constellations = request.POST.get('constellationКохаб')
    return render(request, "results.html", context={'constellations': constellations})

def quiz_view(request):
    questions = create_questions()

    if request.method == 'POST':
        for q_id in questions:
            user_answer = request.POST.get(q_id, '').strip()
            questions[q_id]['user_answer'] = user_answer

        request.session['quiz_results'] = questions
        return redirect('/results')

    return render(request, 'quiz.html', {'questions': questions})

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
