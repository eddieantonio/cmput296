SRC = $(wildcard lab-*.md)
HTML = $(addsuffix .html,$(basename $(SRC)))
PDF = $(addsuffix .pdf,$(basename $(SRC)))
CSSFILE = simple.css

.PHONY: all
all: html pdf

.PHONY: html
html: $(HTML)

.PHONY: pdf
pdf: $(PDF)

.PHONY: install-hooks
install-hooks:
	ln -s ../../pre-commit.sh .git/hooks/pre-commit

%.html: %.md
	pandoc --standalone --smart --css $(CSSFILE) -o $@ $<

%.pdf: %.html
	wkhtmltopdf --page-size letter --print-media-type $< $@
