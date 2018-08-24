from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import (MachineModel, MachinePart)
from app.serializers import (MachineModelSerializer, MachinePartSerializer)
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def list_all_models(request): 
    if request.method == "GET":
        all_models = MachineModel.objects.all()
        serializer = MachineModelSerializer(all_models, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def list_all_parts(request): 
    if request.method == "GET":
        all_parts = MachinePart.objects.all()
        serializer = MachinePartSerializer(all_parts, many=True)
        return JsonResponse(serializer.data, safe=False)
