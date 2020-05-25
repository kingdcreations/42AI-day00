import string


def text_analyzer(*text):
    """\n\tThis function counts the number of upper characters, lower
     characters, punctuation and spaces in a given text."""
    if (len(text) > 1):
        print("ERROR")
    elif len(text) == 0:
        s = input("What is the text to analyse?\n")
        text_analyzer(s)
    elif isinstance(text[0], str) is not True:
        print("ERROR")
    else:
        n = 0
        up = 0
        low = 0
        punc = 0
        sp = 0
        for x in text[0]:
            n += 1
            if (x.isupper()):
                up += 1
            if (x.islower()):
                low += 1
            if (x in string.punctuation):
                punc += 1
            if (x.isspace()):
                sp += 1
        print("The text contains", n, "characters:\n")
        print("-", up, "upper letters\n")
        print("-", low, "lower letters\n")
        print("-", punc, "punctuation marks\n")
        print("-", sp, "spaces")
