from django.db import models

# Create your models here.
class Post(models.Model):
	ticket_num = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	assign_to = models.CharField(max_length=20)
	details = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.subject