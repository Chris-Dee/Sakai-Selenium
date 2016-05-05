# -*- coding: utf-8 -*-
import os
import sys
import json
import imp
import time
import csv
import subprocess
from StringIO import StringIO

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
        url = request.GET['url']
        current_file = Document.objects.get(title=title).docfile
        
	#Write URL to CSV
        responseCSV = HttpResponse(content_type='text/csv')
        responseCSV['Content-Disposition'] = 'attachment; filename="defaultname.csv"'
        writer = csv.writer(responseCSV)
        writer.writerow(['url', url])
	
        timestring = str(int(time.time()))
        stderr_temp = sys.stderr
	stdout_temp = sys.stdout
        print sys.stderr
        curr_path = os.path.dirname(os.path.abspath(__file__))
        log_filename = curr_path + "/logs/"+title+"selenium_log" + timestring + ".log"
        log_filename=log_filename.replace(" ", "_")
	print log_filename
	#log_string = StringIO()
        if not os.path.exists(os.path.dirname(log_filename)):
                print "yay"
                try:
                    os.makedirs(os.path.dirname(log_filename))
		except OSError:
                    raise Exception("creating directory failed")
        log_file = open(log_filename, 'w+')

	#print sys.stderr
	#print sys.stdout
        #sys.stderr = log_string
	#sys.stdout = log_string

	#test_import = imp.load_source('test_import', '.' + current_file.url)
        subprocess.call(["python", os.getcwd() + current_file.url], stdout=log_file, stderr=log_file)	
        #test_import.unittest.main(module=test_import, argv=sys.argv[:1], exit=False)
	
	#print sys.stderr
	#print sys.stdout
        #sys.stderr = stderr_temp
	#sys.stdout = stdout_temp
	#print sys.stderr
	#print sys.stdout
        #log_file.write(log_string.getvalue())
#        log_file = open("selenium_log" + timestring, 'r')
        
	#test_output = log_string.getvalue()
        log_file.close() 
	log_file = open(log_filename, 'r')
	test_output = log_file.read()
        print log_file.read()
        response_data = {
            'result': test_output
        }
	print "right before"
        print test_output
	log_file.close()
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
    
    if request.method == 'DELETE':
        title = json.loads(request.read())['title']
        Document.objects.get(title = title).delete()
        return HttpResponse(status=200)
