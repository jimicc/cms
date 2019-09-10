# Generated by Django 2.2 on 2019-09-10 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0010_auto_20190910_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Full_Name', max_length=50)),
                ('slug', models.CharField(default='full-name', max_length=50)),
                ('position', models.CharField(default='Subtitle', max_length=200)),
                ('preamble', models.CharField(default='This_is_the_Preamble', max_length=200)),
                ('avaliable', models.CharField(default='Currently Avaliable', max_length=200)),
                ('relocate', models.CharField(default='Willing to relocate to: ', max_length=200)),
                ('cv_image', models.FileField(blank=True, default='cv-face.jpg', upload_to='')),
                ('email', models.CharField(default='email', max_length=50)),
                ('phone', models.CharField(default='phone', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cv_headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='headline', max_length=50)),
                ('date', models.CharField(default='headline', max_length=50)),
                ('title', models.CharField(default='title', max_length=50)),
                ('headline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Cv')),
            ],
        ),
        migrations.AlterField(
            model_name='website',
            name='link_2_tab_opt_1',
            field=models.CharField(default='title_tab_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='website',
            name='link_2_tab_opt_2',
            field=models.CharField(default='title_tab_2', max_length=20),
        ),
        migrations.CreateModel(
            name='Cv_list_element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_element', models.CharField(default='list_element', max_length=50)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Cv_headline')),
            ],
        ),
    ]
