from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    SELECT=(
        ('dni','dni'),
        ('pass.','pasaporte'),
        ('Tr.mil','tarjeta militar'),
    )
    user=models.OneToOneField(User)
    documento=models.CharField(max_length=6, choices=SELECT)
    numero_doc=models.CharField(max_length=8)
    departamento=models.CharField(max_length=20)
    distrito =models.CharField(max_length=20)
    provincia =models.CharField(max_length=20)
    class Meta:
        permissions=(
            ('create','puede crear'),
            ('list','listar'),
            ('view','puede ver'),
            ('update','puede actualizar'),
            ('delete','puede eliminar'),
        )

    def __unicode__(self):
        return self.user.username

