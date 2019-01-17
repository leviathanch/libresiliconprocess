yaml = steps_wet.yaml steps_dry.yaml
texs = $(yaml:.yaml=.tex)
pdfs = $(yaml:.yaml=.pdf)

all: $(pdfs)

$(texs): %.tex : %.yaml
	./tables_generator.py -f $<

$(pdfs):  %.pdf : %.tex
	max_in_open=32 xelatex '\def\inctable{$<}\input{process.tex}'
	mv process.pdf $@

check:
	./tables_generator.py check

