from django.db import models

class Druzyna(models.Model):

    nazwa = models.CharField(max_length=30)
    kraj = models.CharField(max_length=2)



    class Meta:
        ordering = ["nazwa"]
        verbose_name_plural = 'Drużyna'

    def __str__(self) -> str:
        return f"{self.nazwa} ({self.kraj})"