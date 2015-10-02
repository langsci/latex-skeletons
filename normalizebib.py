inbib = open('localbibliography.bib')
outbib = open('sorted.bib','w')

r = inbib.read().split('\n@')
inbib.close()
r.sort()
outbib.write('\n@'.join(r[::-1]))
outbib.close()