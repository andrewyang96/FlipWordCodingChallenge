import re

# load 10000 word list and sort descending by length and all lowercase
wordlist = []
with open("data/google-10000-english.txt", "r") as f:
    for line in f.readlines():
        wordlist.append(line.strip())
wordlist.sort(key=len, reverse=True)

# load sentences from 1984
sents = []
with open("data/1984.txt", "r") as f:
    for line in f.readlines():
        for sentence in [sent.strip().replace("\x92", "'") for sent in line.split(".")]:
            if sentence != "":
                sents.append(sentence)

# load words from the sentences (is a 2-D array and all lowercase)
words = []
for sent in sents:
    words.append([word.lower() for word in re.findall(r"[\w']+", sent)])

# wordlist - sorted list of words, all lowercase
# sents - list of sentences
# words - list of words that appear in sents, all lowercase
# returns a string representing the sentence that the most difficult word appears in
def analyze(wordlist, sents, words):
    for word in wordlist:
        isWordInList = []
        for sent in words:
            isWordInList.append(word in sent)
        if True in isWordInList:
            print word, "exists"
            indices = [i for i, x in enumerate(isWordInList) if x]
            indexdict = {}
            for index in indices:
                indexdict[index] = words[index].index(word)
            minIndex = min(indexdict, key=indexdict.get)
            return sents[minIndex] + "."
    return None

if __name__ == "__main__":
    print analyze(wordlist, sents, words)
