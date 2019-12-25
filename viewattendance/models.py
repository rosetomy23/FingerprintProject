from django.db import models
from django.db.models import ImageField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import os


def get_image_path(instance, filename):
    return os.path.join('FingerprintProject', str(instance.id), filename)


class Branch(models.Model):
    class Meta:
        verbose_name_plural = "Branches"
    branch_name = models.CharField(max_length=30, null=False, unique=True, verbose_name="Branch Name",
                                  help_text="Branch name")

    def __str__(self):
        return self.branch_name


class Classroom(models.Model):
    class_id = models.CharField(max_length=20, null=False, unique=True, verbose_name="Class ID",
                                  help_text="Class ID")
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.class_id


class Student(models.Model):
    student_id = models.CharField(max_length=20, null=False, unique=True, verbose_name="Student ID", help_text="Student ID")
    student_name = models.CharField(max_length=90, null=False, verbose_name="Student Name", help_text="Name of the student")
    class_id = models.ForeignKey(Classroom, on_delete=models.CASCADE, default=1)
    profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.student_id

# fingerprint,class


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, null=False, unique=True, verbose_name="Teacher ID",
                                  help_text="Teacher ID")
    teacher_name = models.CharField(max_length=90, null=False, verbose_name="Teacher Name",
                                    help_text="Name of the teacher")
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, default=1)
    profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.teacher_id

# class+subject


class Course(models.Model):
    course_id = models.CharField(max_length=20, null=False, unique=True, verbose_name="Course ID",
                                  help_text="Course ID")
    course_name = models.CharField(max_length=90, null=False, verbose_name="Course Name",
                                    help_text="Name of the course")
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.course_id
