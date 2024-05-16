from django.db import models
from django.contrib.auth.models import User
# to make an image smaller size
from PIL import Image

# Create your models here.
class Profile(models.Model):
    # establishing a connection bw the User model and the Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile picture/image 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # done to modify something within the class
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # the image the user uploaded will be opened by the Image module from PIL
        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        