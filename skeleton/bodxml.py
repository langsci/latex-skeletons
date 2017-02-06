template = """<?xml version="1.0" encoding="utf-8"?>
<BoD>
  <Header>
    <FromCompany>Language Science Press</FromCompany>
    <FromCompanyNumber>112345678</FromCompanyNumber>
    <SentDate>20140217</SentDate>
    <SentTime>11:00</SentTime>
    <FromPerson>Sebastian Nordhoff</FromPerson>
    <FromEmail>sebastian.nordhoff@langsci-press.org</FromEmail>
  </Header>
  <MasteringOrder>
    <Product>
      <MasteringType>Upload</MasteringType>
      <EAN>{isbn13}</EAN>
      <Contributor>
        <ContributorRole>{creatortype}</ContributorRole>
        <ContributorName>{creatorlastname}, {creatorfirstname}</ContributorName>
        <ContributorShortBio>{biosketch}</ContributorShortBio>
      </Contributor>
      <Title>{booktitle}</Title>
	  <Series>{series}, Bd. {Series Number}</Series>
	  <EditionNumber>{edition}</EditionNumber>
	  <PublicationDate>20140226</PublicationDate>
	  <Blurb>{blurb}</Blurb>
      <Height>240</Height>
      <Width>170</Width>
      <Pages>{pagecount}</Pages>
      <ColouredPages>{colorpages}</ColouredPages>
      <Paper>white</Paper>
	  <Quality>Standard</Quality>
	  <Binding>{covertype}</Binding>
      <Finish>matt</Finish>
      <Language>{booklanguage}</Language>
      <Subject Scheme="WGS">1111</Subject>
	  	  <Price>
        <PriceValue>{europrice}</PriceValue>
        <PriceCurrency>EUR</PriceCurrency>
      </Price>
	  </Product>
  </MasteringOrder>
</BoD>
""" 
