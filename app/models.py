from django.db import models

class detailformdata(models.Model):
	Name=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	class Meta:
		db_table="detailformdata"