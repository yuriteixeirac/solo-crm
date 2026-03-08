from django.shortcuts import render


def tasks_board(request):
    return render(request, 'tasks/board.html')
