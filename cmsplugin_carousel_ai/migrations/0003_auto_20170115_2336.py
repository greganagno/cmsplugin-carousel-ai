# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_carousel_ai', '0002_auto_20170113_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='slide_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='slide_header',
            new_name='header',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='slide_subheader',
            new_name='subheader',
        ),
    ]
