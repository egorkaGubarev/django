from django.shortcuts import render
from django.core.cache import cache
from proj_maths import db_stars


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
