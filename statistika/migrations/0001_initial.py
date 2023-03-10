# Generated by Django 4.1.6 on 2023-03-04 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assos_app', '0005_alter_ombor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveIntegerField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('umumi_suma', models.PositiveIntegerField()),
                ('tolov', models.PositiveIntegerField()),
                ('nasya', models.PositiveIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assos_app.client')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assos_app.mahsulot')),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assos_app.ombor')),
            ],
        ),
    ]
