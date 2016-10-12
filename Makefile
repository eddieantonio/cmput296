SRC = $(wildcard lab-*.md),
HTML = $(addsuffix .html,$(basename $(SRC)))
CSSFILE = simple.css

$(HTML):

install-hooks:
	ln -s ../../pre-commit.sh .git/hooks/pre-commit

%.html: %.md
	pandoc --standalone --smart --css $(CSSFILE) -o $@ $<
