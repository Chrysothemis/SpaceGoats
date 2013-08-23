# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table(u'ffxiv_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ffxiv+', to=orm['auth.User'])),
            ('server', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('picture', self.gf('goatnails.db.models.ImageWithThumbsField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ffxiv', ['Character'])

        # Adding model 'Job'
        db.create_table(u'ffxiv_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abv', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('icon', self.gf('goatnails.db.models.ImageWithThumbsField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ffxiv', ['Job'])

        # Adding model 'Level'
        db.create_table(u'ffxiv_level', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ffxiv.Character'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ffxiv.Job'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ffxiv', ['Level'])

        # Adding model 'Article'
        db.create_table(u'ffxiv_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ffxiv+', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ffxiv', ['Article'])

        # Adding model 'Screenshot'
        db.create_table(u'ffxiv_screenshot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('image', self.gf('goatnails.db.models.ImageWithThumbsField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ffxiv', ['Screenshot'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table(u'ffxiv_character')

        # Deleting model 'Job'
        db.delete_table(u'ffxiv_job')

        # Deleting model 'Level'
        db.delete_table(u'ffxiv_level')

        # Deleting model 'Article'
        db.delete_table(u'ffxiv_article')

        # Deleting model 'Screenshot'
        db.delete_table(u'ffxiv_screenshot')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ffxiv.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ffxiv+'", 'to': u"orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ffxiv.character': {
            'Meta': {'object_name': 'Character'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ffxiv.Job']", 'through': u"orm['ffxiv.Level']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('goatnails.db.models.ImageWithThumbsField', [], {'max_length': '100', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ffxiv+'", 'to': u"orm['auth.User']"}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ffxiv.job': {
            'Meta': {'object_name': 'Job'},
            'abv': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'icon': ('goatnails.db.models.ImageWithThumbsField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ffxiv.level': {
            'Meta': {'object_name': 'Level'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ffxiv.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ffxiv.Job']"}),
            'level': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ffxiv.screenshot': {
            'Meta': {'object_name': 'Screenshot'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('goatnails.db.models.ImageWithThumbsField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['ffxiv']