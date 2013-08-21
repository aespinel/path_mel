# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Adoption'
        db.create_table('coco_adoption', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Person'])),
            ('mediator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coco.Mediator'])),
            ('delivery_date', self.gf('django.db.models.fields.DateField')()),
            ('date_of_visit', self.gf('django.db.models.fields.DateField')()),
            ('checked_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('preparation_of_last_delivery', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cord_care', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cord_cut', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('baby_bathe', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('wiped', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('baby_wrap', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('baby_hold', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('baby_colostrums', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('breastfeed', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('feed', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('other_food', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('liquids', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('family_planning', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fp_method', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fp_awareness', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fp_service_providers', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fp_family_discussion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fp_family_member', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fp_use', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('coco', ['Adoption'])


        # Changing field 'Dissemination.total_pregnant_women'
        db.alter_column('coco_dissemination', 'total_pregnant_women', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Dissemination.total_lactating_women'
        db.alter_column('coco_dissemination', 'total_lactating_women', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Dissemination.total_households'
        db.alter_column('coco_dissemination', 'total_households', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Dissemination.total_new_households'
        db.alter_column('coco_dissemination', 'total_new_households', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))
        # Adding unique constraint on 'Dissemination', fields ['date', 'start_time', 'village', 'end_time', 'mediator']
        db.create_unique('coco_dissemination', ['date', 'start_time', 'village_id', 'end_time', 'mediator_id'])

        # Adding unique constraint on 'Video', fields ['title']
        db.create_unique('coco_video', ['title'])


        # Changing field 'Person.delivery_date'
        db.alter_column('coco_person', 'delivery_date', self.gf('django.db.models.fields.DateField')(null=True))
        # Adding unique constraint on 'Mediator', fields ['name']
        db.create_unique('coco_mediator', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Mediator', fields ['name']
        db.delete_unique('coco_mediator', ['name'])

        # Removing unique constraint on 'Video', fields ['title']
        db.delete_unique('coco_video', ['title'])

        # Removing unique constraint on 'Dissemination', fields ['date', 'start_time', 'village', 'end_time', 'mediator']
        db.delete_unique('coco_dissemination', ['date', 'start_time', 'village_id', 'end_time', 'mediator_id'])

        # Deleting model 'Adoption'
        db.delete_table('coco_adoption')


        # Changing field 'Dissemination.total_pregnant_women'
        db.alter_column('coco_dissemination', 'total_pregnant_women', self.gf('django.db.models.fields.PositiveIntegerField')(default=False))

        # Changing field 'Dissemination.total_lactating_women'
        db.alter_column('coco_dissemination', 'total_lactating_women', self.gf('django.db.models.fields.PositiveIntegerField')(default=False))

        # Changing field 'Dissemination.total_households'
        db.alter_column('coco_dissemination', 'total_households', self.gf('django.db.models.fields.PositiveIntegerField')(default=0))

        # Changing field 'Dissemination.total_new_households'
        db.alter_column('coco_dissemination', 'total_new_households', self.gf('django.db.models.fields.PositiveIntegerField')(default=0))

        # Changing field 'Person.delivery_date'
        db.alter_column('coco_person', 'delivery_date', self.gf('django.db.models.fields.DateField')(default=None))

    models = {
        'coco.adoption': {
            'Meta': {'object_name': 'Adoption'},
            'baby_bathe': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'baby_colostrums': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'baby_hold': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'baby_wrap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'breastfeed': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'checked_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cord_care': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cord_cut': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_visit': ('django.db.models.fields.DateField', [], {}),
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'family_planning': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fp_awareness': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fp_family_discussion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fp_family_member': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fp_method': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fp_service_providers': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fp_use': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liquids': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mediator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Mediator']"}),
            'other_food': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Person']"}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preparation_of_last_delivery': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wiped': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'coco.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'dissemination': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Dissemination']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Person']"}),
            'question_asked': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'coco.dissemination': {
            'Meta': {'unique_together': "(('date', 'start_time', 'end_time', 'mediator', 'village'),)", 'object_name': 'Dissemination'},
            'attendance_records': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coco.Person']", 'through': "orm['coco.Attendance']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Mediator']"}),
            'song': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'total_households': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_lactating_women': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_new_households': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_pregnant_women': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Video']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coco.Village']"})
        },
        'coco.mediator': {
            'Meta': {'object_name': 'Mediator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'villages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coco.Village']", 'symmetrical': 'False'})
        },
        'coco.person': {
            'Meta': {'object_name': 'Person'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'delivery_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'coco.village': {
            'Meta': {'object_name': 'Village'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['coco']