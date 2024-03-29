# Generated by Django 4.1.7 on 2023-03-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finpay', '0005_alter_user_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=20)),
                ('cvv', models.CharField(max_length=3)),
                ('cardtype', models.CharField(choices=[('V', 'verve'), ('M', 'mastercard'), ('vi', 'visa')], max_length=3)),
                ('expirydate', models.DateField()),
            ],
        ),
    ]
