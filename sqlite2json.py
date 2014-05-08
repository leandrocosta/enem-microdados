#!/usr/bin/env python

import sys
import sqlite3
import simplejson
simplejson.encoder.FLOAT_REPR = lambda f: ('%.2f' % f)
simplejson.encoder.c_make_encoder = None

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

qry =""" 
     SELECT
         COD_MUNICIPIO_INSC, SUM(INSCRITOS), SUM(PRESENTES),
         AVG(CN_AVG/PRESENTES), AVG(CH_AVG/PRESENTES),
         AVG(LC_AVG/PRESENTES), AVG(MT_AVG/PRESENTES),
         AVG(RE_AVG/PRESENTES), AVG(ME_AVG/PRESENTES)
     FROM SUMMARY GROUP BY COD_MUNICIPIO_INSC
     """

d = [list(row) for row in c.execute(qry)]

print simplejson.dumps(d, separators=(',', ':'))#, indent=1)
