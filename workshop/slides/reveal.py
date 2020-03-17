# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-01 10:17
# modified : 2015-07-01 10:17
"""
Compile slides from simple markdown syntax.
"""

__author__="Johann-Mattis List"
__date__="2015-07-01"

from markdown import markdown
import sys
import re

template = open('templates/template.html').read()
style = open('templates/template.css').read()
script = open('templates/template.js').read()

if len(sys.argv) == 1:
    print("Usage: python reveal.py INFILE")
    sys.exit()

# get the title from the slide
infile = open(sys.argv[1]).read()
title = infile[:infile.index('\n')].replace('# ','')
infile = infile[infile.index('\n'):]

# convert stuff
def convert(md):

    md = markdown(md, extensions=['markdown.extensions.tables'])

    md = re.sub(r'@([a-z]*):"([^"]*)"',r'<span class="\1">\2</span>', md)

    patterns = [
            (':bib:','http://bibliography.lingpy.org?key='),
            (':wiki:', 'http://de.wikipedia.org/wiki/')
            ]
    for s,t in patterns:
        md = md.replace(s,t)

    regexes = [
            (':([a-z\-A-Z_ ]*): (.*) ::', r'<span class="\1">\2</span>'),
            ]
    for s,t in regexes:
        md = re.sub(s, t, md, re.DOTALL)

    return md

# we split the infile according to sections
slides = infile.split('\n---\n')

# get global settings
mysetup = {}
for line in slides[0].split('\n'):
    if line.startswith('@'): 
        k,v = line[1:line.index(':')], ':'.join(line.split(':')[1:])
        if k in ['style'] and k in mysetup:
            mysetup[k] += v
        else:
            mysetup[k] = v

text = ''
for slide in slides[1:]:

    inslides = slide.split('\n--\n')
    
    if len(inslides) == 1:
        slide_text = ''
        slide_anno = mysetup.copy()
        for line in slide.split('\n'):
            if line.startswith('@'):
                k,v = line[1:line.index(':')], ':'.join(line.split(':')[1:])
                if k in ['style'] and k in slide_anno:
                    slide_anno[k] += v
                else:
                    slide_anno[k] = v
            else:
                slide_text += line+'\n'
        if slide_anno:
            anno_text = ' '.join(['{0}="{1}"'.format(k,v) for k,v in
                slide_anno.items()])
        else:
            anno_text = ''

        text += '<section '+anno_text+'>\n'+convert(slide_text)+'\n</section>\n\n'
    else:
        text += '<section>\n'
        for inslide in inslides:
            slide_text = ''
            slide_anno = mysetup.copy()
            for line in inslide.split('\n'):
                if line.startswith('@'):
                    k,v = line[1:line.index(':')], ':'.join(line.split(':')[1:])
                    if k in ['style'] and k in slide_anno:
                        slide_anno[k] += v
                    else:
                        slide_anno[k] = v
                else:
                    slide_text += line+'\n'

            if slide_anno:
                anno_text = ' '.join(['{0}="{1}"'.format(k,v) for k,v in
                    slide_anno.items()])
            else:
                anno_text = ''

            text += '<section '+anno_text+'>\n'+convert(slide_text)+'\n</section>\n'
        text += '</section>\n\n'

with open(sys.argv[1].split('/')[-1].replace('.md','.html'), 'w') as f:
    f.write(template.format(SLIDES=text, TITLE=title, SCRIPT=script, STYLE=style))
print("Finished compiling your slide.")

