import json
import uuid

from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View

from .models import ShortLink

class GenerateShortLink(View):
    def post(self, request):
        data = json.loads(request.body)

        shortLink = ShortLink.objects.create(
            origin=data.get('origin'),
            hash=str(uuid.uuid4()).split('-')[0]
        )

        return JsonResponse({
            'success': True,
            'message': 'Link shortened successfully!',
            'origin': data.get('origin'),
            'short': shortLink.hash
        })

class GoToShortLink(View):
    def get(self, request, hash):
        try:
            shortLink = ShortLink.objects.get(hash=hash)

            return redirect(shortLink.origin)
        except:
            return redirect('/rejected/')
