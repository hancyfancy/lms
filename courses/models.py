from django.contrib.auth.models import User
from django.db import models
from db import models as mi_models

MEDIA_CHOICES = (
		('VID', 'Video'),
		('AUD', 'Audio'),
		('PIC', 'Picture'),
		('DOC', 'Document'),		
		('XLS', 'Excel'),
		('PPT', 'Powerpoint'),
		('GFORM', 'Google form'),
		('GDOC', 'Google document'),
		)

class Course(models.Model):
	title = models.CharField(max_length=255, unique=True)
	description = models.TextField()
	pass_grade = mi_models.DecimalRangeField(max_digits=5, decimal_places=2, min_value=0, max_value=100, default=50)
	def __str__(self):
		return self.title
	class Meta:
		db_table = 'mangalyacore_courses'
	
class Material(models.Model):
	title = models.CharField(max_length=255, unique=True)
	def __str__(self):
		return self.title
	class Meta:
		db_table = 'mangalyacore_materials'

class Content(models.Model):
	material = models.ForeignKey(Material, on_delete=models.CASCADE)
	label = models.CharField(max_length=255)
	url = models.TextField()
	type = models.CharField(max_length=255, choices=MEDIA_CHOICES, default='DOC')
	def __str__(self):
		return self.label
	class Meta:
		db_table = 'mangalyacore_material_content'

class UserCourseMaterial(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	material = models.ForeignKey(Material, on_delete=models.CASCADE)
	grade = mi_models.DecimalRangeField(max_digits=5, decimal_places=2, min_value=0, max_value=1, default=0)
	def __str__(self):
		return self.user.username + ' enrolled in ' + self.course.title
	class Meta:
		db_table = 'mangalyacore_user_course_material'
	
