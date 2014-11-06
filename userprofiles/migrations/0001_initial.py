# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.CharField(max_length=6, choices=[(b'dni', b'dni'), (b'pass.', b'pasaporte'), (b'Tr.mil', b'tarjeta militar')])),
                ('numero_doc', models.CharField(max_length=8)),
                ('departamento', models.CharField(max_length=20)),
                ('distrito', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
