# Generated by Django 3.2.9 on 2022-01-19 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('questions_language', models.CharField(choices=[('english', 'English'), ('german', 'German'), ('czech', 'Czech'), ('spanish', 'Spanish')], default='english', max_length=200)),
                ('answer_language', models.CharField(choices=[('english', 'English'), ('german', 'German'), ('czech', 'Czech'), ('spanish', 'Spanish')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('is_noun', models.BooleanField(default=True)),
                ('article', models.CharField(blank=True, max_length=200, null=True)),
                ('set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set', to='vocab_app.questionset')),
            ],
        ),
    ]