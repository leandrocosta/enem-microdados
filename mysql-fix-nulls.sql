UPDATE enem2010 SET ESCOLARIDADE_MAE = 0 WHERE ESCOLARIDADE_MAE IS NULL;
UPDATE enem2010 SET ESCOLARIDADE_PAI = 0 WHERE ESCOLARIDADE_PAI IS NULL;
UPDATE enem2010 SET RENDA_FAMILIAR = 0 WHERE RENDA_FAMILIAR IS NULL;
UPDATE enem2010 SET ST_CONCLUSAO = 0 WHERE ST_CONCLUSAO IS NULL;
UPDATE enem2010 SET TIPO_ESCOLA = 0 WHERE TIPO_ESCOLA IS NULL;
