# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServerLog'
        db.create_table('log_serverlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('action', self.gf('django.db.models.fields.IntegerField')()),
            ('entry_table', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('log', ['ServerLog'])


    def backwards(self, orm):
        # Deleting model 'ServerLog'
        db.delete_table('log_serverlog')


    models = {
        'log.serverlog': {
            'Meta': {'object_name': 'ServerLog'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'entry_table': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'})
        }
    }

    complete_apps = ['log']