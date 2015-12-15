import re
from initd import INITD

  
orig = ''
trans = ''

for k in INITD:
  s = INITD[k]
  for c in s:
    orig+=c
    trans+=k
     
transtable = str.maketrans(orig, trans)

p = re.compile(r"\\indexentry \{(.*)\|hyperpage")

    
def process(s): 
  m = p.match(s) 
  o = m.groups(1)[0]
  t = o.translate(transtable)
  if t == o:
    return s
  else:
    return s.replace(o,"%s@%s"%(o,t))
  
  

if __name__ == '__main__':
  fn = 'main.adx'
  lines = open(fn).readlines()
  print(len(lines))
  lines2 = list(map(process, lines))
  print(lines2)
  