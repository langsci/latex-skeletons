# specify your main target here:
all: XeTeX_piteSaami_SDL.pdf

# specify teh main file and all the files that you are including
SOURCE= abbreviationsSDL.tex     derivationalMorphSDL.tex  listOfRecordingsSDL.tex  nounsSDL.tex           phraseTypesSDL.tex  pronounsSDL.tex             verbsSDL.tex acknowledgementsSDL.tex  hyphenationSDL.tex        morphWordformsSDL.tex    otherWordFormsSDL.tex  RecordingsInventorySDL.tex  XeTeX_piteSaami_SDL.tex adjectivesSDL.tex        introductionSDL.tex       newcommandsSDL.tex       phonologySDL.tex       syntaxSentencesSDL.tex\
PiteGrammarBibSDL.bib\
LSP/langsci.cls
	 
%.pdf: %.tex $(SOURCE)
	xelatex -no-pdf $* 
#	bibtex -min-crossrefs=200 $*
	xelatex -no-pdf $* 
#	bibtex -min-crossrefs=200 $*
#	xelatex  -no-pdf $*
#	makeindex -o $*.ind $*.idx
#	makeindex -o $*.lnd $*.ldx
#	makeindex -o $*.wnd $*.wdx
#	LSP/bin/reverse-index <$*.wdx >$*.rdx
#	makeindex -o $*.rnd $*.rdx
	\rm $*.adx
	authorindex -i -p $*.aux > $*.adx
	sed -e 's/}{/|hyperpage}{/g' $*.adx > $*.adx.hyp
	makeindex -o $*.and $*.adx.hyp
	xelatex -no-pdf $* 
	xelatex $* 


# http://stackoverflow.com/questions/10934456/imagemagick-pdf-to-jpgs-sometimes-results-in-black-background
cover: XeTeX_piteSaami_SDL.pdf
	convert $*.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png

# convert $*.pdf\[0\] -resize 486x -background white -alpha remove -bordercolor black -border 2  cover.png

# 204x303 with a 2x2 margin it has to be 200x299
#convert tmp.pdf\[0\] -resize x299 -background white -alpha remove -bordercolor black -border 2  -quality 100 cover.png

# does not seem to have any effect:
# http://www.imagemagick.org/script/command-line-options.php#quality

clean:
	rm -f *.bak *~ *.log *.blg *.aux *.toc *.cut *.out *.tmp *.tpm *.adx *.adx.hyp *.idx *.ilg \
	*.and *.glg *.glo *.gls *.wdx *.wnd *.wrd *.wdv *.ldx *.lnd *.rdx *.rnd *.xdv 

realclean: clean
	rm -f *.dvi *.ps *.pdf *.bbl

#clean:
#	rm -f *.bak *~ *.log *.blg *.bbl *.aux *.toc *.cut *.out *.tmp *.tpm *.adx *.adx.hyp *.idx *.ilg *.ind \
#	*.and *.glg *.glo *.gls *.wdx *.wnd *.wrd *.wdv *.ldx *.lnd *.rdx *.rnd *.xdv 
#
#realclean: clean
#	rm -f *.dvi *.ps *.pdf



