# Generated by Django 2.2.6 on 2019-11-03 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TShirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_TShirts', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('link_TShirts', models.CharField(max_length=512)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=64)),
                ('id_ts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.TShirts')),
            ],
        ),
    ]
