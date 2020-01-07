# Generated by Django 3.0.2 on 2020-01-07 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('followed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_that_is_being_followed', to=settings.AUTH_USER_MODEL)),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_that_is_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]