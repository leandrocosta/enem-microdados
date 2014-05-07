enem2010.json: enem2010.db
	../sqlite2json.py enem2010.db >.$@.tmp
	mv .$@.tmp $@

enem2010.db: DADOS_ENEM_2010_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv
	rm -f .$@.tmp
	sqlite3 .$@.tmp "CREATE TABLE dados(NU_INSCRICAO INTEGER PRIMARY KEY,IDADE INTEGER,TP_SEXO INTEGER,COD_MUNICIPIO_INSC INTEGER,ST_CONCLUSAO INTEGER,TP_ESTADO_CIVIL INTEGER,TP_COR_RACA INTEGER,NU_NT_CN REAL,NU_NT_CH REAL,NU_NT_LC REAL,NU_NT_MT REAL,NU_NOTA_REDACAO REAL);"
	sqlite3 .$@.tmp "CREATE TABLE questionario(NU_INSCRICAO INTEGER PRIMARY KEY,Q02 CHAR,Q03 CHAR,Q04 CHAR,Q33 CHAR,FOREIGN KEY(NU_INSCRICAO) REFERENCES dados(NU_INSCRICAO));"
	sqlite3 .$@.tmp "CREATE INDEX idx_municipios ON dados(cod_municipio_insc);"
	../deps/csv2sqlite/csv2sqlite.py DADOS_ENEM_2010_CUT.csv .$@.tmp dados
	../deps/csv2sqlite/csv2sqlite.py QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv .$@.tmp questionarios
	mv .$@.tmp $@

#   1: NU_INSCRICAO   3: IDADE      4: TP_SEXO    5: COD_MUNICIPIO_INSC   8: ST_CONCLUSAO     30: TP_ESTADO_CIVIL  31: TP_COR_RACA
#  57: NU_NT_CN      58: NU_NT_CH  59: NU_NT_LC  60: NU_NT_MT            80: NU_NOTA_REDACAO
DADOS_ENEM_2010_CUT.csv: DADOS_ENEM_2010.csv
	cut -d ',' -f1,3-5,8,30-31,46-49,69 $^ | sed -e 's/\"//g' | sed -e 's/\,\./\,/g' >$@

#  1: NU_INSCRICAO
#  4: Q02 - Até quando seu pai estudou? [A (Não estudou) - H (Pós-graduação)] + I (Não sei)
#  5: Q03 - Até quando sua mãe estudou? [A (Não estudou) - H (Pós-graduação)] + I (Não sei)
#  6: Q04 - Somando a sua renda com a renda das pessoas que moram com você, quanto é, aproximadamente, a renda familiar mensal? [A - K (Acima de 30 salários)]
# 35: Q33 - Em que tipo de escola você cursou o Ensino Médio? [A - I]
QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv: QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.csv
	cut -d ',' -f1,4-6,35 $^ | sed -e 's/\"//g' >$@

DADOS_ENEM_2010.csv: DADOS_ENEM_2010.txt
	cat ENEM_2010_FIELDNAMES.txt >$@
	awk -v FIELDWIDTHS='12 4 3 1 7 150 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 8 7 150 2 1 1 1 7 150 2 1 1 1 1 9 9 9 9 45 45 45 45 3 3 3 3 1 45 45 50 45 1 9 9 9 9 9 9' -v OFS=',' '{$$1=$$1 ""; for (i=1; i<=NF; i++) { gsub(/^[ \t]+|[ \t]+$$/, "", $$i);$$i="\"" $$i "\""} print}' $< >>$@

QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.csv: QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.txt
	cat QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_FIELDNAMES.txt >$@
	awk -v FIELDWIDTHS='12 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1' -v OFS=',' '{$$1=$$1 ""; for (i=1; i<=NF; i++) { gsub(/^[ \t]+|[ \t]+$$/, "", $$i);} print}' $< >>$@

DADOS_ENEM_2010.txt: microdados_enem2010_2.rar
	unrar e $< 'Microdados ENEM 2010/Dados Enem 2010/$@'
	touch $@

QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.txt: microdados_enem2010_2.rar
	unrar e $< 'Microdados ENEM 2010/Dados Enem 2010/$@'
	touch $@

microdados_enem2010_2.rar:
	wget ftp://ftp.inep.gov.br/microdados/$@ -O .$@.tmp
	mv .$@.tmp $@

clean:
	rm -f microdados_enem2010_2.rar DADOS_ENEM_2010.txt QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.txt DADOS_ENEM_2010.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.csv DADOS_ENEM_2010_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv enem2010.db enem2010.json
