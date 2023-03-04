import random
from lexicon.lexicon_ru import LEXICON_RU


# Функция возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spok'])


# Функция возвращающая ключ из словаря по которому
# хранится значение, передаваемое как аргумент - выбор пользоватедля
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


# Функция определяющая победителя
def get_winner(user_choice: str, bot_choice: str):
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': ['scissors', 'lizard'],
                             'scissors': ['paper', 'lizard'],
                             'paper': ['rock', 'spok'],
                             'lizard': ['spok', 'paper'],
                             'spok': ['scissors', 'rock']}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif bot_choice in rules[user_choice]:
        return 'user_won'
    else:
        return 'bot_won'
