import sys
author = sys.argv[1]
booktitle = sys.argv[2]

template = """Dear  {name},
thanks for your offer. The book can be found at
http://www.glottotopia.org/{author}/{booktitle}.pdf

You are assigned the following chapters:
{chapterlist}

These can be found at
{linklist}

You can either proofread locally and send the corrections in your
preferred format, or you can use the online annotation available at

{orlist}

Guidelines for proofreaders can be found here
http://langsci-press.org/public/downloads/LangSci_Guidelines_Proofreaders.pdf

Guidelines for online annotation can be found here
http://langsci-press.org/openReview/userGuide

We aim at having the corrections in by Monday February 15

Best wishes and thanks again for your help
Sebastian
"""

chapters = ['0']+[l.strip() for l in open("chapternames").readlines()]
assignments = open("assignments").readlines()

mails = []

for a in assignments:
	name = a.split()[0]
	chapternumbers = a.split()[1:]
	chapterlist = '\n'.join("%s %s"%(i,chapters[int(i)]) for i in chapternumbers)
	linklist  = '\n'.join(["http://www.glottotopia.org/%s/%s.pdf"%(author,i) for i in chapternumbers])
	orlist  = "\n".join(["https://via.hypothes.is/http://www.glottotopia.org/%s/%s.pdf"%(author,i) for i in chapternumbers])
	mails.append(template.format(name=name, author=author,booktitle=booktitle,chapterlist=chapterlist,linklist=linklist,orlist=orlist))
	
separator =	'\n'+80*'-'+'\n'
print separator.join(mails)
