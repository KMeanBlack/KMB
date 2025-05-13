from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Notes(models.Model):
    notes_id=models.AutoField
    notes_name=models.CharField(max_length=300)
    branch= models.CharField(max_length=50, default="")
    subject= models.CharField(max_length=50, default="")
    notesfile = models.FileField(null=True)
    description=RichTextField(null=True)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="education/images",default="")

    def __str__(self):
        return self.branch  + " -- " +  self.subject