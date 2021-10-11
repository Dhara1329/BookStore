from django.db import models

# Create your models here.
class UserDetailsModel(models.Model):
	"""docstring for UserModel"""
	First_Name = models.CharField(max_length = 30)
	Last_Name = models.CharField(max_length = 30)
	Email = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 10)
	Contact_Number = models.IntegerField()
	Address = models.CharField(max_length = 100)
	Landmark = models.CharField(max_length = 20)
	City = models.CharField(max_length = 15)
	State = models.CharField(max_length = 15)
	Zip	= models.CharField(max_length = 10)

class BookDetailsModel(models.Model):
	"""docstring for BookDetailsModel"""
	Book_Name = models.CharField(max_length = 100)
	Book_Price = models.IntegerField()
	Standard = models.IntegerField()
	Book_Image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.Book_Name