#The author's names are Sydney Eidelbes and Leena Bradley

def num_os(word):
    count=0
    for letter in word:
        if letter == "o":
            count=count+1
    print(count)

num_os("bonobos")
num_os("apple")
num_os("bob")

