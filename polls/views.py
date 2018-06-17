from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello world in the polls app {0}".format(q.question_text))

def detail(request, question_id):
    return HttpResponse('Estas buscando la pregunta %s'%question_id)

def results(request, question_id):
    response = "Estas buscando los resultados de la pregunta %s"

    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s"%question_id)
