# Generated by Django 5.0.2 on 2024-08-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ysof_tagarticle',
            fields=[
                ('taid', models.BigAutoField(primary_key=True, serialize=False)),
                ('tadescri', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
