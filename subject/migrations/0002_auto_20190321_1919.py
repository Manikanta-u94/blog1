# Generated by Django 2.1.7 on 2019-03-21 13:49

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='course_name',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('Python', 'Python'), ('Java', 'Java'), ('MYSQL', 'MYSQL')], max_length=24),
        ),
    ]
