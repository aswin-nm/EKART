from django.db import models

# Create your models here.
class products(models.Model):
    LIVE=0
    DELETE=1
    title=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    DELETE_CHOICES=((LIVE,'LIVE'),(DELETE,'DELETE'))
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title