# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.db import models

# Create your models here.

class Bank(models.Model):
    """A bank
    """

    name = models.CharField(max_length=80)

    bic = models.CharField(max_length=11)

    def __unicode__(self):
        return u'%s' %  self.name


class Account(models.Model):
    """``Bank`` ``Account``s go here.
    """

    ## NULLable because we don't always know the bank
    bank = models.ForeignKey(Bank, null=True, blank=True, default=None)

    ## Not sure how long IBANs or others can be
    ## or if different banks can have the same numbers; probably not
    number = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return u'%s' % self.number


class Person(models.Model):
    """An owner of an ``Account``
    """

    name = models.CharField(max_length=160)

    ## Can not always know the account here for eg. incoming transactions
    account = models.ForeignKey(Account, null=True, blank=True, default=None)

    def __unicode__(self):
        return u'%s' % self.name


class TransactionType(models.Model):
    """What kind of ``Transaction`` was it?
    """

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return u'%s' % self.name


class Transaction(models.Model):
    """These are rows read in from a bank statement
    """

    booking_date = models.DateField()
    value_date = models.DateField()
    due_date = models.DateField()

    # Can be grown ;)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    # Payer/Recipient
    person = models.ForeignKey(Person)

    account = models.ForeignKey(Account)

    ## Denormalize just in case
    bic = models.CharField(max_length=11, null=True, blank=True, default=None)

    transaction_type = models.ForeignKey(TransactionType)

    reference = models.CharField(max_length=80, null=True, blank=True, default=None)
    payer_reference = models.CharField(max_length=80, null=True, blank=True, default=None)

    message = models.TextField(null=True, blank=True, default=None)

    card_number = models.CharField(max_length=80, null=True, blank=True, default=None)

    receipt = models.CharField(max_length=80, null=True, blank=True, default=None)

    def __unicode__(self):
        return u'%s' % self.amount

# EOF

