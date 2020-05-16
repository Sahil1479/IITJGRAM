from django.db import models

from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_media", blank=True, null=True)
    caption = models.TextField()
    
    created_date = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return str(self.author) + " " + str(self.created_date)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

class Postlink(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    link = models.URLField(max_length = 200, blank=True, null=True)
    caption = models.TextField(max_length = 1000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.author) + " " + str(self.created_date)

      

class Postvideo(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    video = models.FileField(upload_to='user_media', null=True, verbose_name="")
    caption = models.TextField(max_length = 1000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.author) + " " + str(self.created_date)

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args,**kwargs)

class Postdocument(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='user_media', null=True, verbose_name="")
    caption = models.TextField(max_length = 1000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.pdf)

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args,**kwargs)  

class Comment(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    comments = models.CharField(max_length=200,blank=True,null=True)
    id_p = models.IntegerField()
    def __str__(self):
        return str(self.comments) + " " + str(self.author)

class Profile(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    profileimage = models.ImageField(upload_to="user_media", blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    pro_id = models.IntegerField()
    branch = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    facebooklink = models.URLField(max_length = 200, blank=True, null=True)
    instagramlink = models.URLField(max_length = 200, blank=True, null=True)
    twitterlink = models.URLField(max_length = 200, blank=True, null=True)
    linkedinlink = models.URLField(max_length = 200, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    dob = models.TextField(blank=True, null=True)
    professional_skills = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return str(self.author)
