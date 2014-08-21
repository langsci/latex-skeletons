# specify your main target here:
all: lsp-skeleton.pdf

# specify teh main file and all the files that you are including
SOURCE= lsp-skeleton.tex chapters/01.tex chapters/02.tex chapters/03.tex\
localbibliography.bib\
LSP/langsci.cls
	 
%.pdf: %.tex $(SOURCE)
	xelatex -no-pdf lsp-skeleton 
	bibtex -min-crossrefs=200 lsp-skeleton
	xelatex  -no-pdf lsp-skeleton
	makeindex -o lsp-skeleton.ind lsp-skeleton.idx
	makeindex -o lsp-skeleton.lnd lsp-skeleton.ldx
#	makeindex -o lsp-skeleton.wnd lsp-skeleton.wdx
#	LSP/bin/reverse-index <lsp-skeleton.wdx >lsp-skeleton.rdx
#	makeindex -o lsp-skeleton.rnd lsp-skeleton.rdx 
	authorindex -i -p lsp-skeleton.aux > lsp-skeleton.bib.adx
	sed 's/|hyperpage//' lsp-skeleton.adx > lsp-skeleton.txt.adx 
	cat lsp-skeleton.bib.adx lsp-skeleton.txt.adx > lsp-skeleton.combined.adx
#	sed -e 's/}{/|hyperpage}{/g' lsp-skeleton.adx > lsp-skeleton.adx.hyp
	makeindex -o lsp-skeleton.and lsp-skeleton.combined.adx
	xelatex -no-pdf lsp-skeleton 
	xelatex lsp-skeleton 


cover: lsp-skeleton.pdf
	convert lsp-skeleton.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png

clean:
	rm -f *.bak *~ *.log *.blg *.aux *.toc *.cut *.out *.tmp *.tpm *.adx *.adx.hyp *.idx *.ilg \
	*.and *.glg *.glo *.gls *.wdx *.wnd *.wrd *.wdv *.ldx *.lnd *.rdx *.rnd *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf *.bbl
