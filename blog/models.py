from django.db import models

# title, publication date, body, image

class Blog(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return(self.title)
    def summary(self):
        return self.body[:100] + '...'
    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
