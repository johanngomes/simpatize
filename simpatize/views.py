import json

from django.http import HttpResponse
from django.template import loader

from src.QueryHelper import QueryHelper


def index(request):
    template = loader.get_template('templates/index.html')
    return HttpResponse(template.render())


def result(request):
    QueryHelper.identify_query(request.GET)

    data = {"foo": "bar", "hello": "world"}
    return HttpResponse(json.dumps(data), content_type="application/json")
