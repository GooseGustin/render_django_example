# Generated by Django 4.1.3 on 2024-03-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, to='core.tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('tech', 'Technology'), ('business', 'Business'), ('health and wellness', 'Health and Wellness'), ('travel', 'Travel'), ('food and clothing', 'Food and Clothing'), ('lifestyle', 'Lifestyle'), ('finance and investing', 'Finance and Investing'), ('education', 'Education'), ('faith', 'Faith'), ('entertainment', 'Entertainment'), ('environment and sustainability', 'Environment and Sustainability'), ('arts and culture', 'Arts and Culture')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
