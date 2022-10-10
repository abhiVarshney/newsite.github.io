from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template import loader
jobs=['First Job','Second Job','Third Job']
jobDescription=['First job is going to be web developer','Second job is Software developer','This is a freelancer job']

def home(request):
    items='<ul>'
    for i in jobs:
        jobId=jobs.index(i)
        jobId=str(jobId)
        detailUrl=reverse('jobDetail',args=(jobId,))
        items+=f"<li><a href='{detailUrl}'>{i}</a></li>"
    items+='</ul>'
    return HttpResponse(items)
        

def jobDetails(request,id):
    try:
        return_html=f"<h2>{jobs[int(id)]}</h2><h3><u>Description-</u></h3>{jobDescription[int(id)]}"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound('No result found')

class test:
    x=45
    age=18

def show(request):
    # template=loader.get_template('app/hello.html')
    t=test()
    fList=['Abhinav','Varshney']
    authenticated=True
    context={"name":"User","listt":fList,"classObject":t,"age":t,"authenticated":authenticated}
    # return HttpResponse(template.render(context,request))
    return render(request,'app/index.html',context)

