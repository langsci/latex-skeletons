chapternumber=0 
offset=$1
offset=$(($offset-1))
old=1
for pagenumber in `cat cuts.txt`
do 
new=$(($pagenumber+offset))
echo $i $old-$(($new-1))
qpdf --pages main.pdf $old-$(($new-1)) -- main.pdf $chapternumber.pdf 
old=$new
chapternumber=$(($chapternumber+1))
done
