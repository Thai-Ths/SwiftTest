from rest_framework import viewsets, mixins
from .serializers import EmailSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

from .models import SendMail

class EmailViewSet(viewsets.ModelViewSet):
    queryset = SendMail.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        dict = request.data
        send_mail(
                dict['subject'],
                dict['body'],
                'thai.sutth@gmail.com',
                [dict['to']],
                fail_silently=False,
                )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)