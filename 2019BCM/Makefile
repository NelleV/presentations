TEX = $(wildcard */*.tex) slides.tex

all: slides

slides: slides.pdf

%.pdf: %.tex
	pdflatex $<

clean:
	rm -rf *.out
	rm -rf *.pdf
