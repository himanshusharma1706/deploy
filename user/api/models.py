from django.db import models

class profile(models.Model):
    name=models.CharField(max_length=20 , null=True)
    mobile_number=models.IntegerField(
        
    )
     