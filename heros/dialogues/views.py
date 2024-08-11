from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bsearch(request,pid):
    balayya=[
             {'id':1,'name': "Flute jinka mundhu oodhu,simham mundhu kaadhu"},
             {'id':2,'name': "Once I step in History Repeats"},
       
            ]
    result=None
    for item in balayya:
           if item.get('id')==pid:
                result=item
                break
    if result is not None:
         return HttpResponse(f"<p>Dialogue: {result.get('name')}</p>")
    else:
         return HttpResponse("Dialogues emi levu ra ayya.....")

def csearch(request,pid):
     chiru=[
             {'id':1,'name':"Rananukunnara ralenanukunnara"},
             {'id':2,'name':"Raavalanukunna vaadu vasthey anandhapadaley kaani aashchryapootharey!"},

            ]
     result=None
     for item in chiru:
           if item.get('id')==pid:
                result=item
                break
     if result is not None:
         return HttpResponse(f"<p>Dialogue: {result.get('name')}</p>")
     else:
         return HttpResponse("Dialogues emi levu ra ayya.....") 

def vsearch(request,pid):
      venky=[
             {'id':1,'name': "Iam DCP Ramchandra Myan....."},
             {'id':2,'name': "ohh shit myaan..shit"},
            ]
      result=None
      for item in venky:
           if item.get('id')==pid:
                result=item
                break
      if result is not None:
        return HttpResponse(f"<p>Dialogues :{result.get('name')}</p>")
      else:
        return HttpResponse("Dialogues emi levu ra ayya.....") 
