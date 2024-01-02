# Generated by Django 4.1.12 on 2024-01-02 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_businesstype_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='item',
            new_name='service',
        ),
        migrations.AddField(
            model_name='company',
            name='license_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_products', to='company.services')),
            ],
        ),
    ]
