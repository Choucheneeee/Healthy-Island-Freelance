# Generated by Django 4.2.4 on 2024-06-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('island', '0005_alter_plat_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plat',
            name='ingridients',
            field=models.CharField(blank=True, max_length=380, null=True),
        ),
    ]