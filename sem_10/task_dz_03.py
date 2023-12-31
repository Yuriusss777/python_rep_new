"""В большой текстовой строке подсчитать количество встречаемых слов
и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""


class WordCounter:
    def __init__(self, text):
        self.text = text.lower()
        self.word_counts = {}

    def clean_text(self):
        import re
        self.text = re.sub(r'[^\w\s]', '', self.text)

    def count_words(self):
        words = self.text.split()
        for word in words:
            if word in self.word_counts:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1

    def get_most_common_words(self, n):
        sorted_words = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        return [word[0] for word in sorted_words[:n]]


text = """
Python - высокоуровневый язык программирования, ориентированный на повышение производительности разработчика и читаемости кода. Одной из основных целей языка является предоставление ясного и простого синтаксиса, позволяющего программистам выражать свои идеи в более компактной и красивой форме. Python поддерживает как процедурное, так и объектно-ориентированное программирование, а также имеет богатую библиотеку стандартных инструментов, которая делает его очень мощным и универсальным языком, готовым к решению разнообразных задач.

Некоторые из ключевых особенностей Python:
- Простой и понятный синтаксис, удобный для изучения и использования.
- Динамическая типизация, позволяющая не указывать тип переменных при их объявлении.
- Автоматическое управление памятью, которое решает проблему утечек памяти и освобождения неиспользуемых объектов.
- Модульная архитектура и поддержка пакетов, позволяющая организовывать код в логические блоки и повторно использовать его.
- Большая библиотека стандартных инструментов, включающая модули для работы с файлами, сетью, базами данных, математическими вычислениями и многим другим.
- Поддержка многочисленных сторонних библиотек, которые расширяют возможности Python и позволяют решать специфические задачи.

Python широко используется во множестве областей, включая веб-разработку, научные исследования, анализ данных, машинное обучение, автоматизацию задач, создание игр и многое другое. Благодаря своей простоте и мощности, Python стал одним из самых популярных языков программирования в мире.
"""

counter = WordCounter(text)
counter.clean_text()
counter.count_words()
most_common_words = counter.get_most_common_words(10)

print(f"10 самых частых слов:\n{most_common_words}")
