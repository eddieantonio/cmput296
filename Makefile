SRC = $(wildcard lab-*.md)
HTML = $(addsuffix .html,$(basename $(SRC)))
PDF = $(addsuffix .pdf,$(basename $(SRC)))
CSSFILE = simple.css

# Explicitly set to correct DPI
# https://github.com/wkhtmltopdf/wkhtmltopdf/issues/3241
DPI := $(shell dc -e '96 4 * p')

.PHONY: all
all: html pdf

.PHONY: html
html: $(HTML)

.PHONY: pdf
pdf: $(PDF)

.PHONY: install-hooks
install-hooks:
	ln -sf ../../pre-commit.sh .git/hooks/pre-commit

%.html: %.md
	pandoc --standalone --css $(CSSFILE) -o $@ $<
	@sh -c 'for i in $*/*.py; do [ -f "$$i" ] && openssl dgst -sha256 "$$i"; done || true'

%.py:
	openssl dgst -256 $@


%.pdf: %.html simple.css
	wkhtmltopdf --page-size letter --print-media-type --dpi $(DPI) $< $@
