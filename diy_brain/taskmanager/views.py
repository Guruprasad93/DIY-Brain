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
        email_address = request.session['email_address']
        if(email_address!=''):
            context=None
        #     userID, name = getUserData(email_address)
        #     brainInfo = getBrainInfo(userID)
        #     if not brainInfo:
        #         brainInfo = None
        #     form_class = self.get_form_class()
        #     context = {
        #         'userID': userID,
        #         'name' : name,
        #         'brainInfo': brainInfo,
        #         'email_address': email_address,
        #         'form_class': form_class
        #     }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect("/login")

    
    # def post(self, request, *args, **kwargs):
    #     email_address = request.session['email_address']
    #     userID = getUserID(email_address)
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     # if(form.is_valid()):
    #     taskName = form.cleaned_data['taskName']
    #     taskDescription = form.cleaned_data['taskDescription']
    #     createTask(userID, taskName, taskDescription)
    #     return HttpResponseRedirect("/homepage")
       
        # else:
        #     context = {
        #         'form_class': form_class,
        #         'invalid': True,
        #         'message': 'Invalid form entry'
        #     }
        #     return render(request, self.template_name, context=context)
