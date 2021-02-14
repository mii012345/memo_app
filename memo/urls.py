from django.urls import path

from .import views

app_name = 'memo'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('insert/', views.insert, name="insert"),
    path('<int:memo_id>/edit/', views.edit, name="edit"),
    path('<int:memo_id>/delete/', views.delete, name="delete"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
]