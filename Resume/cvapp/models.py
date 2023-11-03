from django.db import models

# Create your models here.


class Skill_percentage(models.Model):
    Percentage=models.CharField(max_length=100,null=True)
    skill=models.CharField(max_length=100,null=True)
    p_bar=models.CharField(max_length=100,null=True)
    
class Education(models.Model):
    institute=models.CharField(max_length=100,null=True)
    education=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=100,null=True)
    desc=models.CharField(max_length=100,null=True)
    
class Experience(models.Model):
    institute=models.CharField(max_length=100,null=True)
    job_title=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=100,null=True)
    desc=models.CharField(max_length=100,null=True)