def read_file():
    with open("input.txt", "r") as f:
        text = f.read()
        return text
text = read_file()


def clean_text(text):
    text.lower()
    text.split()
    text=text.replace("\n"," ")
    return text


def count(text):
    words = 0
    char = 0
    for t in text.split():
        words += 1
        for w in t:
            char += 1
    return (words, char)
words,char=count(text)


def frequency(text):
    text1=text.lower()
    f = {}
    for freq in text1.split():
        if freq not in f:
            f[freq] = 1
        else:
            f[freq] += 1

    return f


def max(text):
    f = frequency(text)
    current = 0
    max_word=[]
    
    for freq in f:
        if f[freq] > current:
            current = f[freq]
            max_word=[freq]
        elif f[freq] == current:
            max_word.append(freq)
        

    return max_word


def longest(text):
    text=text.split()
    prev = len(text[0])
    longest = None
    for word in text[1:]:
        if len(word) > prev:
            longest = word
            prev = len(word)
    return longest




def vowelandconso(text):
    vowel = 0
    con = 0
    for ch in text:
        if ch in "aeiou":
            vowel += 1
        else:
            con += 1

    return (vowel, con)
vowel,consonant=vowelandconso(text)

result={ 
    "clean text:":clean_text(text),
    "word:":words,
    "charecter":char,
    "frequency:":frequency(text),
    "max word:":max(text.lower()),
    "longest":longest(text),
    "vowel":vowel,
    "consonant":consonant
}

print(result)
