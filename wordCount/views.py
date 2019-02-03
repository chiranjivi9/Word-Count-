import operator
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def count(request):
    fulltext = request.GET['textarea']
    print(fulltext)
    wordDictionary = {}
    wordList = fulltext.split()

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext' : fulltext, 'count': (len(wordList)), 'sortedWords' : sortedWords})
