# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PaymentGroups.group'
        db.delete_column('profiles_paymentgroups', 'group')

        # Adding field 'PaymentGroups.payment_group'
        db.add_column('profiles_paymentgroups', 'payment_group',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PaymentGroups.group'
        db.add_column('profiles_paymentgroups', 'group',
                      self.gf('django.db.models.fields.CharField')(default='hello', max_length=200),
                      keep_default=False)

        # Deleting field 'PaymentGroups.payment_group'
        db.delete_column('profiles_paymentgroups', 'payment_group')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.hearabout': {
            'Meta': {'object_name': 'HearAbout'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'profiles.paymentgroups': {
            'Meta': {'object_name': 'PaymentGroups'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'affil_other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'affiliation': ('django.db.models.fields.CharField', [], {'default': "'UBCStudent'", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gluten': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graduating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hear': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['profiles.HearAbout']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lactose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nut_allergy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.TextField', [], {'default': "'Maybe try setting a goal...'", 'blank': 'True'}),
            'other_faculty': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'student_num': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'times_participation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'vegan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year_of_study': ('django.db.models.fields.CharField', [], {'default': "'U1'", 'max_length': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']