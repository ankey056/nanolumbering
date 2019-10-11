

INPUTDIR=input
OUTPUTDIR=output
PERFORM=./source/perform.py
LEARN=./source/learning.py
LMODELDIR=./learning/model


all: $(LMODELDIR)/table.txt
	mkdir $(OUTPUTDIR)/
	$(PERFORM) $(INPUTDIR)/ $(OUTPUTDIR)/


learning: $(LMODELDIR)/table.txt

$(LMODELDIR)/table.txt: $(LMODELDIR)/methods-list.txt
	cat $< | $(LEARN) > $@
	cat $@

.PHONY: learning clean

clean:
	rm -f $(OUTPUTDIR)/* $(LMODELDIR)/table.txt
	find ./source -type f -iname '*.pyc' -delete
