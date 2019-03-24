from django.shortcuts import render
from django.views import View


class HomePageViews(View):
    def get(self, request):

        return render(request, 'www/home.html', locals())

    def post(self, request):
        pass