from django.db import models

# Create your models here.

JOP_TYPE = (
    ('Full Time' , 'Full Time'),
    ('Part Time' , 'Part Time'),
)

class Job(models.Model):
    title = models.CharField(max_length = 100)
    jop_type = models.CharField(max_length = 10 , choices = JOP_TYPE)
    description = models.TextField(max_length = 1000)
    published_at = models.DateTimeField(auto_now = True)
    salary = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 0)    
    vacancy = models.IntegerField(default = 1)
    category = models.ForeignKey('Category' , on_delete= models.CASCADE)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


