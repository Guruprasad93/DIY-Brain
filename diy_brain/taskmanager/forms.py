from django import forms

class BrainArchitectureForm(forms.Form):
    layers = forms.IntegerField(label = 'Number of layers')
    neurons = forms.IntegerField(label = 'Number of neurons in each layer')
    inputs = forms.IntegerField(label = 'Number of input units')
    outputs = forms.IntegerField(label = 'Number of output units')