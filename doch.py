# -*- coding: utf-8 -*-
import sys, time, os
from mechanize import Browser
import re
import pickle
LOGIN_URL = 'https://karty.vsb.cz/dochazka'
USERNAME = 'LOGIN'
PASSWORD = 'HESLO'
br = Browser()
br.open(LOGIN_URL)
br.select_form(nr=0)
br['username'] = USERNAME
br['password'] = PASSWORD
resp = br.submit()
html=resp.get_data().decode('windows-1250') 
#print html
if u'Jste evidován v docházce' in html:
    #prihlaseni = re.compile(u'jste začal (.*?) a přihlásil', re.DOTALL |  re.IGNORECASE).findall(html)
    prihlaseni = re.compile('al (.*?) a p', re.DOTALL |  re.IGNORECASE).findall(html)
    #verze = re.compile('<b>verze (.*?)</b>', re.DOTALL |  re.IGNORECASE).findall(resp.get_data())
#    print u'Přihlášen do docházky v %s' % prihlaseni[0]

    znamenko = re.compile(u'Dnes (.*?) hodin.<br>', re.DOTALL |  re.IGNORECASE).findall(html)
    if u'chybí' in znamenko[0]:
        znamenko[0]='-'
    else:
        znamenko[0]=''
    if u'chybí' in znamenko[1]:
        znamenko[1]='-'
    else:
        znamenko[1]=''
    rozdil = re.compile(u'span> (.*?) hodin.<br>', re.DOTALL |  re.IGNORECASE).findall(html)
#    print u'\tTýdenní rozdíl je %s%s' % (znamenko[0], rozdil[0])
#    print u'\tMěsíční rozdíl je %s%s' % (znamenko[1], rozdil[1])
#    print u'%s/T%s%s/M%s%s' % (prihlaseni[0], znamenko[0], rozdil[0], znamenko[1], rozdil[1])
    print u'%s/M%s%s' % (prihlaseni[0][:5], znamenko[1], rozdil[1])
else:
    print '**DOCHÁZKA**'
