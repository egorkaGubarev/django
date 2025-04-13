from django.shortcuts import render
from django.core.cache import cache
from proj_maths import terms_db


def hello(request, name='Unknown User'):
    name_provided = False
    if request.method == 'GET' and 'my_input' in request.GET:
        name = request.GET['my_input']
        name_provided = True
    return render(request, 'hello.html', context={'name': name, 'name_provided': name_provided})

def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_db.db_get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    cache.clear()
    user_name = request.POST.get("name")
    new_term = request.POST.get("new_term", "")
    new_definition = request.POST.get("new_definition", "").replace(";", ",")
    context = {"user": user_name}
    if len(new_definition) == 0:
        context["success"] = False
        context["comment"] = "Описание должно быть не пустым"
    elif len(new_term) == 0:
        context["success"] = False
        context["comment"] = "Термин должен быть не пустым"
    else:
        context["success"] = True
        context["comment"] = "Ваш термин принят"
        terms_db.db_write_term(new_term, new_definition, user_name)
    if context["success"]:
        context["success-title"] = ""
    return render(request, "term_request.html", context)

def show_stats(request):
    stats = terms_db.db_get_terms_stats()
    return render(request, "stats.html", context={'stats': stats})
