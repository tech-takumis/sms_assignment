from rest_framework import serializers
from .models import User, Send_SMS
from phonenumbers import parse,is_valid_number,format_number,PhoneNumberFormat
import phonenumbers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Send_SMS
        fields = '__all__'

    def validate_to(self,value):
        try:
            parse_number = phonenumbers.parse(value,None)

            if not is_valid_number(parse_number):
                raise serializers.ValidationError("Invalid phone number format.")
            return format_number(parse_number,PhoneNumberFormat.E164) 

        except phonenumbers.NumberParseException:
            raise serializers.ValidationError('Invalid phone number')