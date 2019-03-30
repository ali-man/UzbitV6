from django.urls import path

from www.views import AuthQuery, ArticleListViews

app_name = 'www'
urlpatterns = [
    # Auth routers
    path('login/', AuthQuery.login, name='login'),
    path('logout/', AuthQuery.logout, name='logout'),
    path('register/', AuthQuery.register, name='register'),
    # Articles routers
    path('articles/', ArticleListViews.as_view(), name='articles'),
]