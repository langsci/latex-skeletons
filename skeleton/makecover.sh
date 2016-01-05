#!/usr/bin/bash

series=$1
number=$2
author=$3
title=$4
subtitle=$5

cp localmetadata.tex localmetadata.tex~

echo "\author{$3}">> localmetadata.tex
echo "\title{$4}">> localmetadata.tex
echo "\subtitle{$5}">> localmetadata.tex
echo "\renewcommand{\lsSeries}{$1}">> localmetadata.tex 
echo "\renewcommand{\lsSeriesNumber}{$2}">> localmetadata.tex  

rm main.pdf
make pdf
make cover
mv localmetadata.tex~ localmetadata.tex