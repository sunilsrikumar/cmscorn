# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
# from .models import FlatPage #Gives an error while adding more fields in model
from pagedown.widgets import AdminPagedownWidget

class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        # this is not automatically inherited from FlatpageFormOld
        model = FlatPage
        fields = ['id', 'content']

class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
