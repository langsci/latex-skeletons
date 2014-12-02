# specify your main target here:
all: book pod cover

# specify thh main file and all the files that you are including
SOURCE= lsp-edskeleton.tex chapters/01.tex chapters/02.tex chapters/03.tex\
localbibliography.bib\
LSP/langsci.cls
	 
lsp-edskeleton.pdf: lsp-edskeleton.tex $(SOURCE)
	xelatex -no-pdf lsp-edskeleton 
	./bibtexvolume
	xelatex  -no-pdf lsp-edskeleton
	sed -i s/.*\\emph.*// lsp-edskeleton.adx #remove titles which biblatex puts into the name index
	makeindex -o lsp-edskeleton.and lsp-edskeleton.adx
	makeindex -o lsp-edskeleton.lnd lsp-edskeleton.ldx
	makeindex -o lsp-edskeleton.snd lsp-edskeleton.sdx
	xelatex -no-pdf lsp-edskeleton 
	xelatex lsp-edskeleton 

#create only the book
book: lsp-edskeleton.pdf 

#create a png of the cover
cover: lsp-edskeleton.pdf
	convert lsp-edskeleton.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png
	display cover.png

#extract the front cover, back cover and spine from the pdf	
triptychon: lsp-edskeleton.pdf#output=long has to be used for this to work
	pdftk A=lsp-edskeleton.pdf cat  A1  output front.pdf 
	pdftk A=lsp-edskeleton.pdf cat A2 output back.pdf 
	pdftk A=lsp-edskeleton.pdf cat A3 output spine.pdf

#prepare for print on demand services	
pod: bod createspace

#prepare for submission to BOD
bod: triptychon #output=long has to be used for this to work
	pdftk A=lsp-edskeleton.pdf B=blank.pdf cat B A4-end output tmp.pdf 
	./filluppages tmp.pdf bod/bodcontent.pdf
	\rm tmp.pdf
	xelatex bodcover.tex
	mv bodcover.pdf bod/

# prepare for submission to createspace
createspace: triptychon #output=long has to be used for this to work
	xelatex createspacecover.tex
	mv createspacecover.pdf createspace
	pdftk A=lsp-edskeleton.pdf B=blank.pdf cat B A4-end output createspace/createspacecontent.pdf

#housekeeping	
clean:
	rm -f *.bak *~ *.backup *.tmp \
	*.adx *.and *.idx *.ind *.ldx *.lnd *.sdx *.snd *.rdx *.rnd *.wdx *.wnd \
	*.log *.blg *.ilg \
	*.aux *.toc *.cut *.out *.tpm *.bbl *-blx.bib *_tmp.bib \
	*.glg *.glo *.gls *.wrd *.wdv *.xdv \
	*.run.xml 

realclean: clean
	rm -f *.dvi *.ps *.pdf 
