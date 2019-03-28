from django.contrib import admin

from www.models import Profile, Tags, CategoryOfArticles, Articles

admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(CategoryOfArticles)
admin.site.register(Articles)