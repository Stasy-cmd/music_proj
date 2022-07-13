from django.db import models

from user.models import User


class Track(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    author = models.CharField(verbose_name="Исполнитель", max_length=50)
    release_date = models.DateField(verbose_name="Дата выхода", blank=True, null=True)
    genre = models.CharField(verbose_name="Жанр", max_length=50)
    duration_in_seconds = models.IntegerField(verbose_name="Длительность в секундах")
    album = models.CharField(verbose_name="Альбом", max_length=50)
    logo = models.ImageField(verbose_name="Обложка", null=True, blank=True)
    stared_user = models.ManyToManyField(User,
                                         related_name='favorite_tracks', blank=True)
    track_file = models.FileField(verbose_name='Файл', upload_to='music_files')

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(verbose_name="Название", max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Track)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
