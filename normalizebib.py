import sys
import re
import pprint

keys = {}
class Record(): 
  TYPKEYFIELDS = r"^([^\{]+)\{([^,]+),[\s\n\t]*((?:.|\n)*)\}"
  def __init__(self,s):  
    #print(s)
    m = re.match(self.TYPKEYFIELDS,s)
    self.typ = m.group(1).lower()
    self.key = m.group(2)
    try: 
      self.fields = dict((tp[0].strip()\
          .replace('\n',' ')\
          .replace('\t',' '),
          tp[1].strip()\
          .replace('\n',' ')\
          .replace('\t',' ')
            ) for tp in [re.split('\s*=\s*',t,maxsplit=1) 
        for t in re.split('(?<=\})\s*,\s*\n',
              m.group(3).strip()
              )
        ]
            )
    except IndexError:
      print(s)
    self.errors = []
    if self.key in keys:
      self.errors.append("duplicate key %s"% self.key)
    keys[self.key] = True
    self.conform()
    self.report()
    
  def conform(self):
    if self.fields.get('editor') != None and self.fields.get('booktitle') == None:
      self.fields['booktitle'] = self.fields['title'] 
    pages = self.fields.get('pages')
    if pages != None: 
      self.fields['pages'] = re.sub(r'([0-9])-([0-9])',r'\1--\2',pages)
		 
    self.conformsubtitles()
    self.conforminitials()
    self.checkand()
    self.checkbook()
    self.checkarticle()
    self.checkincollection()
  
  def report(self):
    if len(self.errors)>0: 
      print(self.key,'\n  '.join(['  ']+self.errors))
 
      
  def upperme(self,match):
    return match.group(1) + ' {' +match.group(2).upper()+'}'

 
      
  def conformsubtitles(self):
    for t in ('title','booktitle'):
      if self.fields.get(t) != None: 
        self.fields[t] = re.sub(r'([:\.\?!]) *([a-zA-Z])', self.upperme ,self.fields[t])
      
  def conforminitials(self):
    for t in ('author','editor'):
      if self.fields.get(t) != None: 
        self.fields[t] = re.sub(r'([A-Z])\.([A-Z])', r'\1. \2',self.fields[t])
        
  def checkand(self):
    for t in ('author','editor'):
      if self.fields.get(t) != None: 
        ands = self.fields[t].count(' and ')
        commas = self.fields[t].count(',')
        if commas > ands +1:
          print(self.key, self.fields[t])
          
  def checkbook(self):
    if self.typ != 'book':
      return 
    mandatory = ('year', 'title', 'address', 'publisher')
    for m in mandatory:
      self.handleerror(m)
    if self.fields.get('series') != None: 
      number = self.fields.get('number')
      volume = self.fields.get('volume')
      if volume != None:
        if number == None:
          self.fields['number'] = volume
          del self.fields['volume'] 
    if self.fields.get('author') ==  None:
      if  self.fields.get('editor') ==  None:
        print("neither author nor editor")        
    if self.fields.get('author') !=  None:
      if  self.fields.get('editor') !=  None:
        print("both author and editor")
        
      
  def checkarticle(self):
    if self.typ != 'article':
      return 
    mandatory = ('author', 'year', 'title', 'journal', 'volume', 'pages')
    for m in mandatory:
      self.handleerror(m)
      
  def checkincollection(self):
    if self.typ != 'incollection':
      return 
    mandatory = ('author', 'year', 'title', 'pages')
    for m in mandatory:
      self.handleerror(m)
    if self.fields.get('crossref'):
      return
    mandatory2 = ('booktitle', 'editor', 'publisher', 'address')
    for m2 in mandatory2:
      self.handleerror(m2)
        
      
  def handleerror(self,m):
      if self.fields.get(m) == None:
        self.fields[m] = r"\biberror{no %s}" % m
        self.errors.append("missing %s"%m) 
      
		
    
    
  def bibtex(self): 
    s = """@%s{%s,\n\t%s\n}"""%(self.typ,
																self.key,",\n\t".join(
																									["%s = %s" %(f,self.fields[f]) 
																									for f in sorted(self.fields.keys())]
																									)
															)
    return s
    


if __name__ == "__main__":    
  inbib = open(sys.argv[1])
  outbib = open('sorted.bib','w')

  a = inbib.read().split('\n@') 
  p = a[0]
  r = a[1:] 
  r.sort() #in order to get the order of edited volumes and incollection right
  new = ',\n\n'.join([Record(q).bibtex() for q in r[::-1]]) 
  #print(new)
  inbib.close()
  outbib.write(p)
  outbib.write('\n')
  outbib.write(new)
  outbib.close()
