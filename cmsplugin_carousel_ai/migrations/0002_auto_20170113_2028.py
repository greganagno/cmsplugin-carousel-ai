# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_carousel_ai', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='caption_line1',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='caption_line2',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='caption_line3',
        ),
        migrations.AddField(
            model_name='slide',
            name='slide_content',
            field=models.CharField(max_length=160, blank=True, verbose_name='slide content'),
        ),
        migrations.AddField(
            model_name='slide',
            name='slide_header',
            field=models.CharField(max_length=160, blank=True, verbose_name='slide header'),
        ),
        migrations.AddField(
            model_name='slide',
            name='slide_subheader',
            field=models.CharField(max_length=160, blank=True, verbose_name='slide subheader'),
        ),
        migrations.AddField(
            model_name='slide',
            name='template',
            field=models.CharField(default='default', max_length=255, verbose_name='Template', choices=[('default', 'Default')]),
        ),
    ]
