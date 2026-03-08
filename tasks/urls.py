from django.urls import path
from tasks.views import tasks_board



urlpatterns = [
    path('', tasks_board, name='board')
]
