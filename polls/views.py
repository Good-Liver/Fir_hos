from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from .models import Sawal, Chuus

def index(request):
    latest_question_list = sawal.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
   # return HttpResponse(template.render(context, request))
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.Sana <3")

def detail(request, question_id):
    try:
        question = Sawal.objects.get(pk=question_id)
    except Sawal.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # response = "Fuck"
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.Chuss_set.get(pk=request.POST['choice'])
    except (KeyError, Chuus.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)