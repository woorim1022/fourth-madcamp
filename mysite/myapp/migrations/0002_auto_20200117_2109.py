# Generated by Django 2.2.5 on 2020-01-17 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='body',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='letter',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Letter')),
            ],
        ),
    ]
