# specify your main target here:
all: lsp-skeletonnofonts.pdf

# specify teh main file and all the files that you are including
SOURCE= lsp-skeletonnofonts.tex chapters/01.tex chapters/02.tex chapters/03.tex\
localbibliography.bib\
LSP/langsci.cls
	 
%.pdf: %.tex $(SOURCE)
	xelatex -no-pdf lsp-skeletonnofonts 
	bibtex -min-crossrefs=200 lsp-skeletonnofonts
	xelatex  -no-pdf lsp-skeletonnofonts
	makeindex -o lsp-skeletonnofonts.ind lsp-skeletonnofonts.idx
	makeindex -o lsp-skeletonnofonts.lnd lsp-skeletonnofonts.ldx
#	makeindex -o lsp-skeletonnofonts.wnd lsp-skeletonnofonts.wdx
#	LSP/bin/reverse-index <lsp-skeletonnofonts.wdx >lsp-skeletonnofonts.rdx
#	makeindex -o lsp-skeletonnofonts.rnd lsp-skeletonnofonts.rdx 
	authorindex -i -p lsp-skeletonnofonts.aux > lsp-skeletonnofonts.bib.adx
	sed 's/|hyperpage//' lsp-skeletonnofonts.adx > lsp-skeletonnofonts.txt.adx 
	cat lsp-skeletonnofonts.bib.adx lsp-skeletonnofonts.txt.adx > lsp-skeletonnofonts.combined.adx
#	sed -e 's/}{/|hyperpage}{/g' lsp-skeletonnofonts.adx > lsp-skeletonnofonts.adx.hyp
	makeindex -o lsp-skeletonnofonts.and lsp-skeletonnofonts.combined.adx
	xelatex -no-pdf lsp-skeletonnofonts 
	xelatex lsp-skeletonnofonts 


cover: lsp-skeletonnofonts.pdf
	convert lsp-skeletonnofonts.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png
	display cover.png

bodcover: lsp-skeletonnofonts.pdf
	pdftk A=lsp-skeletonnofonts.pdf cat  A1  output front.pdf 
	pdftk A=lsp-skeletonnofonts.pdf cat A2 output back.pdf 
	pdftk A=lsp-skeletonnofonts.pdf cat A3 output spine.pdf
	xelatex cover.tex

 

clean:
	rm -f *.bak *~ *.log *.blg *.aux *.toc *.cut *.out *.tmp *.tpm *.adx *.adx.hyp *.idx *.ilg \
	*.and *.glg *.glo *.gls *.wdx *.wnd *.wrd *.wdv *.ldx *.lnd *.rdx *.rnd *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf *.bbl
