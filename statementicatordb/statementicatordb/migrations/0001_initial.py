# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Bank'
        db.create_table('statementicatordb_bank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('bic', self.gf('django.db.models.fields.CharField')(max_length=11)),
        ))
        db.send_create_signal('statementicatordb', ['Bank'])

        # Adding model 'Account'
        db.create_table('statementicatordb_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['statementicatordb.Bank'], null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('statementicatordb', ['Account'])

        # Adding model 'Person'
        db.create_table('statementicatordb_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['statementicatordb.Account'], null=True, blank=True)),
        ))
        db.send_create_signal('statementicatordb', ['Person'])

        # Adding model 'TransactionType'
        db.create_table('statementicatordb_transactiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('statementicatordb', ['TransactionType'])

        # Adding model 'Transaction'
        db.create_table('statementicatordb_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('booking_date', self.gf('django.db.models.fields.DateField')()),
            ('value_date', self.gf('django.db.models.fields.DateField')()),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statementicatordb.Person'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statementicatordb.Account'])),
            ('bic', self.gf('django.db.models.fields.CharField')(default=None, max_length=11, null=True, blank=True)),
            ('transaction_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statementicatordb.TransactionType'])),
            ('reference', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('payer_reference', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('card_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('receipt', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
        ))
        db.send_create_signal('statementicatordb', ['Transaction'])


    def backwards(self, orm):
        
        # Deleting model 'Bank'
        db.delete_table('statementicatordb_bank')

        # Deleting model 'Account'
        db.delete_table('statementicatordb_account')

        # Deleting model 'Person'
        db.delete_table('statementicatordb_person')

        # Deleting model 'TransactionType'
        db.delete_table('statementicatordb_transactiontype')

        # Deleting model 'Transaction'
        db.delete_table('statementicatordb_transaction')


    models = {
        'statementicatordb.account': {
            'Meta': {'object_name': 'Account'},
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['statementicatordb.Bank']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'statementicatordb.bank': {
            'Meta': {'object_name': 'Bank'},
            'bic': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'statementicatordb.person': {
            'Meta': {'object_name': 'Person'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['statementicatordb.Account']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        'statementicatordb.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statementicatordb.Account']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'bic': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'booking_date': ('django.db.models.fields.DateField', [], {}),
            'card_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'payer_reference': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statementicatordb.Person']"}),
            'receipt': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'transaction_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statementicatordb.TransactionType']"}),
            'value_date': ('django.db.models.fields.DateField', [], {})
        },
        'statementicatordb.transactiontype': {
            'Meta': {'object_name': 'TransactionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['statementicatordb']
