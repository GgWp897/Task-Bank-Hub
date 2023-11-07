from django.db import models

class Users(models.Model):
    email=models.CharField('Email', max_length=30)
    password=models.CharField('Пароль', max_length=40)
    def __str__(self):
        return self.email
    
class Statement(models.Model):
    task=models.CharField('Задание', max_length=256)
    taskAll=models.TextField('Описание')
    date=models.DateField('Дата окончания')
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
        return self.task
