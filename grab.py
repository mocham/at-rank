from urllib.request import urlopen
import os
import pickle
from lxml import etree
from lxml.html import tostring, fromstring
import json
from selenium import webdriver


skill_dict = {
    'bodyguard': 'bodyguard',
    'inspire': 'motivate',
    'pierce': 'jab',
    'poison': 'gas',
    'strike': 'punch',
    'armored': 'sturdy',
    'berserk': 'crazed',
    'outlast': 'recover',
    'invigorate': 'boost',
    'counter': 'payback',
    'weaken': 'cripple',
    'leech': 'leech',
    'weakenall': 'cripple-all',
    'barrier': 'shield',
    'barrierall': 'shield-all',
    'rallyall': 'cheer-all',
    'rally': 'cheer',
    'heal': 'heal',
    'healall': 'heal-all',
    'shrapnel': 'bomb',
    'hijack': 'hijack',
}


downgrade_dict = {}
upgrade_dict = {
    'bullock': 'mythic-bullock',
    'chris': 'chris-griffin',
    'dale': 'mythic-dale',
    'dr-zoidberg': 'mythic-dr-zoidberg',
    'fry': 'philip-j-fry',
    'hank': 'hank-hill',
    'linda': 'linda-belcher',
    'lois': 'lois-griffin',
    'steve': 'steve-smith',
    'bill': 'bill-dauterive',
    'gene': 'eugene-belcher',
    'hayley': 'mythic-hayley',
    'hermes': 'hermes-conrad',
    'klaus': 'klaus-heisler',
    #'luanns': 
    'meg': 'meg-griffin',
    'professor-farnsworth': 'mythic-professor-farnsworth',
    'quagmire': 'mythic-quagmire',
    'teddy': 'mythic-teddy',
    'amy': 'dr-amy-wong',
    'bob': 'mythic-bob',
    'boomhauer': 'mythic-boomhauer',
    'brian': 'mythic-brian',
    'francine': 'francine-smith',
    'leela': 'mythic-leela',
    'louise': 'mythic-louise',
    'peggy': 'mythic-peggy',
    'stan': 'mythic-stan',
    'stewie': 'mythic-stewie',
    'bender': 'mythic-bender',
    'bobby': 'mythic-bobby',
    'peter': 'mythic-peter',
    'tina': 'mythic-tina',
}

for lower in upgrade_dict:
    downgrade_dict[upgrade_dict[lower]] = lower


chs = [
        'bullock', 'chris', 'dale', 'dr-zoidberg', 'fry', 'hank', 'linda', 'lois', 'mort', 'steve',
        'bill', 'gene', 'hayley', 'hermes', 'klaus', 'luanns', 'meg', 'professor-farnsworth', 'quagmire', 'teddy', 
        'amy', 'bob', 'boomhauer', 'brian', 'francine', 'leela', 'louise', 'peggy', 'stan', 'stewie',
        'bill-dauterive',
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
        'francine-smith',
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
        'mythic-bobby',
        'mythic-peter',
        'mythic-tina',
        ]

maxed_out_items = {
    'dr-cahill': [10, 52],
    'horse-camp': [10, 45],
    'leon-petard': [17, 41],
    'quahog-martial-arts-academy': [16,33],
    'ski-mask': [12, 40],
    'stuffington-academy': [12, 43],
    'tom-landry-middle-school': [17, 39],
    'blernsball': [12, 42],
    'james-woods-high-school': [11,46],
    'turnin-jeff': [20, 35],
    'legendary-toad-licking': [18, 37],
    'shrimp-dress': [11, 50],
    'fart-school-for-the-gifted': [8, 48],
    'fart-school-jimmy-jr': [9, 50],
    'wine-bucket': [10, 46],
    'student-lucky': [18, 38],
    'iraq-lobster': [18, 33],
    'rogers-closet': [14, 41],
    'legendary-james-woods-high-school': [11, 46],
    'bandit': [19, 36],
}

