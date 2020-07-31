from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {
    #     'name':'keyur',
    #     'place':'Ahmedabad'
    # }
    return render(request,'index.html'  )
    # return HttpResponse('''<h1>hello Keyur</h1><a href='https://www.google.com/search?q=reliance+share&rlz=1C1CHBD_enIN900IN900&oq=relience+&aqs=chrome.1.69i57j0l2j46j0l2j46l2.8923j0j7&sourceid=chrome&ie=UTF-8'>Relince Share </a>''')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')


    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed +  char
        params = {
            'purpose' : 'Remove Punctuations',
            'analyzed_text' : analyzed
        }
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            'purpose': 'Changed to Uppercase',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+ char
        params = {
            'purpose': 'Remove NewLine',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {
            'purpose': 'Extra Space Remover',
            'analyzed_text': analyzed
        }
        djtext = analyzed


    if(removepunc != "on" and newlineremover != "on" and fullcaps != "on" and extraspaceremover != "on"  ):
        return HttpResponse("Error!!! No any one selected option")


    return render(request, 'analyze.html', params)
