# Generated by Django 3.1.5 on 2021-01-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20210110_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='sections',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ArticleSection',
        ),
    ]