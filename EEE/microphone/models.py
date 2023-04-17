from django.db import models

# Create your models here.
class tbl_Authentication(models.Model):
    Empcode = models.IntegerField()
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    is_active = models.IntegerField(null=True)
 
    def __str__(self):
        return self.username
 