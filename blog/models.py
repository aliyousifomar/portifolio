from django.db import models

class Blog (models.Model):

    #create blog model
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    #make a method that will put the blog title in admin page
    def __str__(self):
        return self.title

    #make a summary method to bring only certain portion of the body
    def summary (self):
        return self.body[:10]

    # make a custom date field
    def pub_date_pretty(self):
        return self.pub_date.strftime('%a %B %d %Y')