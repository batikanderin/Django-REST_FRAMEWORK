# Generated by Django 4.0.2 on 2022-02-22 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitaplar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='yorum_sahibi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kullanici_yorumlari', to=settings.AUTH_USER_MODEL),
        ),
    ]
