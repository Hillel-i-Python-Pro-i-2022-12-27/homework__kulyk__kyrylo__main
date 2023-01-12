from random import randint
from faker import Faker


def greetings() -> str:
    fake = Faker()
    return f"Hello {fake.name()}!"


def student_grade() -> str:
    rand_int = randint(0, 100)
    if rand_int >= 95:
        return f"You graduated with a score of {rand_int}, excellent!"
    elif 85 <= rand_int >= 94:
        return f"You graduated with a score of {rand_int}, very good!"
    elif 65 <= rand_int >= 84:
        return f"You graduated with a score of {rand_int}, good!"
    else:
        return f"Your score is {rand_int}, please try again."
