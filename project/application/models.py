from django.db import models

class Profile(models.Model):
    telegram_id = models.IntegerField(verbose_name='telegram id')
    full_name = models.CharField(max_length=255, verbose_name='Полное имя пользователя')
    user_name = models.CharField(max_length=255, verbose_name='Имя пользователя')

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Word(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    word = models.CharField(max_length=255, verbose_name='Cлово')
    translated_word = models.CharField(max_length=255, verbose_name='Переведенное слово')
    translated_language = models.CharField(max_length=255, verbose_name='C языка')
    translated_to_language = models.CharField(max_length=255, verbose_name='Переведен на')

    def __str__(self):
        return str(self.profile)

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'




