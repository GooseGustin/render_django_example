# Generated by Django 4.1.3 on 2024-03-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('tech', 'Technology'), ('business', 'Business'), ('health and wellness', 'Health And Wellness'), ('travel', 'Travel'), ('food and clothing', 'Food And Clothing'), ('lifestyle', 'Lifestyle'), ('finance and investing', 'Finance And Investing'), ('education', 'Education'), ('faith', 'Faith'), ('entertainment', 'Entertainment'), ('environment and sustainability', 'Environment And Sustainability'), ('arts and culture', 'Arts And Culture')], default='', max_length=100),
        ),
    ]
