# Generated by Django 5.0.6 on 2024-06-14 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gato',
            name='castracao',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='gato',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='gatos/'),
        ),
        migrations.AlterField(
            model_name='gato',
            name='saude',
            field=models.TextField(),
        ),
    ]