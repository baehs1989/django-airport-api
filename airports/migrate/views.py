from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

# from file.models import Document
# from airport.models import Airport

# from airports.airport.models import Airport
# from airports.file.models import Document

from airport.models import Airport
from file.models import Document

import os
from django.conf import settings

from .file_validations import airport_file_validations

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def list(request):
    # Render list page with the documents and the form
    all_files = Document.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(all_files, 10)


    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    print (files.start_index())
    print (files)

    return render(request, 'migrate/migrate.html', {'all_files': files})

def migrations(request):
    # Render list page with the documents and the form
    if request.method == 'POST' and request.POST.get("selected_file"):
        selected_file = request.POST.get("selected_file")
        file = Document.objects.filter(pk=selected_file).first()

        text = open(os.path.join(settings.MEDIA_ROOT, str(file)), 'rb')
        lines = text.readlines()
        text.close()

        success_count = 0
        failure_count = 0
        overwrite_count = 0

        for line in lines:
            airport,result = airport_file_validations(line)
            # print (airport, result)

            if result == 1:
                overwrite_count += 1
                airport.save()
            elif result == 2:
                success_count += 1
                airport.save()
            else:
                failure_count += 1

            # print (airport, result)
            # print (success_count, failure_count, overwrite_count)

        # line = airport_file_validations(text.readline())


        # while line != '':
        #     line, result = airport_file_validations(text.readline())

        # return HttpResponseRedirect(reverse('migrate:complete'))
        return render(request, 'migrate/complete.html', {"success":success_count, "fail":failure_count, "update":overwrite_count})
    else:
        print ("ERROR")
    return render(request, 'migrate/migrations.html', {})

def complete(request):
    return render(request, 'migrate/complete.html', {})