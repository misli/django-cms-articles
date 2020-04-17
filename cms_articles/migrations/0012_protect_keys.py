# Generated by Django 2.2.11 on 2020-04-17 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms_articles', '0011_attribute_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tree',
            field=models.ForeignKey(help_text='The page the article is accessible at.', limit_choices_to={'application_urls': 'CMSArticlesApp', 'node__site_id': 1, 'publisher_is_draft': False}, on_delete=django.db.models.deletion.PROTECT, related_name='cms_articles', to='cms.Page', verbose_name='tree'),
        ),
        migrations.AlterField(
            model_name='title',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='image'),
        ),
    ]