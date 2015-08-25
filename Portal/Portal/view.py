# portal/views.py

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings

import json
from pprint import pprint
import SoftLayer
import requests

def home(request):
    return render(request, ['api_and_function.html']);

def device(request):
    return render(request,['api_and_function.html'])

def network(request):
    return render(request, ['api_and_function.html'])