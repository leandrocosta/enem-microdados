#!/usr/bin/env python

import sys
import sqlite3
import simplejson
simplejson.encoder.FLOAT_REPR = lambda f: ('%.2f' % f)
simplejson.encoder.c_make_encoder = None

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

d = []

for row in c.execute('SELECT cod_municipio_insc, COUNT(1), \
        COUNT(nu_nt_cn+nu_nt_ch+nu_nt_lc+nu_nt_mt+nu_nota_redacao), \
        AVG(nu_nt_cn), AVG(nu_nt_ch), AVG(nu_nt_lc), AVG(nu_nt_mt), AVG(nu_nota_redacao), \
        AVG((nu_nt_cn+nu_nt_ch+nu_nt_lc+nu_nt_mt+nu_nota_redacao)/5) \
        FROM dados GROUP BY cod_municipio_insc'):
    attrs = dict(zip(("p", "c", "n", "cn", "ch", "lc", "mt", "re", "me"), row))
    d.append(attrs)

print simplejson.dumps(d, separators=(',', ':'))#, indent=1)
