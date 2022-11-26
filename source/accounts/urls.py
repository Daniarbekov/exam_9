from django.urls import path
from accounts.views import RegisterView, LoginView, logout_view, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('account/<int:pk>', UserView.as_view(), name='user_detail'),
]
