# Generated by Django 4.2.3 on 2023-09-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combined_Weave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.IntegerField()),
                ('image_array', models.JSONField(default=[[1]])),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_img', models.ImageField(upload_to='designs/')),
                ('d_height', models.IntegerField(null=True)),
                ('d_width', models.IntegerField(null=True)),
                ('used_colors', models.JSONField(null=True)),
                ('content_list', models.JSONField(null=True)),
                ('weft_seq', models.TextField(null=True)),
                ('warp_seq', models.TextField(null=True)),
                ('weft_rolls', models.JSONField(null=True)),
                ('warp_rolls', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images_Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='weaves/')),
                ('cat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Simple_Weave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weave_image', models.ImageField(upload_to='weaves/')),
                ('dm', models.JSONField()),
                ('weave_list', models.JSONField(default=[[1]])),
                ('combined_w', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.combined_weave')),
            ],
        ),
        migrations.AddField(
            model_name='combined_weave',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.design'),
        ),
    ]