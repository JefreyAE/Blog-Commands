# Generated by Django 3.0.5 on 2023-02-22 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='git',
            name='category',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='code',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='link',
        ),
        migrations.AddField(
            model_name='linux',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Topic'),
        ),
        migrations.DeleteModel(
            name='Docker',
        ),
        migrations.DeleteModel(
            name='Git',
        ),
    ]
