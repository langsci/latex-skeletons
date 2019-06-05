chapternumber=0 
offset=$1
offset=$(($offset-1))
old=1
for pagenumber in `cat cuts.txt`
do 
new=$(($pagenumber+offset))
echo $i $old-$(($new-1))
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
    -dFirstPage=$old -dLastPage=$(($new-1)) \
    -sOutputFile=$chapternumber.pdf main.pdf
old=$new
chapternumber=$(($chapternumber+1))
done
