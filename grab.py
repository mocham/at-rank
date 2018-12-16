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
        'hermes-conrad',
        'mythic-stewie',
        'mythic-quagmire',
        'mythic-brian',
        'mythic-stan',
        'mythic-bullock',
        'mythic-hayley',
        'mythic-louise',
        'mythic-bob',
        'mythic-teddy',
        'mythic-peggy',
        'mythic-boomhauer',
        'mythic-dale',
        'mythic-leela',
        'mythic-dr-zoidberg',
        'mythic-professor-farnsworth',
        'mythic-bender',
        ]

class at_card:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp
        self.trait = 'none'
        self.skills = []
        self.slug = ''
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
    rarity = ''
    for card in cards:
        index += 1
        if index % 3 == 1:
            continue
        if index % 3 == 2:
            rarity = card.attrib['rarity']
            continue
        if rarity != 'legendary':
            continue
        atcd = at_card(int(card.find('cb-stats')[0].text),
                int(card.find('cb-stats')[1].text))
        atcd.slug = card.attrib['slug']
        if 'trait' in card.attrib:
            atcd.trait = card.attrib['trait']
        for node in card.find('cb-skills'):
            try:
                value = int(node.text)
                if 'target' in node.attrib:
                    if node.attrib['targer'] == 'trait':
                        value = 0.4 * value
                    if node.attrib['targer'] == 'show':
                        value = 0.3 * value
                    #print(node.attrib['target'])
                atcd.skills.append([node.attrib['type'], value])
            except:
                continue
        atcds.append(atcd)
    data[ch] = atcds

for ch in chs:
    analyse(ch)

with open('combos', 'wb') as f:
    pickle.dump(data, f)

