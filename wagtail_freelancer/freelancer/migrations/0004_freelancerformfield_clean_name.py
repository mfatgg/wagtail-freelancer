# Generated by Django 2.2.19 on 2021-03-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0003_auto_20180905_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancerformfield',
            name='clean_name',
            field=models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name'),
        ),
    ]