#!/bin/bash
pagecount=$(pdftk main.pdf dump_data|grep NumberOfPages| awk '{print $2}')

cswidth=`echo $pagecount*0.0572008|bc`
echo $pagecount
echo $cswidth
sed -i s/spinewidth=\[0-9\.\]*/spinewidth=$cswidth/ createspacecover.tex
xelatex createspacecover
xelatex createspacecover
okular createspacecover.pdf


# bodscwith=$()
# bodhcwith=$()
