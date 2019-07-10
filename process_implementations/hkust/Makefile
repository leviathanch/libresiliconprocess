yaml = steps_wet.yaml steps_dry.yaml
yamldeps = cleanliness_levels.yaml equipment.yaml repetitive_steps.yaml
tikzdeps = $(wildcard tikz_process_steps/*.tex)
texs = $(yaml:.yaml=.tex)
pdfs = $(yaml:.yaml=.pdf)

all: $(pdfs)

$(texs): %.tex:%.yaml $(yamldeps) $(tikzdeps)
	./tables_generator.py -f $<

$(pdfs): %.pdf:%.tex
	max_in_open=32 xelatex '\def\inctable{$<}\input{process.tex}' > log
	mv process.pdf $@
	rm log process.log

check:
	./tables_generator.py check

clean:
	rm $(texs) $(pdfs)
