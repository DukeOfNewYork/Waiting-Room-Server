from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Computer
from django.core import serializers
from django.utils import timezone
import json


# Create your views here.
@csrf_exempt
def input(request):
    computers = Computer.objects.all()
    if request.method == 'GET':
        data = {'JsonObject': 'Returned', 'Server': 'Connected'}
        data = json.dumps(data)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = request.body
        print(data)
        jsondata = json.loads(data)
        print(jsondata['computer'])
        if jsondata['computer']:
            try:
                computerobj = Computer.objects.get(name=jsondata['computer'])
            except Computer.DoesNotExist:
                computerobj = Computer(name=jsondata['computer'])
            computerobj.start_time = timezone.now()
            computerobj.save()

        return HttpResponse(json.dumps(serializers.serialize("json", [computerobj], )), content_type='application/json')


@csrf_exempt
def output(request):
    computers = Computer.objects.all()
    if request.method == 'GET':
        return HttpResponse(json.dumps(serializers.serialize("json", computers, )), content_type='application/json')
    else:
        data = request.body
        print(data)
        jsondata = json.loads(data)
        computerobj = Computer.objects.get(name=jsondata['computer'])
    return HttpResponse(json.dumps(serializers.serialize("json", [computerobj], )), content_type='application/json')


@csrf_exempt
def monitoring(request):
    computers = Computer.objects.all()
    print(computers)
    jsonlist = {}
    for computer in computers:
        print(computer.name)
        jsonlist[computer.name] = computer.status
    if request.method == 'GET':
        print(jsonlist)
        return JsonResponse(jsonlist, safe=False)


@csrf_exempt
def administration(request):
    computers = Computer.objects.all()
    print(computers)
    jsonlist = {}
    if request.method == 'GET':
        for computer in computers:
            print(computer.name)
            jsonlist[computer.name] = computer.status
        print(jsonlist)
        return render(request, 'index.html', {'jsonlist': jsonlist})
    if request.method == 'POST':
        jsondata = json.loads(request.body)
        try:
            computerid = jsondata['computer']
            computerstate = jsondata['state']
            computer = Computer.objects.get(name=computerid)
            if computerid:
                if computerstate == "RS":
                    computer.delete()
                else:
                    computer.status = computerstate
                    computer.save()
        except:
            print("nothing")
        return render(request, 'index.html')