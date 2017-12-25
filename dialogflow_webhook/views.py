#from django.shortcuts import render

# Create your views here.
import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import WebhookTransaction

@csrf_exempt
@require_POST
def webhook(request):

  jsondata = request.body
  data = json.loads(jsondata.decode('utf-8'))
  meta_inst = copy.copy(request.META)
  meta = {}
  for k, v in meta_inst.items():
    if isinstance(v, str):
      meta[k]=meta_inst[k]

  WebhookTransaction.objects.create(
    date_generated=data['timestamp'],
    body=data,
    request_meta=meta
  )

  return HttpResponse(status=200)
