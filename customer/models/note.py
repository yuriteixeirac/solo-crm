from django.db import models


class Note(models.Model):
    note = models.TextField()
    interaction = models.ForeignKey('Interaction', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'note on {self.interaction}: {self.note}'