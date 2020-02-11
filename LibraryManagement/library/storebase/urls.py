from django.urls import path
from .views import BooksSerializer
from .views import AuthorCreateApiView, AuthorListApiView, AuthorRetrieveApiView, AuthorUpdateApiView, \
    AuthorDestroyApiView, LoginView, LogoutView


urlpatterns = [
    # url(r'book', BooksSerializer.as_view(), name='book'),

    path(r'p', AuthorCreateApiView.as_view(), name='create'),
    path(r'g', AuthorListApiView.as_view(), name='get'),
    path(r'r/(?P<id>\d+)/$', AuthorRetrieveApiView.as_view(), name='retrieve'),
    path(r'u/(?P<id>\d+)/$', AuthorUpdateApiView.as_view(), name='update'),
    path(r'd/(?P<id>\d+)/$', AuthorDestroyApiView.as_view(), name='delete'),
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),
]
