from django.http import HttpResponse
from django.shortcuts import render
import operator


def inputpage(request):
    return render(request, 'enterdata.html')

def countpage(request):
    sabkuch = request.GET['sabkuch']
    kitna = sabkuch.split()
    print(sabkuch)
    kitna_dic={}
    for word in kitna:
        if(word in kitna_dic):
            kitna_dic[word] +=1
        else:    
            kitna_dic[word] = 1
    
    sortedwords = sorted(kitna_dic.items(), key=operator.itemgetter(1), reverse=True )

    return render(request, 'countpage.html',{'sabkuch':sabkuch, 'kitna': len(kitna),'sortedwords':sortedwords, 'dictionary':kitna_dic.items()})

#just messing with git

def homepage(request):
    return render(request,'homepage.html')
def aibaan(request):
    return render(request,'khele.html', {'First':'idk', 'Second':'wyd', 'Third':'stfu', 'Fourth':'idts'})

