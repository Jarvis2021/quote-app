# Generated by Django 2.2 on 2020-05-03 22:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userquote', '0004_auto_20200503_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall_quote',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
