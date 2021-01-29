from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import BrainArchitectureForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class TaskView(FormView):
    form_class = BrainArchitectureForm
    template_name = 'task.html'

    def get(self, request, *args, **kwargs):
        brain_id = request.GET.get('brain_id')
        if(brain_id!=''):
            context={
                'brain_id': brain_id
            }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect("/login")