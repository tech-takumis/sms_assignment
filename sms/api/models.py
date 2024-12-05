from django.db import models

from .utils import send_message

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"Name: {self.name} Phone number: {self.phone_number}, Age: {self.age}"
    
class Send_SMS(models.Model):
    to = models.CharField(max_length=50)
    message = models.TextField(max_length=250)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Send message to {self.to} body: {self.message}"
    
    def save(self,*args,**kwargs):
        if not self.pk:
            try:
                send_message(self.to,self.message)
            except ValueError as e:
                raise Exception(f"Failed to send  SMS:{e}")
        super().save(*args,**kwargs)