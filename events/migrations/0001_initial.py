# Generated by Django 4.2 on 2023-04-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_active', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('prize', models.TextField()),
                ('guidelines', models.TextField()),
                ('konf_hub_url', models.TextField()),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
