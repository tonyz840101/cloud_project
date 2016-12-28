from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def Index(request):
    return render(request,'another/index.html')

def Upload(request):
    file = request.FILES.get('file','')
    exist=models.Table.objects.filter(filename=file.name)
    if(exist.__len__()):
        exist[0].file.storage.delete(exist[0].file.path)
        exist[0].delete()
    table = models.Table.objects.create(filename=file.name,file=file)
    table.save()
    return render(request, 'another/index.html',{'message':'OK',})

def Download(request):
    filename =  models.Table.objects.filter(txt=request.GET['file'])[0]
    response = HttpResponse(filename.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % (str(filename).split('/')[-1])
    return response


def Table(request):
    return render(request,'another/table.html',{'table':models.Table.objects.all(),})