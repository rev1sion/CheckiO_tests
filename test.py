"""
Ваша задача в этой миссии определить популярность определенных слов в тексте.

На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность которых необходимо определить.

При решении этой задачи обратите внимание на следующие моменты

Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
Искомые слова всегда указаны в нижнем регистре
Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
Входные параметры: Текст и массив искомых слов.

Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.
"""

import re


def popular_words(text: str, words: list) -> dict:
    z = [x.lower() for x in re.findall('[A-Za-z\']+(?:\'[A-Za-z]+)?', text) for w in words if re.findall(r'\b%s\b' % w, x.lower())]
    result = []
    for w in words:
        result.append((w, z.count(w)))

    return dict(result)

    # for i in t:
    #     i = i.lower()
    #     z = i in words
    #     if i in words:
    #         result.append(result)
    # for word in words:
    #     f = t.lower().find(word)
    #     result.append(text[f])


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
