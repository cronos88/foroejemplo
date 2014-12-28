# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Votante_resp.usuario' to match new field type.
        db.rename_column(u'mundodjango_votante_resp', 'usuario_id', 'usuario')
        # Changing field 'Votante_resp.usuario'
        db.alter_column(u'mundodjango_votante_resp', 'usuario', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'Votante_resp', fields ['usuario']
        db.delete_index(u'mundodjango_votante_resp', ['usuario_id'])


        # Renaming column for 'Votante_resp.respuesta' to match new field type.
        db.rename_column(u'mundodjango_votante_resp', 'respuesta_id', 'respuesta')
        # Changing field 'Votante_resp.respuesta'
        db.alter_column(u'mundodjango_votante_resp', 'respuesta', self.gf('django.db.models.fields.IntegerField')())
        # Removing index on 'Votante_resp', fields ['respuesta']
        db.delete_index(u'mundodjango_votante_resp', ['respuesta_id'])


        # Changing field 'Votante_preg.usuario'
        db.alter_column(u'mundodjango_votante_preg', 'usuario', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Adding index on 'Votante_resp', fields ['respuesta']
        db.create_index(u'mundodjango_votante_resp', ['respuesta_id'])

        # Adding index on 'Votante_resp', fields ['usuario']
        db.create_index(u'mundodjango_votante_resp', ['usuario_id'])


        # Renaming column for 'Votante_resp.usuario' to match new field type.
        db.rename_column(u'mundodjango_votante_resp', 'usuario', 'usuario_id')
        # Changing field 'Votante_resp.usuario'
        db.alter_column(u'mundodjango_votante_resp', 'usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Renaming column for 'Votante_resp.respuesta' to match new field type.
        db.rename_column(u'mundodjango_votante_resp', 'respuesta', 'respuesta_id')
        # Changing field 'Votante_resp.respuesta'
        db.alter_column(u'mundodjango_votante_resp', 'respuesta_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mundodjango.Respuestas']))

        # Changing field 'Votante_preg.usuario'
        db.alter_column(u'mundodjango_votante_preg', 'usuario', self.gf('django.db.models.fields.IntegerField')())

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mundodjango.categorias': {
            'Meta': {'object_name': 'Categorias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'mundodjango.preguntas': {
            'Meta': {'object_name': 'Preguntas'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mundodjango.Categorias']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'mundodjango.respuestas': {
            'Meta': {'object_name': 'Respuestas'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_resp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mundodjango.Preguntas']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'mundodjango.votante_preg': {
            'Meta': {'object_name': 'Votante_preg'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.IntegerField', [], {}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'mundodjango.votante_resp': {
            'Meta': {'object_name': 'Votante_resp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {}),
            'usuario': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mundodjango']