stats = {
        'bullock':[
            [0,0], [3,15], [0,0],
        ],
        'chris':[
            [0,0], [3,13],[0,0],
        ],
        'dale': [
            [0,0], [2, 13],[0,0],
        ],
        'dr-zoidberg':[
            [0,0], [2,15],[0,0],
        ],
        'fry': [
            [0,0],[6,10],[0,0],
        ],
        'hank':[
            [0,0],[5,8],[0,0],
        ],
        'linda':[
            [0,0],[3,13],[0,0],
        ],
        'lois':[
            [0,0],[5,10],[0,0],
        ],
        'mort': [
            [0,0], [5,10],[0,0],
        ],
        'steve':[
            [0,0], [4,12], [0,0],
        ],
        'bill': [
            [0,0],[7,13],[0,0],
        ],
        'gene':[
            [0,0],[4,16],[0,0],
        ],
        'hayley':[
            [0,0],[5,15], [0,0],
        ],
        'hermes':[
            [0,0],[5,16],[0,0],
        ],
        'klaus':[
            [0,0],[4,15], [0,0],
        ],
        'luanns':[
            [0,0],[7,16],[0,0],
        ],
        'meg':[
            [0,0],[2,18],[0,0],
        ],
        'professor-farnsworth':[
            [0,0],[4,16],[0,0],
        ],
        'quagmire': [
            [0,0],[6,13],[0,0],
        ],
        'teddy':[
            [0,0],[6,14],[0,0],
        ], 
        'amy':[
            [0,0],[7,20],[8,26],
        ],
        'bob':[
            [0,0],[7,22], [9,24],
        ],
        'boomhauer':[
            [0,0],[6,16],[7,22],
        ],
        'brian':[
            [0,0],[6,20],[7,25],
        ],
        'francine':[
            [0,0],[5,25],[6,31],
        ],
        'leela':[
            [0,0],[4,25],[5,30],
        ],
        'louise':[
            [0,0],[4,21], [5,26],
        ],
        'peggy':[
            [0,0], [8,18],[9,22],
        ],
        'stan':[
            [0,0],[8,15],[8,19],
        ],
        'stewie':[
            [0,0],[4,25],[5,30],
        ],
        'bill-dauterive': [
            [13, 24], [15,30], [17, 37],
        ],
        'philip-j-fry':[
            [12, 23], [15, 29], [18, 38],
        ],
        'dr-amy-wong': [
            [10, 31], [13, 38], [14, 49],
        ],
        'eugene-belcher': [
            [11, 24], [14, 31], [16, 40],
        ],
        'chris-griffin': [
            [11, 26], [14, 33], [14, 42],
        ],
        'meg-griffin': [
            [8, 29], [10, 37], [12, 46],
        ],
        'hank-hill': [
            [12, 21], [14, 29], [15, 36],
        ],
        'bender': [
            [9, 24], [11, 33], [14, 38],
        ],
        'steve-smith': [
            [6, 36], [6, 47], [8, 56],
        ],
        'peter': [
            [6, 29], [8, 36], [11, 45],
        ],
        'roger': [
            [6, 30], [9, 35], [12, 41],
        ],
        'tina': [
            [8, 27], [11, 33], [12, 39],
        ],
        'linda-belcher': [
            [6, 33], [8, 39], [9, 48],
        ],
        'klaus-heisler': [
            [2, 36], [3, 48], [4, 60],
        ],
        'bobby': [
            [6, 27], [8, 36], [9, 44],
        ],
        'francine-smith': [
            [9, 30], [11, 37], [14, 45],
        ],
        'lois-griffin': [
            [8, 29], [11, 38], [13, 48],
        ],
        'hermes-conrad': [
            [11, 23], [14, 30], [17, 38],
        ],
        'mythic-stewie': [
            [9, 51], [12, 62], [0, 0],
        ],
        'mythic-quagmire': [
            [14, 44], [18, 55], [0, 0],
        ],
        'mythic-brian': [
            [10, 50], [14, 62], [0, 0],
        ],
        'mythic-stan': [
            [14, 42], [17, 57], [0,0],
        ],
        'mythic-bullock': [
            [15, 36], [20, 49], [0,0],
        ],
        'mythic-hayley':[
            [12, 44], [16,57], [0,0],
        ],
        'mythic-louise': [
            [8, 54], [12, 63], [0, 0],
        ],
        'mythic-bob': [
            [16, 44], [19, 55], [0, 0],
        ],
        'mythic-teddy': [
            [13, 40], [17, 60], [0,0],
        ],
        'mythic-peggy': [
            [12, 45], [17, 57], [0,0],
        ],
        'mythic-boomhauer':[
            [12, 41], [17, 52], [0,0],
        ],
        'mythic-dale': [
            [13, 42], [17, 55], [0,0],
        ],
        'mythic-leela': [
            [18, 35], [21, 44],[0,0],
        ],
        'mythic-dr-zoidberg': [
            [11,52], [15, 63], [0,0],
        ],
        'mythic-professor-farnsworth': [
            [15, 35], [19, 50], [0,0],
        ],
        'mythic-bender': [
            [15,44],[19, 56], [0,0],
        ],
        'mythic-bobby': [
            [12, 56], [14, 67],[0,0],
        ],
        'mythic-peter': [
            [11, 52], [15, 65], [0,0],
        ],
        'mythic-tina': [
            [16, 45], [20, 54], [0,0],
        ],
}

