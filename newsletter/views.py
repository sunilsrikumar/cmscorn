# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from .models import Subscribe
from .utils import SendSubscribeMail

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        email_qs = Subscribe.objects.filter(email_id = email)
        if email_qs.exists():
            data = {"status" : "404"}
            return JsonResponse(data)
        else:
            Subscribe.objects.create(email_id = email)
            SendSubscribeMail(email) # Send the Mail
    return HttpResponse("/")