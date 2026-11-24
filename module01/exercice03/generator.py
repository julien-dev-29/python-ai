import random

def generator(text: str, sep = " ", option = None):
    '''
    Split the text according  to sep value and yields the substring
    '''
    splited_text = text.split(sep=sep)
    if option == "ordered":
       n = len(splited_text)
       for i in range(n):
           for j in range(0, n - i - 1):
               if splited_text[j] > splited_text[j + 1]:
                   splited_text[j], splited_text[j + 1] = splited_text[j + 1], splited_text[j]
    for word in splited_text:
        yield word