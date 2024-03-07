#The author's names are Sydney Eidelbes and Leena Bradley

def too_long(string):
    if len(string) <= 140:
        print("Length is okay!")
        print(string)
    else:
        print("Too long!")
