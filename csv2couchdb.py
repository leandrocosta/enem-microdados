#!/usr/bin/env python
#coding=utf-8

"""Usage:
    csv2couchdb.py --csv-file=FILE --couchdb-url=URL --db-name=NAME --id-attr=ATTR --bulk-size=SIZE
    csv2couchdb.py -h | --help

Options:
    -h --help                   Show this screen.
    -f FILE --csv-file=FILE
    -u URL --couchdb-url=URL
    -n NAME --db-name=NAME
    -i ATTR --id-attr=ATTR
    -b SIZE --bulk-size SIZE
"""
from docopt import docopt
import csv
import pycouchdb
from progressbar import ProgressBar, Percentage, Bar, ETA

def _guess_types(fileobj, max_sample_size=100):
    '''Guess column types (as for SQLite) of CSV.

    :param fileobj: read-only file object for a CSV file.
    '''
    reader = csv.reader(fileobj)
    # skip header
    _headers = reader.next()
    # we default to text for each field
    types = ['text'] * len(_headers)
    # order matters
    # (order in form of type you want used in case of tie to be last)
    options = [
        ('text', unicode),
        ('real', float),
        ('integer', int)
        # 'date',
        ]
    # for each column a set of bins for each type counting successful casts
    perresult = {
        'integer': 0,
        'real': 0,
        'text': 0
        }
    results = [ dict(perresult) for x in range(len(_headers)) ]
    for count,row in enumerate(reader):
        for idx,cell in enumerate(row):
            cell = cell.strip()
            # replace ',' with '' to improve cast accuracy for ints and floats
            cell = cell.replace(',', '')
            for key,cast in options:
                try:
                    # for null cells we can assume success
                    if cell:
                        cast(cell)
                    results[idx][key] += 1
                # shz: ignore all exceptions
                except (Exception), inst:
                    pass
        if count >= max_sample_size:
            break
    for idx,colresult in enumerate(results):
        for _type, dontcare in options:
            if colresult[_type] == count + 1:
                types[idx] = _type
    return types

if __name__ == '__main__':
    arguments = docopt(__doc__)

    server = pycouchdb.Server(arguments['--couchdb-url'])

    try:
        db = server.database(arguments['--db-name'])
    except Exception, e:
        print 'error trying to database instance named %s [%s]' % (arguments['--db-name'], e)
        db = server.create(arguments['--db-name'])
        print 'database %s created' % arguments['--db-name']

    fo = open(arguments['--csv-file'])
    reader = csv.reader(fo)

    types = _guess_types(fo)
    fo.seek(0)
    numdocs = len(fo.readlines())-1
    fo.seek(0)
    headers = reader.next()

    i = 0
    docs = []
    print 'Saving: %d docs' % numdocs
    pbar = ProgressBar(widgets=[Percentage(), ' ', Bar(), ' ', ETA()], maxval=numdocs).start()

    for row in reader:
        row = [
            None if x == ''
            else float(x.replace(',', '')) if y == 'real'
            else int(x) if y == 'integer'
            else x for (x,y) in zip(row, types) ]

        doc = dict(zip(headers, row))

        for x in list(doc.keys()):
            if doc[x] == None:
                del doc[x]

        doc['_id'] = str(doc[arguments['--id-attr']])

        #db.save(doc)

        docs.append(doc)
        i = i+1

        if (len(docs) >= int(arguments['--bulk-size'])):
            db.save_bulk(docs)
            pbar.update(i)
            docs = []

    pbar.finish()
