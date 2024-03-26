
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static

from . import views
from .views import article_list, article_detail, edit_article
from django.conf import settings

urlpatterns = [
        path('', article_list, name='article_list'),
        path('article/<int:article_id>/', article_detail, name='article_detail'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout_view'),
        path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
        path('edit/<int:article_id>', edit_article, name='edit_article')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)