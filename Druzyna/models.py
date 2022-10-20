from django.db import models

class Druzyna(models.Model):

    nazwa = models.CharField(max_length=30)
    kraj = models.CharField(max_length=2)



    class Meta:
        ordering = ["nazwa"]

        verbose_name = 'test'
        verbose_name_plural = 'twst2'

    def __str__(self) -> str:
        return f"{self.nazwa} ({self.kraj})"