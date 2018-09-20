"""
generate templatic emails for community proofreading

The LangSci ID of a book is given as the first argument of the command line. 

The author name to figure in the subject line is given as the second argument

The list of chapters is found in a file `chapternames` with one entry per line 

The matching of community proofreaders and chapters is made in a file `assignments`.
This file has one name (withouth spaces) and a list of chapternumbers per line. 
An example is "John 2 3 4"

The due date is set to 4 weeks from today.
"""
import sys
from datetime import datetime, date, time, timedelta
import os


template = """Dear  {name},
thanks for your offer. The book can be found at
https://paperhive.org/documents/remote?type=langsci&id={githubid} 

You are assigned the following chapters:
{chapterlist}

Please also have a look at the lists of references, in particular missing capitalization.

Next to the Paperhive online annotation platform, you can also download the pdf from http://langsci.github.io/{githubid}/proofreading.pdf if you prefer. Having the correction at Paperhive in a central place has proven much more convenient for the authors, but it is up to you to choose your preferred method of proofreading.

Guidelines for proofreaders can be found here
http://langsci-press.org/public/downloads/LangSci_Guidelines_Proofreaders.pdf

For most of the issues mentioned there, native competence is not necessary. We have every chapter checked by 2 people, at least one of which is a native speaker.

We aim at having the corrections in by {duedate}. Please let us know when you are done. 

Best wishes and thanks again for your help
Sebastian
"""


if __name__ == "__main__":
    githubid = sys.argv[1] 
    authorname = sys.argv[2] 

    chapters = ['0']+[l.strip() for l in open("chapternames").readlines()] #add dummy 0 to make chapters start with '1'
    assignments = open("assignments").readlines() 
    duedate=(datetime.now() + timedelta(weeks=4)).strftime("%B %d")
    
    for l in assignments:
        #parse the chapternames file
        name = l.split()[0]
        chapternumbers = l.split()[1:]
        #collate all assigned chapters
        chapterlist = '\n'.join("* %s %s"%(i,chapters[int(i)]) for i in chapternumbers)	
        #generate mail body
        mailbody = template.format(**locals()) 
        #launch mail program
        thunderbirdoptionstring = """-compose "to=%s,subject='proofreading %s',format=2,body='%s'" """%(name,authorname,mailbody) 
        os.system("thunderbird %s"%thunderbirdoptionstring)
            