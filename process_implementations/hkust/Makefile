all: pdf
pdf:
	./tables_generator.py
	xelatex process_hkust.tex &> process_hkust.log
check:
	./tables_generator.py check

