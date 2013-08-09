# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Village'
        db.create_table('coco_village', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('coco', ['Village'])

        # Adding model 'Person'
        db.create_table('coco_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('other_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('delivery_date', self.gf('django.db.models.fields.DateField')()),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Village'])),
        ))
        db.send_create_signal('coco', ['Person'])

        # Adding model 'Mediator'
        db.create_table('coco_mediator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('coco', ['Mediator'])

        # Adding M2M table for field villages on 'Mediator'
        db.create_table('coco_mediator_villages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediator', models.ForeignKey(orm['coco.mediator'], null=False)),
            ('village', models.ForeignKey(orm['coco.village'], null=False))
        ))
        db.create_unique('coco_mediator_villages', ['mediator_id', 'village_id'])

        # Adding model 'Video'
        db.create_table('coco_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('coco', ['Video'])

        # Adding model 'Dissemination'
        db.create_table('coco_dissemination', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Village'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Video'])),
            ('mediator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Mediator'])),
            ('song', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('game', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('total_households', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('total_new_households', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('total_pregnant_women', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('total_lactating_women', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('coco', ['Dissemination'])

        # Adding model 'Attendance'
        db.create_table('coco_attendance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Person'])),
            ('dissemination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Dissemination'])),
            ('question_asked', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('liked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('coco', ['Attendance'])


    def backwards(self, orm):
        # Deleting model 'Village'
        db.delete_table('coco_village')

        # Deleting model 'Person'
        db.delete_table('coco_person')

        # Deleting model 'Mediator'
        db.delete_table('coco_mediator')

        # Removing M2M table for field villages on 'Mediator'
        db.delete_table('coco_mediator_villages')

        # Deleting model 'Video'
        db.delete_table('coco_video')

        # Deleting model 'Dissemination'
        db.delete_table('coco_dissemination')

        # Deleting model 'Attendance'
        db.delete_table('coco_attendance')


    models = {
        'coco.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'dissemination': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Dissemination']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Person']"}),
            'question_asked': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'coco.dissemination': {
            'Meta': {'object_name': 'Dissemination'},
            'attendance_records': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coco.Person']", 'through': "orm['coco.Attendance']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Mediator']"}),
            'song': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'total_households': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'total_lactating_women': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'total_new_households': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'total_pregnant_women': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Video']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Village']"})
        },
        'coco.mediator': {
            'Meta': {'object_name': 'Mediator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'villages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coco.Village']", 'symmetrical': 'False'})
        },
        'coco.person': {
            'Meta': {'object_name': 'Person'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Village']"})
        },
        'coco.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coco.village': {
            'Meta': {'object_name': 'Village'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['coco']