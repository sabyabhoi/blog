from django.db import models
from django.contrib.auth.models import User

from markdown_deux import markdown

STATUS = (
  (0, 'Draft'),
  (1, 'Publish')
)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now_add=True)

  content = models.TextField()
  description = models.TextField(blank=True) 
  image = models.ImageField(upload_to='images', blank=True)
  likes = models.IntegerField(default=0)

  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

  def get_markdown(self):
    content = self.content
    return markdown(content)

  def increment_likes(self):
    self.likes += 1

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=80)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)

class Newsletter(models.Model):
  email = models.EmailField()
  entered_on = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.email