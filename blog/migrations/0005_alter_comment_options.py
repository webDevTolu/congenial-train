# Generated by Django 4.1.4 on 2022-12-29 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_comment_blog_commen_created_0e6ed4_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]
