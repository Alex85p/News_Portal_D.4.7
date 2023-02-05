from django import template

register = template.Library()


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError("Value must be a string")
    else:
        bad_words = ['badword1', 'badword2', 'badword3']
        words = value.split()
        for i, word in enumerate(words):
            if word.lower() in bad_words:
                words[i] = word[0] + "*" * (len(word) - 1)
        return " ".join(words)
