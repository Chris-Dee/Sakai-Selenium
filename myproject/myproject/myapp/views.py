# -*- coding: utf-8 -*-
import os
import sys
import json
import imp
import time

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotModified, HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from myproject.myapp.models import Site
from myproject.myapp.forms import SiteForm


def list(request):
    # Handle file upload

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        site_form = SiteForm(request.POST)
        if form.is_valid():
            print request.FILES
            print request.POST
            print "this is the resquet"
            newdoc = Document(title=request.POST['titleField'],docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
        elif site_form.is_valid():
            print request.POST
            print "this is the request"
            newsite = Site(url=request.POST['urlField'])
            newsite.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))

    else:
        form = DocumentForm()  # A empty, unbound form
        site_form = SiteForm()
    print request.GET
    # Load documents for the list page
    documents = Document.objects.all()
    sites = Site.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'sites': sites, 'form': form, 'site_form': site_form},
        context_instance=RequestContext(request)
    )

def script(request):

    if request.method == 'GET':
        title = request.GET['title']
        current_file = Document.objects.get(title=title).docfile
        target = open('.' + current_file.url, 'r')
        timestring = str(int(time.time()))
        stderr_temp = sys.stderr
        target = open("." + current_file.url, 'r')      
        log_file = open("selenium_log" + timestring, 'w+')
        sys.stderr = log_file
        test_import = imp.load_source('test_import', '.' + current_file.url)
        #print test_import.__dict__.keys()
        test_import.unittest.main(module=test_import, argv=sys.argv[:1], exit=False)
        sys.stderr = stderr_temp
        log_file.close()
        read_file = open("selenium_log" + timestring, 'r')
        test_output = read_file.read()
        print read_file.read()
        response_data = {
            'result': test_output 
        }
        print test_output
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
    
    if request.method == 'DELETE':
        title = json.loads(request.read())['title']
        Document.objects.get(title = title).delete()
        return HttpResponse(status=200)