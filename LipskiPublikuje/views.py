from django.http import HttpResponseRedirect
from django.utils import timezone

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect

from LipskiPublikuje.models import Articles, Comments, AboutMe
from .forms import CommentForm, EditArticleForm


# Create your views here.

def article_list(request):
    articles = Articles.objects.all().order_by('-pub_date')
    latest_article = Articles.objects.all().order_by('-pub_date').first()
    three_articles = Articles.objects.all().order_by('-pub_date')[1:4]
    about_me = AboutMe.objects.first()
    is_admin = request.user.is_authenticated and request.user.is_superuser
    return render(request, 'index.html', {'articles': articles, 'latest_article': latest_article,
                                          'three_articles': three_articles, 'is_admin': is_admin, 'about_me': about_me})

def article_detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    is_admin = request.user.is_authenticated and request.user.is_superuser
    return render(request, 'article_detail.html', {'article': article, 'is_admin': is_admin})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('article_list')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('article_list')  # Przekieruj użytkownika na stronę główną po udanym zalogowaniu
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('article_list')

def article_detail(request, article_id):
    articles = Articles.objects.all().order_by('-pub_date')
    article = Articles.objects.get(pk=article_id)
    comments = article.comments.all()
    is_admin = request.user.is_authenticated and request.user.is_superuser
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = article
            comment.pub_date = timezone.now()
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'article_detail.html', {'article': article, 'articles': articles, 'form': form, 'comments': comments, 'is_admin': is_admin})
def delete_comment(request, comment_id):
    is_admin = request.user.is_authenticated and request.user.is_superuser
    if request.method == 'POST' and is_admin == True:
        comment = get_object_or_404(Comments, pk=comment_id)
        comment.delete()
    return redirect('article_detail', article_id=comment.article_id.pk)

def edit_article(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    articles = Articles.objects.all().order_by('-pub_date')
    if request.method == 'POST':
        form = EditArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/article/' + str(article.id))
    else:
        form = EditArticleForm(instance=article)

    return render(request, 'editarticle.html', {'form': form, 'article': article, 'articles': articles})
