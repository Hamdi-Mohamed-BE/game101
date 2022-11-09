# Generated by Django 3.2.6 on 2022-11-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='game',
            old_name='category',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='description',
            new_name='genre',
        ),
        migrations.RemoveField(
            model_name='game',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.RemoveField(
            model_name='game',
            name='label',
        ),
        migrations.RemoveField(
            model_name='game',
            name='name',
        ),
        migrations.RemoveField(
            model_name='game',
            name='price',
        ),
        migrations.RemoveField(
            model_name='game',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='game',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='game',
            name='play_time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(to='games.Platform'),
        ),
    ]
