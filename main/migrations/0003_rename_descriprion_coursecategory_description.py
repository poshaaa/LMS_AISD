# Generated by Django 4.1.2 on 2022-11-23 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecategory',
            old_name='descriprion',
            new_name='description',
        ),
    ]