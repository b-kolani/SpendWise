from django.conf import settings
from django.db import models

# Create your models here.
class   Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    icon = models.CharField(max_length=50, blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='categories',
        on_delete=models.CASCADE
    )

    class   Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                name='unique_category_per_user'
            )
        ]

    def __str__(self):
        return self.name