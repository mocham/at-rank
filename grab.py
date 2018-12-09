from urllib.request import urlopen
import os
import pickle
from lxml import etree
from lxml.html import tostring, fromstring
from selenium import webdriver

chs = ['bill-dauterive',
        'philip-j-fry',
        'dr-amy-wong',
        'eugene-belcher',
        'chris-griffin',
        'meg-griffin',
        'hank-hill',
        'bender',
        'steve-smith',
        'peter',
        'roger',
        'tina',
        'linda-belcher',
        'klaus-heisler',
        'bobby',
        'lois-griffin',
        'hermes-conrad'
        ]

class at_card:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp
        self.trait = 'none'
        self.skills = []
    def prt(self):
        print([self.atk, self.hp, self.trait, self.skills])

data = {}
def analyse(ch):
    fn = 'html/' + ch + '.html'
    if os.path.exists(fn):
        with open(fn, 'r') as f:
            lns = f.readlines()
            src = ''
            for x in lns:
                src += x
    else:
        driver = webdriver.PhantomJS()
        driver.get('https://cartoon-battle.cards/recipes?' + ch)
        with open(fn, 'w') as f:
            f.write(driver.page_source)
        src = driver.page_source
    tree = etree.HTML(src)
    cards = tree.xpath('//cb-card')
    atcds = []
    index = 0
    for card in cards:
        index += 1
        if index % 3 == 1:
            continue
        if index % 3 == 2:
            continue
        atcd = at_card(int(card.find('cb-stats')[0].text),
                int(card.find('cb-stats')[1].text))
        if 'trait' in card.attrib:
            atcd.trait = card.attrib['trait']
        for node in card.find('cb-skills'):
            try:
                atcd.skills.append([node.attrib['type'], int(node.text)])
            except:
                continue
        atcd.prt()
        atcds.append(atcd)
    data[ch] = atcds

for ch in chs:
    analyse(ch)

with open('combos', 'wb') as f:
    pickle.dump(data, f)

