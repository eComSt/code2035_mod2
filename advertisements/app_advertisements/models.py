from django.db import models

class Advertisement(models.Model):
    title = models.CharField("Заголовок",max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=20, decimal_places=2)
    auction = models.BooleanField("Торг", default=False,help_text="Отметьте если торг уместен")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    def __str__(self):
        return self.title