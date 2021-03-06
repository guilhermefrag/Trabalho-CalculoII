# Generated by Django 4.0.4 on 2022-05-18 17:18

from django.db import migrations, models
import sympycharfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_x', sympycharfield.fields.SympyCharField(max_length=20)),
                ('g_x', sympycharfield.fields.SympyCharField(max_length=20)),
                ('area', models.FloatField()),
            ],
            options={
                'db_table': 'integral',
                'managed': False,
            },
        ),
    ]
