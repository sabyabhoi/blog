from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Newsletter
from .forms import CommentForm, NewsletterForm
from django.shortcuts import render, get_object_or_404

class PostList(generic.ListView): 
  queryset = Post.objects.filter(status=1).order_by('-created_on') 
  template_name = 'index.html'

def post_detail(request, slug):
  template_name = 'post_detail.html'
  post = get_object_or_404(Post, slug=slug)

  comments = post.comments.filter()
  new_comment = None

  if request.method == 'POST': # Check if the user is POSTing a comment 
    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
      new_comment = comment_form.save(commit=False) # Retrieve the comment but don't save it to the database yet
      new_comment.post = post 

      if not post.comments.filter(body=new_comment.body).exists(): # Check if the comment already exists
        new_comment.save() # Save the comment to database if it doesn't exist

  else: # If the user isn't posting a comment, then just display the comment form
    comment_form = CommentForm()

  return render(request, template_name, {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

def base(request):
  template_name = 'base.html'

  if request.method == 'POST': 
    newsletter_form = NewsletterForm(data = request.POST)
    if newsletter_form.is_valid():
      email = newsletter_form.save(commit=False)
  else: 
    newsletter_form = NewsletterForm()
  return render(request, template_name, {'form': newsletter_form})

def about(request):
  template_name = 'about.html'
  return render(request, template_name)