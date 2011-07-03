SRCDIRS = src
GENTARGETS = all clean show show-chromium

$(GENTARGETS): $(SRCDIRS)
	#Make recursion
	$(MAKE) -C $< $@

show: all
	see src/slides.html


