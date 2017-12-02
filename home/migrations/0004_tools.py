# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text=b'Name of Resource', max_length=255)),
                ('introduction', models.TextField(blank=True, help_text=b'Text to describe the page')),
                ('link', models.URLField(blank=True, help_text=b'url')),
                ('icon', models.ForeignKey(blank=True, default=b'https://image.flaticon.com/icons/svg/25/25284.svg', help_text=b'icon for your link.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]