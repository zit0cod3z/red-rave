# Generated by Django 4.2.2 on 2024-09-09 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heirs_holding_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ('-submitted_at',)},
        ),
    ]