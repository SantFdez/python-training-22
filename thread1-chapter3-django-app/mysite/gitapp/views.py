import json
from django.shortcuts import render
import requests
import ipdb


def index(request):

    r = requests.get('https://api.github.com/users/stackbuilders/repos')
    context = {'data': json.dumps(r.json(), indent=2)}
    ipdb.set_trace()
    return render(request, 'gitapp/index.html', context)
