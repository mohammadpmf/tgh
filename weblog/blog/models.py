from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    
    def __str__(self):
        return f"{self.title} {self.author}"

class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    c_p = models.ForeignKey('blog.post', on_delete=models.CASCADE, null=True, blank=True)
    