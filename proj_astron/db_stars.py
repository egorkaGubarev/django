import numpy as np
from proj_astron.models import Star


def db_get_stars_for_table():
    stars = []
    for i, item in enumerate(Star.objects.all()):
        stars.append([i + 1, item.star, item.type, item.magnitude, item.constellation])
    return stars

def db_write_star(name, star_type, magnitude, constellation):
    Star(star=name, type=star_type, magnitude=magnitude, constellation=constellation).save()

def db_get_star_stats():
    magnitudes = [star.magnitude for star in Star.objects.all()]
    return {"stars_all": len(magnitudes),
            "magnitude_avg": round(np.mean(magnitudes), 2),
            "magnitude_max": max(magnitudes),
            "magnitude_min": min(magnitudes)}

def create_questions(amount=5):
    stars = np.array(Star.objects.all())
    stars_in_game = stars[np.random.default_rng().choice(len(stars), size=amount, replace=False)]
    return {'q_' + str(i): {'text': stars_in_game[i].star,
                            'correct_answer': stars_in_game[i].constellation,
                            'user_answer': None} for i in range(amount)}
