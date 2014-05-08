enem2012.json: enem2012.db
	../sqlite2json.py enem2012.db >.$@.tmp
	mv .$@.tmp $@

enem2012.db: DADOS_ENEM_2012_CUT.csv QUESTIONARIO_ENEM_2012_CUT.csv
	rm -f .$@.tmp
	sqlite3 .$@.tmp <../schema.sql
	../deps/csv2sqlite/csv2sqlite.py DADOS_ENEM_2012_CUT.csv .$@.tmp dados
	../deps/csv2sqlite/csv2sqlite.py QUESTIONARIO_ENEM_2012_CUT.csv .$@.tmp questionarios
	sqlite3 .$@.tmp <../summary.sql
	mv .$@.tmp $@

#   1: NU_INSCRICAO   3: IDADE      4: TP_SEXO    5: COD_MUNICIPIO_INSC   8: ST_CONCLUSAO     12: TP_ESTADO_CIVIL  13: TP_COR_RACA
#  57: NU_NT_CN      58: NU_NT_CH  59: NU_NT_LC  60: NU_NT_MT            80: NU_NOTA_REDACAO
DADOS_ENEM_2012_CUT.csv: DADOS_ENEM_2012.csv
	cut -d ',' -f1,3-5,8,12-13,57-60,80 $^ | sed -e 's/\"//g' | sed -e 's/\,\./\,/g' >$@

#  1: NU_INSCRICAO
#
#  3: Q01 - Até quando seu pai estudou?
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
#  4: Q02 - Até quando sua mãe estudou?
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
#  5: Q03 - Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)
#  A	Nenhuma renda;
#  B	Até um salário mínimo (até R$622,00);
#  C	Mais de 1 até 1,5 (de R$ 622,01 até R$ 933,00).
#  D	Mais de 1,5 até 2 (de R$ 933,01 até R$ 1244,00).
#  E	Mais de 2 até 2,5 (de R$ 1244,01 até R$ 1555,00).
#  F	Mais de 2,5 até 3 (de R$ 1555,01 até R$ 1866,00).
#  G	Mais de 3 até 4 (de R$ 1866,01 até R$ 2488,00).
#  H	Mais de 4 até 5 (de R$ 2488,01 até R$ 3110,00).
#  I	Mais de 5 até 6 (de R$ 3110,01 até R$ 3732,00).
#  J	Mais de 6 até 7 (de R$ 3732,01 até R$ 4354,00).
#  K	Mais de 7 até 8 (de R$ 4354,01 até R$ 4976,00).
#  L	Mais de 8 até 9 (de R$ 4976,01 até R$ 5598,00).
#  M	Mais de 9 até 10 (de R$ 5598,01 até R$ 6220,00).
#  N	Mais de 10 até 12 (de R$ 6220,01 até R$ 7464,00).
#  O	Mais de 12 até 15 (de R$ 7464,01 até R$ 9330,00).
#  P	Mais de 15 até 20 (de R$ 9330,01 até R$ 12440,00).
#  Q	Acima de 20 salários (mais de R$12440,00);
#
# 37: Q35 - Em que tipo de escola você cursou o Ensino Médio?
# A	Somente em escola pública;
# B	Maior parte em escola pública;
# C	Somente em escola particular;
# D	Maior parte em escola particular;
# E	Somente em escola indígena;
# F	Maior parte em escola indígena;
# G	Somente em escola situada em comunidade quilombola;
# H	Maior parte em escola situada em comunidade quilombola;

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
