all:
	make -C enem2012
	make -C enem2011
	make -C enem2010

clean:
	make -C enem2012 clean
	make -C enem2011 clean
	make -C enem2010 clean
