# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib import admin

from statementicatordb.statementicatordb import models

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('booking_date', 'due_date', 'transaction_type', 'amount', 'person', 'account', 'bic', 'message', 'receipt')

admin.site.register(models.Bank)
admin.site.register(models.Account)
admin.site.register(models.Person)
admin.site.register(models.TransactionType)
admin.site.register(models.Transaction, TransactionAdmin)

# EOF

