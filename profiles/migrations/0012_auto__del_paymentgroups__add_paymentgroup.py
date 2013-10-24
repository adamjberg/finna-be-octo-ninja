# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PaymentGroups'
        db.delete_table(u'profiles_paymentgroups')

        # Removing M2M table for field email on 'PaymentGroups'
        db.delete_table(db.shorten_name(u'profiles_paymentgroups_email'))

        # Adding model 'PaymentGroup'
        db.create_table(u'profiles_paymentgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('primary_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'profiles', ['PaymentGroup'])

        # Adding M2M table for field email on 'PaymentGroup'
        m2m_table_name = db.shorten_name(u'profiles_paymentgroup_email')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paymentgroup', models.ForeignKey(orm[u'profiles.paymentgroup'], null=False)),
            ('paymentgroupemail', models.ForeignKey(orm[u'profiles.paymentgroupemail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paymentgroup_id', 'paymentgroupemail_id'])


    def backwards(self, orm):
        # Adding model 'PaymentGroups'
        db.create_table(u'profiles_paymentgroups', (
            ('primary_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('payment_group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'profiles', ['PaymentGroups'])

        # Adding M2M table for field email on 'PaymentGroups'
        m2m_table_name = db.shorten_name(u'profiles_paymentgroups_email')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paymentgroups', models.ForeignKey(orm[u'profiles.paymentgroups'], null=False)),
            ('paymentgroupemail', models.ForeignKey(orm[u'profiles.paymentgroupemail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paymentgroups_id', 'paymentgroupemail_id'])

        # Deleting model 'PaymentGroup'
        db.delete_table(u'profiles_paymentgroup')

        # Removing M2M table for field email on 'PaymentGroup'
        db.delete_table(db.shorten_name(u'profiles_paymentgroup_email'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'confsessions.session': {
            'Meta': {'object_name': 'Session'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'presenter': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sessiontype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['confsessions.SessionType']"}),
            'teaser': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'confsessions.sessiontime': {
            'Meta': {'object_name': 'SessionTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'confsessions.sessiontype': {
            'Meta': {'object_name': 'SessionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'session_time': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['confsessions.SessionTime']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.hearabout': {
            'Meta': {'object_name': 'HearAbout'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.paymentgroup': {
            'Meta': {'object_name': 'PaymentGroup'},
            'email': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.PaymentGroupEmail']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'primary_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'profiles.paymentgroupemail': {
            'Meta': {'object_name': 'PaymentGroupEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'affil_other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'affiliation': ('django.db.models.fields.CharField', [], {'default': "'UBCStudent'", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gluten': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graduating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hear': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['profiles.HearAbout']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lactose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nut_allergy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_faculty': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'saved_sessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['confsessions.Session']", 'symmetrical': 'False'}),
            'student_num': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'times_participation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'vegan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year_of_study': ('django.db.models.fields.CharField', [], {'default': "'U1'", 'max_length': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']