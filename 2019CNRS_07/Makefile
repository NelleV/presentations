TEX = $(wildcard */*.tex) slides.tex

all: slides.pdf

slides: slides.pdf

%.pdf: %.tex
	pdflatex $<

clean:
	rm -rf thesis.pdf
	for i in $(SRCDIRS); do $(MAKE) -C $$i $@; done;
