from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    q= Question.objects.get(pk=1)

    return HttpResponse("Hello world in the polls app {0}".format(q.question_text))