from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=20)
    surname = models.CharField("Фамилия", max_length=15)
    birthday = models.DateField("Дата рождения")
    bio = models.TextField("Биография")
    desc = models.TextField("Жив или умер")

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]
        constraints = [
            models.UniqueConstraint(
                fields=("surname", "bio"),
                condition=models.Q(desc="Жив"),
                name = "unique_surname_bio"
            )
        ]

class Publisher(models.Model):
    name = models.CharField("Название", unique=True)

class Book(models.Model):
    title = models.CharField("Название", unique=True, blank=True)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_author = models.ManyToManyField(Author)