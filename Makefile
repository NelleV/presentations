
all: build

build:
	find . -name "*.tex" | xargs pdflatex

clean-build:
	find . -name "*.out" | xargs rm -rf
	find . -name "*.log" | xargs rm -rf
	find . -name "*.aux" | xargs rm -rf
	find . -name "*.nav" | xargs rm -rf
	find . -name "*.snm" | xargs rm -rf
	find . -name "*.toc" | xargs rm -rf

clean: clean-build

trailing-spaces:
	find -name "*.rst" | xargs sed -i 's/[ \t]*$$//'
	find -name "*.tex" | xargs sed -i 's/[ \t]*$$//'

