# Generated by Django 2.2.1 on 2019-06-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0003_member_chi_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
