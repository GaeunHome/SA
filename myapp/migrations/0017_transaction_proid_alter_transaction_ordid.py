# Generated by Django 4.1.4 on 2023-01-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_product_productimage2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='PROID',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ORDID',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
