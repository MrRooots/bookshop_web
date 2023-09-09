# Generated by Django 4.2.4 on 2023-09-03 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=256)),
                ('description', models.TextField()),
                ('published_at', models.DateField()),
                ('page_number', models.PositiveSmallIntegerField()),
                ('published_count', models.PositiveIntegerField()),
                ('weight', models.FloatField()),
                ('slug', models.SlugField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('books', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='bookshop.book')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('books', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='bookshop.book')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('books', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='bookshop.book')),
            ],
        ),
    ]
