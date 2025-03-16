from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)  # Заголовок заметки
    content = models.TextField()             # Содержание заметки
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title