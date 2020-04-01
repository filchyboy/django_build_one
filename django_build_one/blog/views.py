from django.shortcuts import render

posts = [
    {
        'author': 'PersonA',
        'title': 'Post 1',
        'content': 'Content',
        'date_posted': 'March 31, 2020'
    },
    {
        'author': 'PersonB',
        'title': 'Post 2',
        'content': 'More Content',
        'date_posted': 'April 1, 2020'
    }
    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Django Enterprises'})