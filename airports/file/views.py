from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document
from .forms import DocumentForm

import os
from django.conf import settings

from django.views import generic

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            print (newdoc.filename())
            # print (newdoc)
            # print (os.path.join(settings.MEDIA_ROOT, str(newdoc)))
            # text = open(os.path.join(settings.MEDIA_ROOT, str(newdoc)), 'rb')
            # line = text.readline().decode('utf-8')
            # while line != '':
            #     line = text.readline().decode('utf-8')
            #     info = str(line).split(',')
            #     print (info)
            # text.close()

            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('file:upload'))
            return render(request, 'file/success.html', {"file":newdoc})
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    # return render(request, 'file/list.html', {'documents': documents, 'form': form})
    return render(request, 'file/upload.html', {'documents': documents, 'form': form})


def success(request):
    return render(request, 'file/success.html', {})


class FileList(generic.ListView):
    model = Document
    template_name = 'file/file_list.html'
    context_object_name = 'file_list'