# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django import forms
from ckeditor.widgets import CKEditorWidget



class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget()) 

    class Meta:
        # this is not automatically inherited from FlatpageFormOld
        model = FlatPage
        fields = ['id', 'title', 'content']


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
