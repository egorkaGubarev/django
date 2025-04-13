import numpy as np
from proj_maths.models import Star


def db_get_stars_for_table():
    terms = []
    for i, item in enumerate(Star.objects.all()):
        terms.append([i + 1, item.star, item.type, item.magnitude, item.constellation])
    return terms

def db_write_star(name, star_type, magnitude, constellation):
    star = Star(star=name, type=star_type, magnitude=magnitude, constellation=constellation)
    star.save()

def db_get_star_stats():
    stars = Star.objects.all()
    magnitudes = [star.magnitude for star in stars]
    stats = {
        "stars_all": len(stars),
        "magnitude_avg": round(np.mean(magnitudes), 2),
        "magnitude_max": max(magnitudes),
        "magnitude_min": min(magnitudes)
    }
    return stats

def create_questions(amount=2):
    stars = np.array(Star.objects.all())
    rng = np.random.default_rng()
    numbers = rng.choice(len(stars), size=amount, replace=False)
    stars_in_game = stars[numbers]
    questions = {'q' + str(i): {'text': stars_in_game[i].star,
                                'correct_answer': stars_in_game[i].constellation,
                                'user_answer': None} for i in range(amount)}
    return questions
