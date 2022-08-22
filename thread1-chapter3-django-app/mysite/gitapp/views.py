import json
from django.shortcuts import render
import ipdb

from .api import GitApi


def index(request):

    response = GitApi.consume_git_api()
    context = {'data': json.dumps(response, indent=2)}
    # ipdb.set_trace()
    return render(request, 'gitapp/index.html', context)
