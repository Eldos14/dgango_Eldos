from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    complated = models.BooleanField (default=False)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField(default="")
    img = models.URLField(default="")
    

    def __str__(self):
        return self.title
