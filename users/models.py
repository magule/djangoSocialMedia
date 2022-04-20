from django.db import models
from django.contrib.auth.models import User
from PIL import Image #pillow thing to resize profile images

#GET the User well here! i guess yea its given from auth django 


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) #with user modele have a one to one relationship--- İF USER DELETED DELETE THE PROFILE
	image = models.ImageField(default='default.jpg', upload_to='profile-pics')


	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self, *args, **kwargs): #overriding bttw already exists creating our own so we can add some functinatliyty
		super(Profile, self).save(*args, **kwargs) # running the save methood of parent class

		img = Image.open(self.image.path)

		if img.height > 300 or img.width >300:
			output_size = (300,300) #max sizes
			img.thumbnail(output_size)
			img.save(self.image.path)  

