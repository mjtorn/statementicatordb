# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.conf import settings

from statementicatordb.statementicatordb import models

import csv

import datetime

import logging

logger = logging.getLogger('statementicatordb.parser')

class Parser(object):
    """Parer for Nordea TSV bank statements
    """

    fields = {
        u'Kirjauspäivä': 'booking_date',
        u'Arvopäivä': 'value_date',
        u'Maksupäivä': 'due_date',
        u'Määrä': 'amount',
        u'Saaja/Maksaja': 'person',
        u'Tilinumero': 'account',
        u'BIC': 'bic',
        u'Tapahtuma': 'transaction_type',
        u'Viite': 'reference',
        u'Maksajan viite': 'payer_reference',
        u'Viesti': 'message',
        u'Kortinnumero': 'card_number',
        u'Kuitti': 'receipt',
    }

    fk_lookups = {
        'person': ('Person', 'name'),
        'account': ('Account', 'number'),
        'transaction_type': ('TransactionType', 'name'),
    }

    def __init__(self, bic, lines):
        """Simple constructor
        """

        self.bic = bic
        self.lines = lines

    def create_dicts(self):
        """Create a dictionary from lines
        """

        logger.info('Creating dicts from %d lines' % len(self.lines))

        csv_lines = csv.reader(self.lines, dialect='excel-tab')
        csv_lines = list(csv_lines)

        headings = csv_lines.pop(0)

        ## So strange utf-8 is still fucked in 2012 and python
        headings = [unicode(h, 'utf-8') for h in headings]

        out = []
        for i in xrange(len(csv_lines)):
            if csv_lines[i]:
                out.append({})
                for j in xrange(len(headings)):
                    if headings[j]:
                        db_field = self.fields[headings[j]]

                        value = csv_lines[i][j].strip()

                        if db_field.endswith('_date'):
                            for date_input_format in settings.DATE_INPUT_FORMATS:
                                try:
                                    value = datetime.datetime.strptime(value, date_input_format)
                                    break
                                except ValueError:
                                    pass
                        elif db_field == 'amount':
                            # finns suck with this...
                            value = value.replace(',', '.')
                        elif db_field == 'account' and not value:
                            value = self.ban

                        out[-1][db_field] = value or None

        logger.info('Done')

        return out

    def get_or_create(self, d):
        """Statements!
        """

        for k, v in d.items():
            if self.fk_lookups.has_key(k):
                model_name, field_name = self.fk_lookups[k]

                model = getattr(models, model_name)
                bob, created = model.objects.get_or_create(**{field_name: v})

                d[k] = bob

        return models.Transaction.objects.get_or_create(**d)

    def run(self):
        """Do the magic
        """

        logger.info('SHOWTIME')

        ## Assume we have all BICs
        self.bank = models.Bank.objects.get(bic=self.bic)

        ## first line contains account number
        ban_line = self.lines.pop(0)
        self.ban = ban_line.split()[-1]

        ## Make sure we exist
        self.account, created = models.Account.objects.get_or_create(bank=self.bank, number=self.ban)

        ## followed by an empty one
        self.lines.pop(0)

        data_dicts = self.create_dicts()

        for d in data_dicts:
            transaction, created = self.get_or_create(d)
            if created:
                logger.info(u'created %s' % transaction)

# EOF

