# -*- coding: cp936 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from books.models import Author
from todo.models import Task
from django import forms
from django.contrib.auth.forms import UserCreationForm
import datetime
pwd = "/Users/apple/Desktop/github/bloodycoder/todo_reminder/memorycurv/credit/data/"
def hello(request):
    t = get_template('text.html')
    values = request.META.items()
    html = ''
    for k in values:
        html +=(t.render(Context({'name1':k[0],'name2':k[1]})))
    return HttpResponse(html)
    

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if(len(q)>20):
            errors.append("Please less than 20 words")
        if(not request.GET['q']):
            errors.append("Please input sth")
        if(not errors):
            aut = Author.objects.filter(first_name__icontains= q)
            return render_to_response('search_results.html',{'books':aut,'query':q})
        return render_to_response('search_form.html',{'errors':errors})
    else:
        return render_to_response('search_form.html',{'errors':errors})



def todo_index(request):
    all_task = Task.objects.all()
    f = open(pwd+"job")
    jobs = f.readlines()
    f.close()
    new_dict = []
    for i in range(len(jobs)):
        job = jobs[i]
        my_dict = dict()
        jobsplit = job.split(',')
        my_dict['task_id'] = i+1
        my_dict['task_name'] = jobsplit[0]
        my_dict['task_credit'] = jobsplit[1]
        new_dict.append(my_dict)
    print jobs
    print new_dict
    return render_to_response('todo_index.html',{'tasks':new_dict})

def todo_add(request):
    return render_to_response('todo_add.html')
def todo_adddata(request):
    if 'q' in request.GET:
        q  = request.GET['q']
        if(not q):
            return HttpResponseRedirect('/todo/add/')
        f = open(pwd+"job")
        jobs = f.readlines()
        f.close()
        new_line = q +','+'0'+'\n'
    	jobs.append(new_line)
        f = open(pwd+'job','w+')
    	f.writelines(jobs)
        f.close()
        return HttpResponseRedirect('/todo/')
    
def todo_del(request):
    q = request.GET['q']
    print q
    code1 = int(q)
    f = open(pwd+"job")
    jobs = f.readlines()
    f.close()
    item = jobs[code1-1]
    item = item.split(',')
    job_name = item[0]
    item = int(item[1])
    del jobs[code1-1]
    f = open(pwd+'job','w+')
    f.writelines(jobs)
    f.close()
    return HttpResponseRedirect('/todo/')
def todo_reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form,
    })

