yaml = steps_wet.yaml steps_dry.yaml
yamldeps = repetitive_steps.yaml
texs = $(yaml:.yaml=.tex)
pdfs = $(yaml:.yaml=.pdf)

all: $(pdfs)

$(texs): %.tex:%.yaml $(yamldeps)
	./tables_generator.py -f $<

$(pdfs): %.pdf:%.tex
	max_in_open=32 xelatex '\def\inctable{$<}\input{process.tex}' > log
	mv process.pdf $@

check:
	./tables_generator.py check

clean:
	rm $(texs) $(pdfs)
