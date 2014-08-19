# specify your main target here:
all: lsp-edskeleton.pdf

# specify teh main file and all the files that you are including
SOURCE= chapters/01.tex chapters/02.tex chapters/03.tex\
localbibliography.bib\
LSP/langsci.cls
	 
%.pdf: %.tex $(SOURCE)
	xelatex -no-pdf $* 
	bibtex -min-crossrefs=200 $*
	xelatex  -no-pdf $*
	makeindex -o $*.ind $*.idx
	makeindex -o $*.lnd $*.ldx
#	makeindex -o $*.wnd $*.wdx
#	LSP/bin/reverse-index <$*.wdx >$*.rdx
#	makeindex -o $*.rnd $*.rdx
	\rm $*.adx
	authorindex -i -p $*.aux > $*.adx
#	sed -e 's/}{/|hyperpage}{/g' $*.adx > $*.adx.hyp
	makeindex -o $*.and $*.adx.hyp
	xelatex -no-pdf $* 
	xelatex $* 


cover: lsp-collection.pdf
	convert $*.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png

clean:
	rm -f *.bak *~ *.log *.blg *.aux *.toc *.cut *.out *.tmp *.tpm *.adx *.adx.hyp *.idx *.ilg \
	*.and *.glg *.glo *.gls *.wdx *.wnd *.wrd *.wdv *.ldx *.lnd *.rdx *.rnd *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf *.bbl
