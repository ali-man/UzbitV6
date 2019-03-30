from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from pytils.translit import slugify

from www.forms import ArticleForm
from www.models import Tags, CategoryOfArticles, Articles


class HomePageViews(View):
    def get(self, request):
        form = ArticleForm()
        articles = Articles.objects.filter(status=2).order_by('-created_datetime')[:12]

        return render(request, 'www/home.html', locals())

    def post(self, request):
        owner = request.user
        title = request.POST['title']
        slug = slugify(request.POST['title'])
        category = request.POST['category']
        poster = request.FILES.get('poster', None)
        description = request.POST['description']
        tags = request.POST.getlist('tags[]', None)

        # Get Article
        get_category = CategoryOfArticles.objects.get(id=category)
        # Create Article
        create_article = Articles(
            owner=owner,
            title=title,
            slug=slug,
            category=get_category,
            description=description,
        )
        if poster is not None:
            create_article.poster = poster

        if request.user.is_staff:
            create_article.status = 2
            messages.success(request, 'Ваша статья успешно опубликована!')
        else:
            create_article.status = 0
            messages.success(request, 'Ваша статья успешно добавлена!')
            messages.warning(request, 'Ваша статья ожидает модерации')

        create_article.save()
        # Adding Tags for Article
        if tags is not None:
            for tag in tags:
                try:
                    _tag = Tags.objects.get(name=tag)
                    create_article.tags.add(_tag)
                except Tags.DoesNotExist:
                    _tag = Tags.objects.create(name=tag, slug=slugify(tag))
                    create_article.tags.add(_tag)

        return redirect('/')


class AuthQuery:

    @staticmethod
    def login(request):
        if request.method == 'GET':
            return redirect('/')

        if request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            if username is not None and password is not None:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'Вы успешно авторизовались!')
                        return redirect('/')
                    else:
                        messages.error(request, 'Ваш аккаунт заблокирован')
                        return redirect('/')
                else:
                    messages.error(request, 'Неверный логин или пароль')
                    return redirect('/')
            else:
                messages.error(request, 'Пустой логин или пароль')
                return redirect('/')
        else:
            messages.error(request, 'Неверный запрос')
            return redirect('/')

    @staticmethod
    def logout(request):
        logout(request)
        messages.info(request, 'Вы успешло разлогинились!')
        return redirect('/')

    @staticmethod
    def register(request):
        if request.method == "GET":
            return redirect('/')

        if request.method == "POST":
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)

            if (username and email and password1 and password2) is not None:
                try:
                    search_username = User.objects.get(username=username)
                except User.DoesNotExist:
                    search_username = None

                if search_username is None:
                    new_user = User.objects.create_user(username, email, password2)
                    new_user.save()
                    user = authenticate(username=username, password=password2)
                    login(request, user)

                    messages.success(request, 'Вы успешно зарегестрировались!')
                    messages.info(request, 'Вы авторизованы!')
                    return redirect('/')

                if search_username is not None:
                    messages.error(request, 'Пользователь с таким именем уже зарегестрирован')
                    return redirect('/')


class ArticleListViews(ListView):
    template_name = 'www/articles/list.html'
    # model = Articles
    queryset = Articles.objects.filter(status=2).order_by("-created_datetime")
    context_object_name = 'articles'
    paginate_by = 2