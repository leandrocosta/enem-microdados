enem2011.json: enem2011.db
	../sqlite2json.py enem2011.db >.$@.tmp
	mv .$@.tmp $@

enem2011.db: DADOS_ENEM_2011_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011_CUT.csv
	rm -f .$@.tmp
	sqlite3 .$@.tmp <../schema.sql
	../deps/csv2sqlite/csv2sqlite.py DADOS_ENEM_2011_CUT.csv .$@.tmp dados
	../deps/csv2sqlite/csv2sqlite.py QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011_CUT.csv .$@.tmp questionarios
	sqlite3 .$@.tmp <../summary.sql
	mv .$@.tmp $@

enem2011.csv: DADOS_ENEM_2011_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011_CUT.csv
	join -t, -j1 -o0,2.2,2.3,2.4,2.5,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,1.11,1.12 --header $^ >$@

#   1: NU_INSCRICAO   3: IDADE      4: TP_SEXO    5: COD_MUNICIPIO_INSC   8: ST_CONCLUSAO     30: TP_ESTADO_CIVIL  31: TP_COR_RACA
#  57: NU_NT_CN      58: NU_NT_CH  59: NU_NT_LC  60: NU_NT_MT            80: NU_NOTA_REDACAO
DADOS_ENEM_2011_CUT.csv: DADOS_ENEM_2011.csv
	cut -d ',' -f1,3-5,8,30-31,46-49,69 $^ | sed -e 's/\"//g' | sed -e 's/\,\./\,/g' >$@

#  1: NU_INSCRICAO
#
#  4: Q02 - Até quando seu pai estudou?
#  A	Não estudou;
#  B	Da 1ª à 4ª série do Ensino Fundamental (antigo primário);
#  C	Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio);
#  D	Ensino Médio (antigo 2º grau) incompleto;
#  E	Ensino Médio (antigo 2º grau);
#  F	Ensino Superior incompleto;
#  G	Ensino Superior;
#  H	Pós-graduação;
#  I	Não sei;
#
#  5: Q03 - Até quando sua mãe estudou?
#  A	Não estudou;
#  B	Da 1ª à 4ª série do Ensino Fundamental (antigo primário);
#  C	Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio);
#  D	Ensino Médio (antigo 2º grau) incompleto;
#  E	Ensino Médio (antigo 2º grau);
#  F	Ensino Superior incompleto;
#  G	Ensino Superior;
#  H	Pós-graduação;
#  I	Não sei;
#
#  6: Q04 - Somando a sua renda com a renda das pessoas que moram com você, quanto é, aproximadamente, a renda familiar mensal?
#  A	Nenhuma renda;
#  B	Até um salário mínimo (até R$545,00);
#  C	Entre 1 e 1,5 salários (entre R$545,00 até R$817,50);
#  D	Entre 1,5 e 2 salários (entre R$817,50 até R$1.090,00);
#  E	Entre 2 e 5 salários (entre R$1.090,00 até R$2.725,00);
#  F	Entre 5 e 7 salários (entre R$2.725,00 até R$3.815,00);
#  G	Entre 7 e 10 salários (entre R$3.815,00 até R$5.450,00);
#  H	Entre 10 e 12 salários (entre R$5.450,00 até R$ 6.540,00);
#  I	Entre 12 e 15 salários (entre R$6.540,00 até R$8.175,00);
#  J	Entre 15 e 30 salários (entre R$8.175,00 até R$ 16.350,00);
#  K	Acima de 30 salários (mais de R$16.350,00);
#
# 35: Q33 - Em que tipo de escola você cursou o Ensino Médio?
# A	Somente em escola pública;
# B	Maior parte em escola pública;
# C	Somente em escola particular;
# D	Maior parte em escola particular;
# E	Somente em escola indígena;
# F	Maior parte em escola indígena;
# G	Somente em escola situada em comunidade quilombola;
# H	Maior parte em escola situada em comunidade quilombola;
# I	Não frequentei a escola.

QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011_CUT.csv: QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.csv
	cut -d ',' -f1,4-6,35 $^ | sed -e 's/\"//g' >$@

DADOS_ENEM_2011.csv: DADOS_ENEM_2011.TXT
	cat DADOS_ENEM_2011_FIELDNAMES.txt >$@
	awk -v FIELDWIDTHS='12 4 3 1 7 150 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 8 7 150 2 1 1 1 7 150 2 1 1 1 1 9 9 9 9 45 45 45 45 3 3 3 3 1 45 45 50 45 1 9 9 9 9 9 9 1 2 8 7 150 2 1 1 1' -v OFS=',' '{$$1=$$1 ""; for (i=1; i<=NF; i++) { gsub(/^[ \t]+|[ \t]+$$/, "", $$i);} print}' $< >>$@

QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.csv: QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.TXT
	cat QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011_FIELDNAMES.txt >$@
	awk -v FIELDWIDTHS='12 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1' -v OFS=',' '{$$1=$$1 ""; for (i=1; i<=NF; i++) { gsub(/^[ \t]+|[ \t]+$$/, "", $$i);} print}' $< >>$@

DADOS_ENEM_2011.TXT: microdados_enem2011.zip
	unzip -j $< DADOS/$@
	dos2unix $@

QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.TXT: microdados_enem2011.zip
	unzip -j $< DADOS/$@
	dos2unix $@

microdados_enem2011.zip:
	wget ftp://ftp.inep.gov.br/microdados/$@ -O .$@.tmp
	mv .$@.tmp $@

clean:
	rm -f microdados_enem2011.zip DADOS_ENEM_2011.TXT QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.TXT DADOS_ENEM_2011.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.csv DADOS_ENEM_2011_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011_CUT.csv enem2011.db enem2011.json
