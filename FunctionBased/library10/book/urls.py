from django.urls import path

from .views import BookView,LogoutView,LoginView



app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('all/', BookView.as_view()),
    # path('all/<int:pk>', BookView.as_view()),
    path('p/', BookView.as_view()),
    path('get/<int:pk>', BookView.as_view()),
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),
]