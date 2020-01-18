# Generated by Django 2.2.4 on 2019-12-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewattendance', '0011_auto_20191225_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(help_text='Name of the course', max_length=90, verbose_name='Course Name'),
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='viewattendance.Classroom')),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='viewattendance.Course')),
                ('teacher_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='viewattendance.Teacher')),
            ],
        ),
    ]