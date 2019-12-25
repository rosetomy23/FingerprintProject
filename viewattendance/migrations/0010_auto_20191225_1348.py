# Generated by Django 2.2.4 on 2019-12-25 08:18

from django.db import migrations, models
import django.db.models.deletion
import viewattendance.models


class Migration(migrations.Migration):

    dependencies = [
        ('viewattendance', '0009_auto_20191225_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='branch_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='viewattendance.Branch'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=viewattendance.models.get_image_path),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.CharField(default='subto', help_text='Teacher ID', max_length=20, unique=True, verbose_name='Teacher ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_name',
            field=models.CharField(default='kii', help_text='Name of the teacher', max_length=90, verbose_name='Teacher Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_id',
            field=models.CharField(default='pulu', help_text='Class ID', max_length=20, unique=True, verbose_name='Class ID'),
            preserve_default=False,
        ),
    ]
