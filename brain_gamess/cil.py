"""Импортируем промт для простоты написания кода."""
import prompt  # импорт модуля

"""Promt is some module"""


def welcome_user():
    """Это функция.

    Она спрашивает имя пользователя
    после ввода имени пользоваетля,
    она приветствует его.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
