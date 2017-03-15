#!/bin/bash
pagecount=$(pdftk main.pdf dump_data|grep NumberOfPages| awk '{print $2}')

cswidth=`echo $pagecount*0.0572008|bc`
bodscwidth=`echo $pagecount*0.052571428571|bc`
bodhcwidth=`echo $bodscwidth+6|bc`
echo $pagecount
echo $cswidth
echo $bodscwidth
echo $bodhcwidth

sed -i s/spinewidth=\[0-9\.\]*/spinewidth=$cswidth/ createspacecover.tex
xelatex createspacecover
xelatex createspacecover
okular createspacecover.pdf &

sed -i s/spinewidth=\[0-9\.\]*/spinewidth=$bodscwidth/ bodcoverSC.tex
xelatex bodcoverSC.tex
xelatex bodcoverSC.tex
okular bodcoverSC.pdf &

sed -i s/spinewidth=\[0-9\.\]*/spinewidth=$bodhcwidth/ bodcoverHC.tex
xelatex bodcoverHC.tex
xelatex bodcoverHC.tex
okular bodcoverHC.pdf

 