enem2010.json: enem2010.db
	../sqlite2json.py enem2010.db >.$@.tmp
	mv .$@.tmp $@

enem2010.db: DADOS_ENEM_2010_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv
	rm -f .$@.tmp
	sqlite3 .$@.tmp <../schema.sql
	../deps/csv2sqlite/csv2sqlite.py DADOS_ENEM_2010_CUT.csv .$@.tmp dados
	../deps/csv2sqlite/csv2sqlite.py QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv .$@.tmp questionarios
	sqlite3 .$@.tmp <../summary.sql
	mv .$@.tmp $@

enem2010.csv: DADOS_ENEM_2010_CUT.csv QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv
	join -t, -j1 -o0,2.2,2.3,2.4,2.5,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,1.11,1.12 --header $^ >$@

#   1: NU_INSCRICAO   3: IDADE      4: TP_SEXO    5: COD_MUNICIPIO_INSC   8: ST_CONCLUSAO     30: TP_ESTADO_CIVIL  31: TP_COR_RACA
#  57: NU_NT_CN      58: NU_NT_CH  59: NU_NT_LC  60: NU_NT_MT            80: NU_NOTA_REDACAO
DADOS_ENEM_2010_CUT.csv: DADOS_ENEM_2010.csv
	cut -d ',' -f1,3-5,8,30-31,46-49,69 $^ | sed -e 's/\"//g' | sed -e 's/\,\./\,/g' | sort -n >$@

#  1: NU_INSCRICAO
#
#  4: Q02 - Até quando seu pai estudou?
#  A	Da 1ª à 4ª série do Ensino Fundamental (antigo primário)
#  B	Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio)
#  C	Ensino Médio (antigo 2º grau)
#  D	Ensino Superior
#  E	Especialização
#  F	Mestrado
#  G	Doutorado
#  H	Não estudou.
#  I	Não sei
#
#  5: Q03 - Até quando sua mãe estudou?
#  A	Da 1ª à 4ª série do Ensino Fundamental (antigo primário)
#  B	Da 5ª à 8ª série do Ensino Fundamental (antigo ginásio)
#  C	Ensino Médio (antigo 2º grau)
#  D	Ensino Superior
#  E	Especialização
#  F	Mestrado
#  G	Doutorado
#  H	Não estudou.
#  I	Não sei
#
#  6: Q04 - Somando a sua renda com a renda das pessoas que moram com você, quanto é, aproximadamente, a renda familiar mensal?
#  A	Até 1 salário mínimo (até R$ 510,00).
#  B	De 1 a 3 salários mínimos (de R$ 510,00 até R$ 1.530,00).
#  C	De 3 a 6 salários mínimos (de R$ 1.530,00 até R$ 3.060,00).
#  D	De 6 a 9 salários mínimos (de R$ 3.060,00 até R$ 4.590,00).
#  E	De 9 a 12 salários mínimos (de R$ 4.590,00 até R$ 6.120,00).
#  F	De 12 a 15 salários mínimos (de R$ 6.210,00 até R$ 7.650,00).
#  G	Mais de 15 salários mínimos (mais de R$ 7.650,00).
#  H	Nenhuma renda.
#
# 35: Q33 - Em que tipo de escola você cursou o Ensino Médio?
# A	Somente em escola pública.
# B	Maior parte em escola pública.
# C	Somente em escola particular.
# D	Maior parte em escola particular.
# E	Somente em escola indígena.
# F	Maior parte em escola não-indígena.
# G	Somente em escola situada em comunidade quilombola.
# H	Não freqüentei a escola

QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010_CUT.csv: QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.csv
	cut -d ',' -f1,4-6,35 $^ | sed -e 's/\"//g' | sort -n >$@

DADOS_ENEM_2010.csv: DADOS_ENEM_2010.txt
	cat DADOS_ENEM_2010_FIELDNAMES.txt >$@
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
