from re import template
from django.db.models import fields
from django.shortcuts import render, resolve_url, get_object_or_404
from django.urls.base import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, request
from .models import Category, Post, Contact
from .forms import EditPost, PostForm, ContactForm


# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def home(request):
    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        cat_menu = Category.objects.all()
        post_footer = Post.objects.all()[0:3]
        
        context['cat_menu'] = cat_menu  
        context['post_footer'] = post_footer
        return context

def CategoryView(request, cats):
    #category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    #return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts})
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        cat_menu = Category.objects.all()
        post_footer = Post.objects.all()[0:3]
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True    
            
        context['post_footer'] = post_footer
        context['cat_menu'] = cat_menu  
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPost
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

class ContactView(ListView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
 
    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        post_footer = Post.objects.all()[0:3]
        context['form'] = self.form_class
        context['post_footer'] = post_footer
        return context