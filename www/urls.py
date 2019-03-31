from django.urls import path

from www.views import AuthQuery, ArticleListViews, ArticleDetailViews

app_name = 'articles'
urlpatterns = [
    # Auth routers
    path('login/', AuthQuery.login, name='login'),
    path('logout/', AuthQuery.logout, name='logout'),
    path('register/', AuthQuery.register, name='register'),
    # Articles routers
    path('articles/', ArticleListViews.as_view(), name='articles-list'),
    path('articles/<int:id>-<slug:slug>', ArticleDetailViews.as_view(), name='articles-detail'),
]