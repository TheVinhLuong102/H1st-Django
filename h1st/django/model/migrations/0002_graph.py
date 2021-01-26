# Generated by Django 3.1.5 on 2021-01-26 20:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import h1st.core.graph
import model_utils.fields
import uuid


class Migration(migrations.Migration):
    dependencies = \
        ('contenttypes', '0002_remove_content_type_name'), \
        ('H1stModel', '0001_initial')

    operations = \
        migrations.CreateModel(
            name='Graph',

            fields=[
                ('uuid',
                 models.UUIDField(
                    db_index=True,
                    default=uuid.uuid4,
                    editable=False,
                    help_text='UUID',
                    primary_key=True,
                    serialize=False,
                    unique=True,
                    verbose_name='UUID')),

                ('created',
                 model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),
                ('modified',
                 model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified')),

                ('polymorphic_ctype',
                 models.ForeignKey(
                    editable=False,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='polymorphic_h1stmodel.graph_set+',
                    to='contenttypes.contenttype'))
            ],

            options={
                'verbose_name': 'H1st Graph',
                'verbose_name_plural': 'H1st Graphs',
                'db_table': 'H1stModel_Graph',
                'ordering': ('-modified',),
                'permissions': (),
                'get_latest_by': 'modified',
                'abstract': False,
                'managed': True,
                'proxy': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'select_on_save': False,
                'default_related_name': 'h1st_graphs',
                'required_db_features': (),
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },

            bases=(models.Model,
                   h1st.core.graph.Graph)
        ),
