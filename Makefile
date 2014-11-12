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
	sed -i s/.*\\emph.*// lsp-skeleton.adx #remove titles which biblatex puts into the name index
	makeindex -o lsp-skeleton.and lsp-skeleton.adx
	makeindex -o lsp-skeleton.lnd lsp-skeleton.ldx
	makeindex -o lsp-skeleton.snd lsp-skeleton.sdx
	xelatex -no-pdf lsp-skeleton 
	xelatex lsp-skeleton 


cover: lsp-skeleton.pdf
	convert lsp-skeleton.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png
	display cover.png

bod: lsp-skeleton.pdf #output=long has to be used for this to work
	pdftk A=lsp-skeleton.pdf cat A1  output front.pdf 
	pdftk A=lsp-skeleton.pdf cat A2 output back.pdf 
	pdftk A=lsp-skeleton.pdf cat A3 output spine.pdf
	xelatex cover.tex
	mv cover.pdf bod
	pdftk A=lsp-skeleton.pdf B=blank.pdf cat B A4-end output bod/content.pdf

createspace: lsp-skeleton.pdf
	pdftk A=lsp-skeleton.pdf cat  A1  output front.pdf 
	pdftk A=lsp-skeleton.pdf cat A2 output back.pdf 
	pdftk A=lsp-skeleton.pdf cat A3 output spine.pdf
	xelatex cover.tex
	mv cover.pdf createspace
	pdftk A=lsp-skeleton.pdf B=blank.pdf cat B A4-end output createspace/content.pdf
	#put pdf and cover in folder

pod: bod createspace
	
clean:
	rm -f *.bak *~ *.backup *.tmp \
	*.adx *.and *.idx *.ind *.ldx *.lnd *.sdx *.snd *.rdx *.rnd *.wdx *.wnd \
	*.log *.blg *.ilg \
	*.aux *.toc *.cut *.out *.tpm *.bbl *-blx.bib\
	*.glg *.glo *.gls *.wrd *.wdv *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf 
