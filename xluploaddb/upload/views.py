# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.files import File

#from myapp import ExcelParser
import xlrd  
from upload.models import Document
from upload.forms import DocumentForm
import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="rite123", 
                      db="test")
test = 'c'

def list(request):    
   if request.method == 'POST':
      form = DocumentForm(request.POST, request.FILES)
      if form.is_valid():
         newdoc = Document(docfile = request.FILES['docfile'])
         newdoc.save()
         newdoc = newdoc.docfile.name
         newdoc = str(newdoc)
         wb = xlrd.open_workbook(newdoc)
         sh = wb.sheet_by_index(0)
         c = 1
         while c < len(sh.col(0)):
           first = sh.col_values(0)[c]
           second = sh.col_values(1)[c]
           x = db.cursor()
           db.set_character_set('utf8')
           x.execute('SET NAMES utf8;')
           x.execute('SET CHARACTER SET utf8;')
           x.execute('SET character_set_connection=utf8;')
           x.execute("INSERT INTO testcont_content(title, description) VALUES('%s','%s');"%(first,second))
           db.commit()
           c=c+1
         # Redirect to the document list after POST
         return HttpResponseRedirect(reverse('upload.views.list'))
   else:
      form = DocumentForm() # A empty, unbound form

   # Load documents for the list page
   documents = Document.objects.all()
   # Render list page with the documents and the form
   return render_to_response(
       'upload/list.html',
       {'documents': documents, 'form': form, 'test': test,},
       context_instance=RequestContext(request)
   )
