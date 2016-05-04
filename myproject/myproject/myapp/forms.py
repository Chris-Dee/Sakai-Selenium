# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    titleField = forms.CharField(
        #initial="name of test to be run"
    )
    docfile = forms.FileField(
        label='Select a file'
    )

class SiteForm(forms.Form):
    urlField = forms.CharField(
        
    )
