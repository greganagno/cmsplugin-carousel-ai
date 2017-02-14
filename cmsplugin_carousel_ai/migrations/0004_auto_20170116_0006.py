# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_carousel_ai', '0003_auto_20170115_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='template',
        ),
        migrations.AddField(
            model_name='carousel',
            name='template',
            field=models.CharField(max_length=255, choices=[('carousel.html', 'Default'), ('intro_slider.html', 'Intro template'), ('image_gallery.html', 'Image template'), ('clients.html', 'Clients template')], default='carousel.html', verbose_name='Template'),
        ),
    ]
