# Generated by Django 3.2.6 on 2021-08-29 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_attachment_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notice',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
    ]
