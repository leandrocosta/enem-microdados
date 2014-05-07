enem2012.json: enem2012.db
	../sqlite2json.py enem2012.db >.$@.tmp
	mv .$@.tmp $@

enem2012.db: DADOS_ENEM_2012_CUT.csv QUESTIONARIO_ENEM_2012_CUT.csv
	rm -f .$@.tmp
	sqlite3 .$@.tmp "CREATE TABLE dados(NU_INSCRICAO INTEGER PRIMARY KEY,IDADE INTEGER,TP_SEXO INTEGER,COD_MUNICIPIO_INSC INTEGER,ST_CONCLUSAO INTEGER,TP_ESTADO_CIVIL INTEGER,TP_COR_RACA INTEGER,NU_NT_CN REAL,NU_NT_CH REAL,NU_NT_LC REAL,NU_NT_MT REAL,NU_NOTA_REDACAO REAL);"
	sqlite3 .$@.tmp "CREATE TABLE questionario(NU_INSCRICAO INTEGER PRIMARY KEY,Q01 CHAR,Q02 CHAR,Q03 CHAR,Q35 CHAR,FOREIGN KEY(NU_INSCRICAO) REFERENCES dados(NU_INSCRICAO));"
	sqlite3 .$@.tmp "CREATE INDEX idx_municipios ON dados(cod_municipio_insc);"
	../deps/csv2sqlite/csv2sqlite.py DADOS_ENEM_2012_CUT.csv .$@.tmp dados
	../deps/csv2sqlite/csv2sqlite.py QUESTIONARIO_ENEM_2012_CUT.csv .$@.tmp questionarios
	mv .$@.tmp $@

#   1: NU_INSCRICAO   3: IDADE      4: TP_SEXO    5: COD_MUNICIPIO_INSC   8: ST_CONCLUSAO     12: TP_ESTADO_CIVIL  13: TP_COR_RACA
#  57: NU_NT_CN      58: NU_NT_CH  59: NU_NT_LC  60: NU_NT_MT            80: NU_NOTA_REDACAO
DADOS_ENEM_2012_CUT.csv: DADOS_ENEM_2012.csv
	cut -d ',' -f1,3-5,8,12-13,57-60,80 $^ | sed -e 's/\"//g' | sed -e 's/\,\./\,/g' >$@

#  1: NU_INSCRICAO
#  3: Q01 - Até quando seu pai estudou?
#  4: Q02 - Até quando sua mãe estudou?
#  5: Q03 - Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)
# 37: Q35 - Em que tipo de escola você cursou o Ensino Médio?
QUESTIONARIO_ENEM_2012_CUT.csv: QUESTIONARIO_ENEM_2012.csv
	cut -d ',' -f1,3-5,37 $^ | sed -e 's/\"//g' >$@

DADOS_ENEM_2012.csv: microdados_enem2012.zip
	unzip -j $< DADOS/$@
	touch $@

QUESTIONARIO_ENEM_2012.csv: microdados_enem2012.zip
	unzip -j $< DADOS/$@
	touch $@

microdados_enem2012.zip:
	wget ftp://ftp.inep.gov.br/microdados/$@ -O .$@.tmp
	mv .$@.tmp $@

clean:
	rm -f microdados_enem2012.zip DADOS_ENEM_2012.csv QUESTIONARIO_ENEM_2012.csv DADOS_ENEM_2012_CUT.csv QUESTIONARIO_ENEM_2012_CUT.csv enem2012.db enem2012.json
