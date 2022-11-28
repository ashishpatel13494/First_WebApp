from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.
def index(request):
    
    return render(request,"index.html",)

def result(request):
    article=request.GET['article']
    words=article.split()
    word_count=len(words)
    
    dict_words={}
    for word in words: 
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
            
    return render(request,"result.html",{"article":article,'word_count':word_count,'dict_words':dict_words})

def current_time(request):
    now=datetime.datetime.now()
    html="<h1>Time Now Is %s.</h1>"% now
    return HttpResponse(html)