import glob
import re

lgs=open("languages4index").read().split('\n')
terms=open("terms4index").read().split('\n')[::-1]#reverse to avoid double indexing

files = glob.glob('chapters/*tex')
for f in files:
  c = open(f).read()  
  for lg in lgs:
    c = c.replace(lg,'\ili{%s}'%lg)
  for term in terms:
    c = re.sub('(?<!isi{)%s(?![\w}])'%term, '\isi{%s}'%term, c)
  outfile = open(f.replace('chapters','indexed'), 'w')
  outfile.write(c)
  outfile.close()
  
  
  