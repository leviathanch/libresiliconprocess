tikzdeps = $(wildcard tikz_process_steps/*.tex)

tikzdeps = $(wildcard tikz_process_steps/*.tex)

texs = $(wildcard *.tex)

pdfs = process_lowtech_steps.pdf

$(pdfs): %.pdf:%.tex $(tikzdeps) $(texs)
	max_in_open=32 xelatex $<
	max_in_open=32 xelatex $<

all: $(pdfs)

clean:
	rm -f *.log
	rm -f *.gz
	rm -f *.aux
	rm -f *.toc
	rm -f *.pdf
	rm -f *.idx
