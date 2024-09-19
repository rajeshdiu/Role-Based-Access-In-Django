from django.db import models

class imageGallerymodel(models.Model):
    Image=models.ImageField(upload_to='Media/dog_img',null=True)
    dog_type=models.CharField(max_length=100,null=True)
    dog_name=models.CharField(max_length=100,null=True)
    dog_age=models.PositiveIntegerField(null=True)
    dog_details=models.TextField(max_length=10000,null=True)
