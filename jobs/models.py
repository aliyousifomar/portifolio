from django.db import models

class Job (models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


    # This method will put the object's name/title on admin page!
    def __str__(self):
        return self.summary[:100]