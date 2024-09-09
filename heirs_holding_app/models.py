from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Registration(models.Model):
	name= models.CharField(max_length=200)
	email= models.EmailField(null=True, max_length=200)
	phone_number= models.CharField(max_length=200)
	submitted_at= models.DateTimeField(auto_now_add=True)

	class Meta():
		ordering = ('-submitted_at',)

	def __str__(self):
		return f'Registration by {self.name} with {self.email} at {self.submitted_at}'