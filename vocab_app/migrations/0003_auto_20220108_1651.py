# Generated by Django 3.2.9 on 2022-01-08 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocab_app', '0002_question_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200)),
                ('questions_language', models.CharField(choices=[('en', 'English'), ('de', 'German'), ('cz', 'Czech'), ('es', 'Spanish')], default='en', max_length=200)),
                ('answer_language', models.CharField(choices=[('en', 'English'), ('de', 'German'), ('cz', 'Czech'), ('es', 'Spanish')], max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_language',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_language',
        ),
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
        migrations.AddField(
            model_name='question',
            name='set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set', to='vocab_app.questionset'),
        ),
    ]