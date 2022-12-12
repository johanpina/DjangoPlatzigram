"""Post models"""


from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """post Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE) # Usamos la llave foranea al modelo user y el CASCADE es par que borre los registros de posts si se borra el usuario
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) ## Este es para enlazar el profile, es otra manera para no crear referencias circulares
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'