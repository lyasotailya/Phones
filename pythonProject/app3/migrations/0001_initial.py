# Generated by Django 5.0.1 on 2024-02-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('release_date', models.CharField(max_length=255)),
                ('lte_exists', models.BooleanField(blank=True)),
            ],
        ),
    ]
