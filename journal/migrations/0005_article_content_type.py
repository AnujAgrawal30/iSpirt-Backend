# Generated by Django 3.1.5 on 2021-01-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_auto_20210114_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_type',
            field=models.CharField(choices=[('HTML', 'HTML'), ('markdown', 'markdown')], default='markdown', max_length=50),
            preserve_default=False,
        ),
    ]