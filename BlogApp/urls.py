from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('add_blog/', views.add_blog, name="add_blog"),
    path('blog_detail/<slug>', views.blog_detail, name="blog_detail"),
    path('see_blog/', views.see_blog, name="see_blog"),
    path('blog_delete/<id>', views.blog_delete, name="blog_delete"),
    path('blog_update/<slug>', views.blog_update, name="blog_update"),
    path('see_blog/', views.see_blog, name="see_blog"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('verify/<token>/', views.verify, name="verify"),
    path('liked_blog/<user>', views.liked_blog, name="liked_blog"),
    path('liked/', views.liked, name="liked"),
]
