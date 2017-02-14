# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('cms', '0002_auto_20170110_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, to='cms.CMSPlugin', related_name='cmsplugin_carousel_ai_carousel', auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=160)),
                ('interval', models.FloatField(verbose_name='slide changing time in seconds', default=5.0)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('caption_line1', models.CharField(verbose_name='slide caption line 1', blank=True, max_length=160)),
                ('caption_line2', models.CharField(verbose_name='slide caption line 2', blank=True, max_length=160)),
                ('caption_line3', models.CharField(verbose_name='slide caption line 3', blank=True, max_length=160)),
                ('url', models.URLField(verbose_name='link to URL', blank=True, max_length=250)),
                ('call_to_action_label', models.CharField(verbose_name='call to action label', blank=True, max_length=250)),
                ('ordering', models.IntegerField(verbose_name='ordering', db_index=True, default=0, help_text='Number which determines the order of slides in carousel. Smallest value first.')),
                ('carousel', models.ForeignKey(verbose_name='carousel', to='cmsplugin_carousel_ai.Carousel', related_name='slides')),
                ('image', filer.fields.image.FilerImageField(verbose_name='slide image', to='filer.Image')),
                ('linked_page', models.ForeignKey(verbose_name='link to page', null=True, to='cms.Page', blank=True, help_text='Page link overrides given URL.')),
            ],
            options={
                'ordering': ('ordering',),
            },
        ),
    ]
