TEX = $(wildcard */*.tex) slides.tex

all: slides

slides: CNRS_51_03.pdf CNRS_07.pdf

%.pdf: %.tex
	pdflatex $<

clean:
	rm -rf *.out
	rm -rf *.pdf
