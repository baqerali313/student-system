# Generated by Django 4.2.6 on 2023-10-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_remove_student__class_student_class_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
