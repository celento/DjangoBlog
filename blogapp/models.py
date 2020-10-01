from django.db import models

# Compare each class to a Table 
class Post(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=30)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

#Used to return String values from the Post objects
    def __str__(self):
        return self.title
