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
	sed -i s/.*\\emph.*// lsp-skeleton.adx
	makeindex -o lsp-skeleton.and lsp-skeleton.adx
	makeindex -o lsp-skeleton.lnd lsp-skeleton.ldx
	makeindex -o lsp-skeleton.snd lsp-skeleton.sdx
	xelatex -no-pdf lsp-skeleton 
	xelatex lsp-skeleton 


cover: lsp-skeleton.pdf
	convert lsp-skeleton.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png
	display cover.png

bodcover: lsp-skeleton.pdf
	pdftk A=lsp-skeleton.pdf cat  A1  output front.pdf 
	pdftk A=lsp-skeleton.pdf cat A2 output back.pdf 
	pdftk A=lsp-skeleton.pdf cat A3 output spine.pdf
	xelatex cover.tex

 

clean:
	rm -f *.bak *~ *.log *.blg *.aux *.toc *.cut *.out *.tmp *.tpm *.adx *.adx.hyp *.idx *.ilg \
	*.and *.glg *.glo *.gls *.wdx *.wnd *.wrd *.wdv *.ldx *.lnd *.rdx *.rnd *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf *.bbl
