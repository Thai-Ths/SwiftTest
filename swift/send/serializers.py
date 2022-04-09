from rest_framework import serializers

from .models import SendMail

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendMail
        fields = ['url', 'name', 'subject', 'to', 'body']