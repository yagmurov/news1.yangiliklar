from django.urls import path
from .views import UserRegistrationsView,UserLoginView, LogoutView,UserUpdateView,PasswordResedView




app_name='accounts'
urlpatterns = [
    path('sign-up/', UserRegistrationsView.as_view(), name='sign-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path("logout", LogoutView.as_view(), name='logout'),
    path("userupdate", UserUpdateView.as_view(), name='userupdate'),
    path('passwordreset', PasswordResedView.as_view(), name="passwordreset")
    
    
]
