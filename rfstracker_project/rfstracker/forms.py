from django import forms
from rfstracker import models

class Salesdbform(forms.ModelForm):

    class Meta():
        model = models.Salesdb
        fields = '__all__'


class Detailsdbform(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)
    #rfsnumber = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta():
        model = models.Detailsdb
        fields = '__all__'
