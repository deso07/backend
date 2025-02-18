from django.db import models

class Todolist(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title