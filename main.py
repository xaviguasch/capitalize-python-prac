'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(word):
    return word[:1].upper() + word[1:]


print(capitalize("amigo"))