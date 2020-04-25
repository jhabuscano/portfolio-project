from django.db import models

# Create A Blog models
#title
#pub_date
# body
# images

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')






# Add the Blog app to the setttings
#Create a migration
#Migrate
#Add to the admin