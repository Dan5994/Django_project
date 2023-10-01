from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.get_post, name="posts"),
    path('create/', views.create_post, name='create'),
    path('main/<int:_id>', views.one_post, name='one_post'),
    path('delete/<int:_id>', views.post_delete, name='delete'),
    path('update/<int:_id>', views.post_update, name='update'),
    path('check/<int:counter>', views.check_if_exist, name = 'check'),
    path('get_create', views.get_or_create)
]