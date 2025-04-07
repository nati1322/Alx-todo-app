from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('todos/<int:pk>/complete/', views.TodoViewSet.as_view({'put': 'mark_as_complete'}), name='todo-complete'),
    path('todos/<int:pk>/incomplete/', views.TodoViewSet.as_view({'put': 'mark_as_incomplete'}), name='todo-incomplete'),
]