from django.shortcuts import render, redirect
from sounds.models import Post, AudioMessages
from sounds.forms import  SubForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from . forms import Subme
from django.contrib import messages
from django.db.models import Q

def index(request):
    post = Post.objects.all()[:6]
    audio = AudioMessages.objects.all()[:6]
    if request.method == 'POST': 
        sub_form = Subme(request.POST )
        if sub_form.is_valid():    
            sub = sub_form.save(commit=False)
            sub.save()
            messages.success(request, 'Thanks for subscribing')
            return redirect('index')           
    else:        
        sub_form = Subme()
    context = {
        'title': 'Recent Posts',
        'post': post,
        'audio': audio,
        'sub_form': sub_form
    }
    return render(request, 'sounds/index.html', context)


def about(request):
    return render(request, 'sounds/about.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "sounds/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class PostListView(generic.ListView):
    model = Post
    paginate_by = 1

class PostDetailView(generic.DetailView):
    model = Post

class AudioListView(generic.ListView):
    model = AudioMessages
    template_name = 'sounds/audio.html'
    paginate_by = 12


def resources(request):
    post = Post.objects.all()[:7]
    context = {
        'post': post,
    }
    return render(request, 'sounds/resources.html', context)

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) )

    return render(request, 'sounds/searchme.html', {'results': results})