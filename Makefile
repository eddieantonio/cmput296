SRC = $(wildcard lab-*.md),
HTML = $(addsuffix .html,$(basename $(SRC)))
CSSFILE = simple.css

$(HTML):

%.html: %.md
	pandoc --standalone --smart --css $(CSSFILE) -o $@ $<
