from django.urls import path
from .views import userLogin,signUp

urlpatterns = [
    path('login/', userLogin.as_view(), name='login'),
    # path('logout/', userLogout.as_view(), name='logout'),
    path('signup/', signUp.as_view(), name='signup'),
]
