from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from .models import *
from datetime import date
from django.contrib import messages
from math import ceil
import json


# Create your views here.
def education(request):
    # Fetch top three posts based on number of views.
    return render(request, 'education/index.html')


def student(request):
    if request.method == 'POST':
        f = request.FILES['notesfile']
        Notes.objects.create(notesfile=f)
    
    allProds = []
    catprods = Notes.objects.values('branch', 'id')
    cats = {item['branch'] for item in catprods}
    
    for cat in cats:
        prod = Notes.objects.filter(branch=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # ✅ Collect unique branches and subjects for filtering
    branches_set = set()
    subjects_set = set()
    for group, _, _ in allProds:
        for note in group:
            branches_set.add(note.branch)
            subjects_set.add(note.subject)

    context = {
        'allProds': allProds,
        'branches': sorted(branches_set),
        'subjects': sorted(subjects_set),
    }

    return render(request, 'education/education.html', context)

def teachers(request):
    return render(request, 'education/404.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'blog/search.html', params)

def studentView(request, myid):

    # Fetch the product using the id
    notes = Notes.objects.filter(id=myid)
    return render(request, 'education/studentview.html', {'notes':notes[0]})

