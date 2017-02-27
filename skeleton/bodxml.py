import  yaml
from datetime import datetime
from pyPdf import PdfFileReader

metadata = yaml.load(open('metadata.yaml','r')) 

template = """<?xml version="1.0" encoding="utf-8"?>
<BoD>
  <Header>
    <FromCompany>Language Science Press</FromCompany>
    <FromCompanyNumber>112345678</FromCompanyNumber>
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
try:
  authors = '\n'.join([authortemplate.format(*a) for a in metadata["creators"]["authors"]])
except TypeError:
  authors = '' 

editortemplate="""
      <Contributor>
        <ContributorRole>editor</ContributorRole>
        <ContributorName>{1}, {0}</ContributorName>
        <ContributorShortBio>{2}</ContributorShortBio>
      </Contributor>
"""

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
metadata['pagecount'] = PdfFileReader(open('Bookblock.pdf','rb')).getNumPages()
metadata['binding'] = 'PB'
metadata['back'] = ''
outputSC = template.format(**metadata)
metadata['isbn'] = metadata['isbns']['hardcover'].replace('-','')
metadata['isbnhc'] = metadata['isbns']['hardcover'].replace('-','')
metadata['binding'] = 'HC'
metadata['back'] = '<Back>rounded</Back>'
outputHC = template.format(**metadata)

hcxml = open("%s_MasteringOrder.xml"%metadata['isbnhc'],'w')
hcxml.write(outputHC)
hcxml.close()

scxml = open("%s_MasteringOrder.xml"%metadata['isbnsc'],'w')
scxml.write(outputSC)
scxml.close()