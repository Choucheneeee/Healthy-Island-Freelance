# Generated by Django 4.2.4 on 2024-06-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('island', '0006_alter_plat_ingridients'),
    ]

    operations = [
        migrations.AddField(
            model_name='plat',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]