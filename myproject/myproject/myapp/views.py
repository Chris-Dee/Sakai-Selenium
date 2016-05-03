# -*- coding: utf-8 -*-
import os

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotModified
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm


def list(request):
    # Handle file upload

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES
            print request.POST
            print "this is the resquet"
            newdoc = Document(title=request.POST['titleField'],docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form
    print request.GET
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def script(request):

    if request.method == 'GET':
        title = request.GET['title']
        current_file = Document.objects.get(title=title).docfile
        print current_file.url
        #script = __import__(current_file.url)
        #print sript.dict
        target = open('.' + current_file.url, 'r')
        print target.read()
        os.system("python ." + current_file.url)
        return HttpResponseNotModified()