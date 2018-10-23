all: pdf
pdf:
	./tables_generator.py
	#xelatex process_hkust.tex &> process_hkust.log
	max_in_open=32 xelatex process_hkust.tex
check:
	./tables_generator.py check

