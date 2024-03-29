# Generated by Django 4.2.3 on 2023-07-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='bars',
            field=models.ManyToManyField(related_name='drinks', to='drinks.bar'),
        ),
    ]
