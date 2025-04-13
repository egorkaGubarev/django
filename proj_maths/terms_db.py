from proj_maths.models import Term


def db_get_terms_for_table():
    terms = []
    for i, item in enumerate(Term.objects.all()):
        terms.append([i + 1, item.term, item.definition])
    return terms

def db_write_term(new_term, new_definition, user_name):
    term = Term(term=new_term, definition=new_definition, author=user_name)
    term.save()

def db_get_terms_stats():
    db_terms = len(Term.objects.filter(author='db'))
    user_terms = len(Term.objects.exclude(author='db'))
    terms = Term.objects.all()
    definition_len = [len(term.definition.split()) for term in terms]
    stats = {
        "terms_all": db_terms + user_terms,
        "terms_own": db_terms,
        "terms_added": user_terms,
        "words_avg": round(sum(definition_len)/len(definition_len), 2),
        "words_max": max(definition_len),
        "words_min": min(definition_len)
    }
    return stats
