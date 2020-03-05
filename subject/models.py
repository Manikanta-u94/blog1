from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class subject(models.Model):
	CHOICES = (
		('Django','Django'),
		('Python','Python'),
		('Java','Java'),
		('MYSQL','MYSQL'))
	course_name = MultiSelectField(choices = CHOICES)


