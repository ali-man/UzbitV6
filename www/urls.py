from django.urls import path

from www.views import AjaxQuery

app_name = 'ajax'
urlpatterns = [
    path('login/', AjaxQuery.login, name='login'),
]