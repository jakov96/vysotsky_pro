from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView

from landing.utils import email_notification, CsrfExemptSessionAuthentication


class FrontendTemplateView(View):
    def get(self, request):
        return render(request, 'index.html')


class FeedbackView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        name = request.data.get('name', '')
        phone = request.data.get('phone', '')

        if name and phone:
            email_notification(request.data)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})

