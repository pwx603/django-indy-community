# Generated by Django 2.1.7 on 2019-03-19 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indy_community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indycredentialdefinition',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indycreddef_set', to='indy_community.IndyWallet', to_field='wallet_name'),
        ),
        migrations.AlterField(
            model_name='indyorgrelationship',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indyrelationship_set', to='indy_community.IndyOrganization'),
        ),
        migrations.AlterField(
            model_name='indyorgrelationship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indyrelationship_set', to='indy_community.IndyUser'),
        ),
    ]
