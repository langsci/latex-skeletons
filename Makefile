# specify your main target here:
all: book 

# specify thh main file and all the files that you are including
SOURCE= lsp-skeletonnofonts.tex chapters/01.tex chapters/02.tex chapters/03.tex\
localbibliography.bib\
LSP/langsci.cls
	 
%.pdf: %.tex $(SOURCE)
	xelatex -no-pdf lsp-skeletonnofonts 
	bibtex -min-crossrefs=200 lsp-skeletonnofonts
	xelatex  -no-pdf lsp-skeletonnofonts
	sed -i s/.*\\emph.*// lsp-skeletonnofonts.adx #remove titles which biblatex puts into the name index
	makeindex -o lsp-skeletonnofonts.and lsp-skeletonnofonts.adx
	makeindex -o lsp-skeletonnofonts.lnd lsp-skeletonnofonts.ldx
	makeindex -o lsp-skeletonnofonts.snd lsp-skeletonnofonts.sdx
	xelatex -no-pdf lsp-skeletonnofonts 
	xelatex lsp-skeletonnofonts 

#create only the book
book: lsp-skeletonnofonts.pdf 

#housekeeping	
clean:
	rm -f *.bak *~ *.backup *.tmp \
	*.adx *.and *.idx *.ind *.ldx *.lnd *.sdx *.snd *.rdx *.rnd *.wdx *.wnd \
	*.log *.blg *.ilg \
	*.aux *.toc *.cut *.out *.tpm *.bbl *-blx.bib \
	*.glg *.glo *.gls *.wrd *.wdv *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf 
