from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
  is_admin=models.BooleanField('Is admin',default=False)
  is_candidate=models.BooleanField('Is candidate',default=False)
  is_recruiter=models.BooleanField('Is recruiter',default=False)


class Job(models.Model):
  position = models.CharField(max_length=100)
  company_name=models.CharField(max_length=100)
  description=models.TextField()
  details=models.TextField()


class Application(models.Model):
  STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Selected','Selected'),
    ('Rejected','Rejected'),
  )
  candidate = models.ForeignKey(User,on_delete=models.CASCADE)
  job = models.ForeignKey(Job,on_delete=models.CASCADE)
  phone = models.CharField(max_length=15)
  qualification = models.CharField(max_length=100)
  experience = models.CharField(max_length=100)
  skills = models.TextField()
  resume = models.FileField(upload_to='resume/')
  cover_letter = models.TextField()
  status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')
  applied_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"{self.candidate.username} - {self.job.position}"



class UserProfile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  phone = models.CharField(max_length=15)
  qualification = models.CharField(max_length=100)
  skills = models.TextField()
  
  profile_picture = models.ImageField(upload_to="profile_pictures/",blank=True,null=True)

  address = models.TextField(blank=True)

  def __str__(self):
    return self.user.username



class SavedJob(models.Model):
  candidate = models.ForeignKey(User,on_delete=models.CASCADE)
  job = models.ForeignKey(Job,on_delete=models.CASCADE)
  saved_date = models.DateTimeField(auto_now_add=True)
  class Meta:
    unique_together = ("candidate","job")

  def __str__(self):
    return f"{self.candidate.username} - {self.job.position}"

