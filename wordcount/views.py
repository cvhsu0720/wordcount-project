# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddict = {}
    
    for word in wordlist:
        if word in worddict:
            # Increase
            worddict[word] +=1
        else:
            #Add to the dictionary
            worddict[word] = 1
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), \
                                          'worddict':sortedwords})
def about(request):
    return render(request, 'about.html')