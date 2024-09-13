from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    LIVE=0
    DELETE=1
    name=models.CharField(max_length=50)
   
    address=models.TextField()
    user=models.OneToOneField(User,related_name='customer_profile',on_delete=models.CASCADE,null=True)
    phone=models.IntegerField(null=True)
    DELETE_CHOICES=((LIVE,'LIVE'),(DELETE,'DELETE'))
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name