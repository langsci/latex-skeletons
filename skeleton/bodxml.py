import  yaml
from datetime import datetime
from pyPdf import PdfFileReader
import shutil
import zipfile

template = """<?xml version="1.0" encoding="utf-8"?>
<BoD>
  <Header>
    <FromCompany>Language Science Press</FromCompany>
    <FromCompanyNumber>110275446</FromCompanyNumber>
    <SentDate>{date}</SentDate>
    <SentTime>{time}</SentTime>
    <FromPerson>Sebastian Nordhoff</FromPerson>
    <FromEmail>sebastian.nordhoff@langsci-press.org</FromEmail>
  </Header>
  <MasteringOrder>
    <Product>
      <MasteringType>Upload</MasteringType>
      <EAN>{isbn}</EAN>
      {authorstring}
      {editorstring}
      <Title>{title}</Title>
      <Series>{series}, Bd. {seriesnumber}</Series>
      <EditionNumber>{edition}</EditionNumber>
      <PublicationDate>{date}</PublicationDate>
      <Blurb>{blurb}</Blurb>
      <Height>240</Height>
      <Width>170</Width>
      <Pages>{pagecount}</Pages>
      <ColouredPages>{colorpagecount}</ColouredPages>
      <ColouredPagesPosition>{colorpagesstring}</ColouredPagesPosition>
      
      <Paper>white</Paper>
      <Quality>Standard</Quality>
      <Binding>{binding}</Binding>
      {back}
      <Finish>matt</Finish>
      <Language>{booklanguage}</Language>
      <Subject Scheme="{scheme[0]}">{scheme[1]}</Subject>
      <InternationalDistribution>Yes</InternationalDistribution>      
      <Price>
        <PriceValue>{europrice}</PriceValue>
        <PriceCurrency>EUR</PriceCurrency>
      </Price>
      <Price>
        <PriceValue>{gbprice}</PriceValue>
        <PriceCurrency>GBP</PriceCurrency>
      </Price>
      <Price>
        <PriceValue>{usdprice}</PriceValue>
        <PriceCurrency>USD</PriceCurrency>
      </Price>
    </Product>
  </MasteringOrder>
</BoD>
"""
 
authortemplate="""
      <Contributor>
        <ContributorRole>author</ContributorRole>
        <ContributorName>{1}, {0}</ContributorName>
        <ContributorShortBio>{2}</ContributorShortBio>
      </Contributor>
"""


editortemplate="""
      <Contributor>
        <ContributorRole>editor</ContributorRole>
        <ContributorName>{1}, {0}</ContributorName>
        <ContributorShortBio>{2}</ContributorShortBio>
      </Contributor>
"""

print "extracting metadata"

metadata = yaml.load(open('metadata.yaml','r')) 
try:
  authors = '\n'.join([authortemplate.format(*a) for a in metadata["creators"]["authors"]])
except TypeError:
  authors = '' 

try:
  editors= '\n'.join([editortemplate.format(*a) for a in metadata["creators"]["editors"]])
except TypeError:
  editors = ''
  
metadata['authorstring'] = authors
metadata['editorstring'] = editors  
metadata['date'] = '{:%Y%m%d}'.format(datetime.now())
metadata['time'] = '{:%H:%M}'.format(datetime.now())
metadata['isbn'] = metadata['isbns']['softcover'].replace('-','')
metadata['isbnsc'] = metadata['isbns']['softcover'].replace('-','')

metadata['colorpagecount'] = len(metadata['colorpages'])
metadata['colorpagesstring'] = ','.join([str(x) for x in metadata['colorpages']])  
metadata['pagecount'] = PdfFileReader(open('bodcontent.pdf','rb')).getNumPages()
#price is 3 EUR base + 5ct per page + 50ct extra per colorpage, rounded up to multiples of 5
metadata['europrice'] = "%i.%s" %(((300+metadata['pagecount']*5+metadata['colorpagecount']*30)/500+1)*5,"00")
metadata['gbprice'] = metadata['europrice']
metadata['usdprice'] = metadata['europrice'] 
metadata['binding'] = 'PB'
metadata['back'] = ''
outputSC = template.format(**metadata)
metadata['isbn'] = metadata['isbns']['hardcover'].replace('-','')
metadata['isbnhc'] = metadata['isbns']['hardcover'].replace('-','')
#Hardcover is always 10 EUR more than softcover
metadata['europrice'] = "%i.%s" %(((1300+metadata['pagecount']*5+metadata['colorpagecount']*30)/500+1)*5,"00")
metadata['gbprice'] = metadata['europrice']
metadata['usdprice'] = metadata['europrice'] 
metadata['binding'] = 'HC'
metadata['back'] = '<Back>rounded</Back>'
outputHC = template.format(**metadata)

print "Creating xml file for softcover", metadata['isbnsc']

scxml = open("bod/%s_MasteringOrder.xml"%metadata['isbnsc'],'w')
scxml.write(outputSC)
scxml.close()

print "Creating xml file for hardcover", metadata['isbnhc']
hcxml = open("bod/%s_MasteringOrder.xml"%metadata['isbnhc'],'w')
hcxml.write(outputHC)
hcxml.close()
 
print "renaming pdf files according to ISBNs"
shutil.copy('Bookblock.pdf','bod/%s_Bookblock.pdf'%metadata['isbnsc'])
shutil.copy('Bookblock.pdf','bod/%s_Bookblock.pdf'%metadata['isbnhc'])
shutil.copy('coverSC.pdf','bod/%s_cover.pdf'%metadata['isbnsc'])
shutil.copy('coverHC.pdf','bod/%s_coverHC.pdf'%metadata['isbnhc'])

print "Creating zip file for softcover", metadata['isbnsc']
zfsc = zipfile.ZipFile('bod/%s_MasteringOrder.zip'%metadata['isbnsc'], mode='w')
zfsc.write('bod/%s_MasteringOrder.xml'%metadata['isbnsc'])
zfsc.write('bod/%s_Bookblock.pdf'%metadata['isbnsc'])
zfsc.write('bod/%s_cover.pdf'%metadata['isbnsc'])
zfsc.close()


print "Creating zip file for hardcover", metadata['isbnhc'] 
zfhc = zipfile.ZipFile('bod/%s_MasteringOrder.zip'%metadata['isbnhc'], mode='w')
zfhc.write('bod/%s_MasteringOrder.xml'%metadata['isbnhc'])
zfhc.write('bod/%s_Bookblock.pdf'%metadata['isbnhc'])
zfhc.write('bod/%s_coverHC.pdf'%metadata['isbnhc'])
zfhc.close()

print "All files created. Files are in /bod"


#hardcover + 10