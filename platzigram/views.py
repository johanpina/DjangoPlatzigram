## este es el archivo de vistas que son las funciones a las que se dirigen las peticiones cuando se pone una URL

from django.http import HttpResponse

from datetime import datetime
import json 

def hello_world(request): # siempre debe ir el request
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'oh hi! current server time is {str(now)}')

def sort_integers(request):
    """ Return a JSON response with sorted integers."""
    numbers = sorted([int(x) for x in  request.GET['numbers'].split(',')])
    #print(request)
    #import pdb; pdb.set_trace()
    data = {
        'status' : 'ok',
        'numbers' : numbers,
        'message' : 'integers sorted succesfully'

    }
    return HttpResponse(json.dumps(data,indent=4),
                        content_type= 'application/json')


def say_hi(request,name, age):
    "Return a greeting"
    if age <12:
        message = f'sorry {name} you are not allowed here'
    else:
        message = f'Hello, {name}! welcome to platzigram'
    return HttpResponse(message)