# Generated by Django 4.1.4 on 2023-01-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_rankinfo_rankpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
