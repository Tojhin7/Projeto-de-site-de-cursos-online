from django.urls import path
from accounts import views
from app_cursos.views import home, CursosListView, CursosCreateView, CursosUpdateView, CursosDeleteView, logout_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', home, name='home'),
    path('login/', views.login_view, name='login'),
    path('cursos/', CursosListView.as_view(), name='cursos_list'),
    path('create/', CursosCreateView.as_view(), name='cursos_create'),
    path('update/<int:pk>/', CursosUpdateView.as_view(), name='cursos_update'),
    path('delete/<int:pk>/', CursosDeleteView.as_view(), name='cursos_delete'),
    path('logout/', logout_view, name='logout'),
    ]
