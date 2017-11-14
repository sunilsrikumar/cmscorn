# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from django.db import models as django_models
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from pagedown.widgets import AdminPagedownWidget

from ckeditor.widgets import CKEditorWidget
from . import models


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


class PostAdmin(admin.ModelAdmin):
    # Note: this makes pagedown the default editor for ALL text fields
    formfield_overrides = {
        django_models.TextField: {'widget': AdminPagedownWidget },
    }
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'post_date', 'posted_by',
                    'comment_count', 'allow_comments')
    readonly_fields = ('comment_count',)


class CommentAdmin(admin.ModelAdmin):
    # Note: this makes pagedown the default editor for ALL text fields
    formfield_overrides = {
        django_models.TextField: {'widget': AdminPagedownWidget },
    }
    list_display = ('user_name', 'user_email', 'ip_address', 'post_date')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)