from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created =models.DateTimeField(auto_now_add=True) #auto_add any time field is created

    def __str__(self):
        return self.title + str(self.complete)

#run py manage.py makemigrations => py manage.py migrate, models then need to be registered in admin.py before they will appear