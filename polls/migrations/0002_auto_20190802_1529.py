# Generated by Django 2.2.4 on 2019-08-02 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quesion_text',
            new_name='question_text',
        ),
    ]