def type_of_ch(ch):
    if (stats[ch][2][0] == 0):
        if (stats[ch][0][0] == 0):
            return '<epic'
        else:
            return 'mythic'
    elif (stats[ch][0][0] == 0):
        return 'epic'
    else:
        return 'legendary'


data = {}
trait_dict = {}
dic = {}
combo_dict = {}

koth = ['mythic-bobby', 'mythic-peggy', 'mythic-boomhauer', 'hank-hill', 'bobby', 'bill-dauterive']

class at_card:
    def __init__(self, atk, hp, item_atk, item_hp):
        self.atk = atk
        self.hp = hp
        self.item_atk = item_atk
        self.item_hp = item_hp
        self.trait = 'none'
        self.skills = []
        self.slug = ''
        self.item_slug = ''
        self.item_rarity = ''
        self.char_rarity = ''
    def prt(self):
        print([self.atk, self.hp, self.trait, self.skills])
    def alt(self, ch):
        if '_lvl_18' in self.item_slug:
            return
        if not(ch in downgrade_dict):
            #print("%s not in downgrade dict."%ch)
            return
        def alt_sub(atk0, hp0, atkm, hpm, atk1, hp1, ch_alt, alt_type = 'C'):
            if alt_type == 'C':
                atk0 += self.item_atk
                atkm += self.item_atk
                atk1 += self.item_atk
                hp0 += self.item_hp
                hpm += self.item_hp
                hp1 += self.item_hp
            else:
                assert(self.item_slug in maxed_out_items)
                atk0 += self.item_atk
                atkm += maxed_out_items[self.item_slug][0]
                atk1 += self.item_atk
                hp0 += self.item_hp
                hpm += maxed_out_items[self.item_slug][1]
                hp1 += self.item_hp
            atk_ratio = atkm/atk1
            hp_ratio = hpm/hp1
            cd = at_card(self.atk * atk_ratio, self.hp * hp_ratio, self.item_atk, self.item_hp)
            cd.trait = self.trait
            cd.slug = self.slug
            cd.item_rarity = self.item_rarity
            cd.char_rarity = self.char_rarity
            if alt_type == 'C':
                cd.item_slug = self.item_slug
            else:
                cd.item_slug = self.item_slug + '_lvl_18'
            combo_power1 = (hp0 + atk0 * 3)
            combo_power2 = (hpm + atkm * 3)
            combo_power3 = (hp1 + atk1 * 3)
            a = (combo_power2 - combo_power3) / (combo_power1 - combo_power3)
            b = 1 - a
            #if (ch_alt[-1] == '8') and (ch[0] != 'm'):
            #    print(combo_power1, combo_power2, combo_power3, ch, downgrade_dict[ch], ch_alt)
            #    print("XX ", a * combo_power1 + b * combo_power3, combo_power2, a, b)
            dch = downgrade_dict[ch]
            for sk in self.skills:
                if not (dch + '+' + self.item_slug) in dic:
                    print(dch + '+' + self.item_slug)
                    continue
                for skl in dic[dch + '+' + self.item_slug].skills:
                    if skl[0] == sk[0]:
                        cd.skills.append([sk[0], skl[1] * a + sk[1] * b])
                        if (ch_alt[-1] == '8') and (ch[0] != 'm'):
                            #print(skl, sk, cd.skills[-1])
                            assert(cd.skills[-1][1]>sk[1])

            if alt_type != 'C':
                #print(ch_alt+'+'+cd.item_slug, cd.hp, cd.atk, cd.skills, [atk0, atk1, atkm])
                pass
            if not (ch_alt in data):
                data[ch_alt] = []
            data[ch_alt].append(cd)

        [atk0, hp0] = stats[downgrade_dict[ch]][1]
        [atk1, hp1] = stats[ch][1]
        ch_alt = ch
        if type_of_ch(ch) == 'legendary':
            alt_sub(atk0, hp0, *stats[ch][2], atk1, hp1, ch + '_lvl_18')
            if self.item_slug in maxed_out_items:
                alt_sub(atk0, hp0, *stats[ch][1], atk1, hp1, ch, 'I')
                alt_sub(atk0, hp0, *stats[ch][2], atk1, hp1, ch + '_lvl_18', 'CI')
        elif type_of_ch(ch) == 'mythic':
            alt_sub(atk0, hp0, *stats[ch][0], atk1, hp1, ch + '_lvl_1')
            if self.item_slug in maxed_out_items:
                #alt_sub(atk0, hp0, *stats[ch][1], atk1, hp1, ch, 'I')
                alt_sub(atk0, hp0, *stats[ch][0], atk1, hp1, ch + '_lvl_1', 'CI')
        if (type_of_ch(ch) == 'mythic') and (type_of_ch(downgrade_dict[ch]) == 'legendary'):
            alt_sub(atk0, hp0, *stats[downgrade_dict[ch]][2], atk1, hp1, downgrade_dict[ch] + '_lvl_18')
            if self.item_slug in maxed_out_items:
                alt_sub(atk0, hp0, *stats[downgrade_dict[ch]][1], atk1, hp1, downgrade_dict[ch], 'I')
                alt_sub(atk0, hp0, *stats[downgrade_dict[ch]][2], atk1, hp1, downgrade_dict[ch] + '_lvl_18', 'CI')

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
    trait = ''
    item_atk = 0
    item_hp = 0
    item_slug = ''
    item_rarity = ''
    char_rarity = ''
    for card in cards:
        index += 1
        if index % 3 == 1:
            char_rarity = card.attrib['rarity']
            continue
        if index % 3 == 2:
            rarity = card.attrib['rarity']
            if 'trait' in card.attrib:
                trait = card.attrib['trait']
            else:
                trait = 'none'
            item_atk = int(card.find('cb-stats')[0].text)
            item_hp = int(card.find('cb-stats')[1].text)
            item_slug = card.attrib['slug']
            item_rarity = rarity
            trait_dict[item_slug] = trait
            continue
        #if char_rarity in ['legendary', 'mythic']:
        #    if not (rarity in ['legendary', 'mythic']):
        #        continue
        atcd = at_card(int(card.find('cb-stats')[0].text),
                int(card.find('cb-stats')[1].text), item_atk, item_hp)
        atcd.slug = card.attrib['slug']
        atcd.item_slug = item_slug
        atcd.item_rarity = item_rarity
        atcd.char_rarity = char_rarity
        if 'trait' in card.attrib:
            if card.attrib['trait'] != trait:
                #print([card.attrib['slug'], card.attrib['trait'], trait])
                pass
            if trait == 'none':
                trait = card.attrib['trait']
            atcd.trait = trait #card.attrib['trait']
        for node in card.find('cb-skills'):
            try:
                value = int(node.text)
                if 'target' in node.attrib:
                    #if card.attrib['slug'] == 'sex-ed-teacher':
                    #    print(node.attrib)
                    if node.attrib['target'] == 'trait':
                        value = 1 * value
                    if node.attrib['target'] == 'show':
                        value = 1 * value
                atcd.skills.append([node.attrib['type'], value])
            except:
                continue
        atcds.append(atcd)
        dic[ch + '+' + atcd.item_slug] = atcd
    data[ch] = atcds

for ch in chs:
    analyse(ch)

for ch in chs:
    if type_of_ch(ch) in ['legendary', 'mythic']:
        for cd in data[ch]:
            cd.alt(ch)

skills = {}

for skill in skill_dict:
    skills[skill_dict[skill]] = {}

cminit = {}

for ch in data:
    for cd in data[ch]:
        combo_dict[ch + '+' + cd.item_slug] = cd.slug
        cminit[cd.slug] = 0
        for sk in cd.skills:
            skills[skill_dict[sk[0]]][ch + '+' + cd.item_slug] = sk[1]

with open('combos', 'wb') as f:
    pickle.dump(data, f)

with open('traits.json', 'w') as f:
    f.write('tr_data = \'' + json.dumps(trait_dict) + '\';')


with open('skills.json', 'w') as f:
    f.write('sk_data = \'' + json.dumps(skills) + '\';\ncombo_data = \'' + json.dumps(combo_dict) + '\';\n' + 'cm_data = \'' + json.dumps(cminit) + '\';\n')
