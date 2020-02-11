from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Book, Author
from .serializers import BookSerializer


class BookView(APIView):
    def get(self, request):
        articles = Book.objects.all()
        authors = Author.objects.all()

        l = []
        for a in authors:

            print("--------------------------------------------------------------------------------")
            print(a.email)
            print(a.name)
            print(a.id)
            queryset = Book.objects.filter(
                author__email=a.email
            )
            # print(queryset)
            for i in queryset:
                print(i.title, i.description)
                d = {
                    'title': i.title,
                    'author': a.name,
                }
                l.append(d)
        return Response({"books": l})

    def post(self, request):
        title = request.data.get('title')
        name = request.data.get('author_name')
        author = Author.objects.get(name=name)
        print("-----", title)

        b = Book.objects.create(title=title, author=author)
        return Response({"message": "SUCCESS"})


    def put(self, request, pk):
        saved_article = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = BookSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid():
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

    def delete(self, request, pk):
        # Get object with this pk
        # print(self.args,self.kwargs)
        print(pk)
        # pk = request.data.get('pk')
        article = get_object_or_404(title=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)


from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        print(request.data)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key,"username":request.data['username']}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response({'message':'logout' },status=204)
