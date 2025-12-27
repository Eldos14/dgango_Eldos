from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('test_python/', views.test_python, name='test_python'),
    path('course/<int:course_id>/', views.course_page, name='course_page'),

]
 


