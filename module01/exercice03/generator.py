import random

def generator(text: str, sep = " ", option = None):
    '''
    Split the text according  to sep value and yields the substring
    '''
    if (
        not isinstance(text, str)
        or not text.isprintable()
        or not isinstance(sep, str)
        or len(sep) == 0
        or option not in (None, "shuffle", "unique", "ordered")
    ):
        print("ERROR")
        return
    
    splited_text = text.split(sep=sep)
    n = len(splited_text)

    if option == "shuffle":
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            splited_text[i], splited_text[j] = splited_text[j], splited_text[i]

    elif option == "unique":
        unique_words = []

        for word in splited_text:
            if word not in unique_words:
                unique_words.append(word)
        splited_text = unique_words

    elif option == "ordered":
       for i in range(n):
           for j in range(0, n - i - 1):
               if splited_text[j] > splited_text[j + 1]:
                   splited_text[j], splited_text[j + 1] = splited_text[j + 1], splited_text[j]

    for word in splited_text:
        yield word