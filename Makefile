TEX = $(wildcard src/*.tex)
PDF = $(UI:.tex=.pdf)
RST=$(wildcard src/*.rst)
HTMLTARGET = $(RST:.rst=.html)
SLAG = $(wildcard src/*.out src/*.log src/*.aux src/*.nav src/*.snm src/*.toc) $(HTMLTARGET)

all: $(PDF) $(HTMLTARGET)

%.html: %.rst
	landslide $< > $@

$(PDF): $(TEX)

%.pdf: %.tex
	pdflatex $<

clean-build:
	-rm $(SLAG)

clean: clean-build

trailing-spaces:
	find -name "*.rst" | xargs sed -i 's/[ \t]*$$//'
	find -name "*.tex" | xargs sed -i 's/[ \t]*$$//'

