import pickle, operator
from math import sqrt
import json

class at_card:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp
        self.trait = 'none'
        self.skills = []
    def prt(self):
        print([self.atk, self.hp, self.trait, self.skills])

current_BGE = []#['educated']#['eduacated', 'addicted']

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

chs_N0 = len(chs)
for i in range(0, chs_N0):
    ch = chs[i]
    if type_of_ch(chs[i]) == 'legendary':
        if ch != 'roger':
            chs.append(ch + '_lvl_18')
    elif type_of_ch(chs[i]) == 'mythic':
        chs.append(ch + '_lvl_1')


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


skill_factor = {
    'bodyguard': 0.9, #'bodyguard',
    'inspire': 1.5, #'motivate',
    'pierce': 0.5, #'jab',
    'poison': 1.5, #'gas',
    'strike': 1.7, #'punch',
    'armored': 1, #'sturdy',
    'berserk': 3, #'crazed',
    'outlast': 0.5, #'recover',
    'invigorate': 0.7, #'boost',
    'counter': 1.1, #'payback',
    'weaken': 0.5, #'cripple',
    'leech': 1.6, #'leech',
    'weakenall': 1.3, #'cripple-all',
    'barrier': 0.7, #'shield',
    'barrierall': 1.2, #'shield-all',
    'rallyall': 0.9, #'cheer-all',
    'rally': 0.5, #'cheer',
    'heal': 0.7, #'heal',
    'healall': 0.8, #'heal-all',
    'shrapnel': 2, #'bomb',
    'hijack': 0.5, #'hijack',
}



maxm = {'hp': 0, 'atk': 0}
bges = [#'none',
        'educated', 
        #'hyper',
        'addicted',
        #'rich',
        'armed',
        'athletic',
        'fighter',
        'disguised',
        'musical',
        'animal',
        'artistic',
        'drunk'
]
tr = {}
rec = {}
score_dict = {}
NBGE = 7

with open('combos', 'rb') as f:
    data = pickle.load(f)
    

    for ch in chs:
        rec[ch] = {}
        for cd in data[ch]:
            maxm['atk'] = max(maxm['atk'], cd.atk)
            maxm['hp'] = max(maxm['hp'], cd.hp)
            for sk in cd.skills:
                if not sk[0] in maxm:
                    maxm[sk[0]] = 0
                maxm[sk[0]] = max(maxm[sk[0]], sk[1])
    def dual_skill_bonus(arr):
        st = []
        bonus = 1
        for sk in arr:
            st.append(sk[0])
        if 'shrapnel' in st:
            if 'leech' in st:
                bonus *= 1.13
            if 'armored' in st:
                bonus *= 1.1
            if 'pierce' in st:
                bonus *= 1.07
            if 'strike' in st:
                bonus *= 1.07
        elif 'berserk' in st:
            if 'leech' in st:
                bonus *= 1.15
            if 'armored' in st:
                bonus *= 1.1
            if 'pierce' in st:
                bonus *= 1.07
            if 'strike' in st:
                bonus *= 1.07
        elif 'counter' in st:
            if 'leech' in st:
                bonus *= 1.15
        if 'leech' in st:
            if 'poison' in st:
                bonus *= 1.1
        return bonus

    debug = False
    verbose = {'bge': 'athletic', 'ch': 'mythic-dr-zoidberg'}
    BGE_affected = True
    def lack_of_skill_factor(num):
        if num == 3:
            return 1.0
        elif num == 2:
            return 1.1
        elif num == 1:
            return 1.2
    for bge in bges:
        if debug:
            if verbose['bge'] != bge:
                continue
        for ch in chs:
            if debug:
                if verbose['ch'] != ch:
                    continue
            combo_values = []
            for cd in data[ch]:
                if cd.trait != bge:
                    continue
                if cd.char_rarity in ['legendary', 'mythic']:
                    if not (cd.item_rarity in ['legendary', 'mythic']):
                        continue
                combo_value = 0.0
                combo_value += cd.atk/maxm['atk'] * 1.2
                combo_value += cd.hp/maxm['hp'] * 1
                #print([0, combo_value])
                if debug:
                    print([1, combo_value])
                for sk in cd.skills:
                    sk_factor = 0.1
                    #for skc in skill_factor[sk[0]]:
                    #    if sk[1] >= skc[1]:
                    #        sk_factor = max(sk_factor, skc[0])
                    sk_factor = skill_factor[sk[0]]
                    delta = sk[1]/maxm[sk[0]] * sk_factor * lack_of_skill_factor(len(cd.skills))
                    combo_value += delta
                    if debug:
                        pass
                        #print([1, sk, skill_factor[sk[0]], maxm[sk[0]], delta])
                if debug:
                    print([cd.slug, cd.skills, combo_value])
                #combo_value *= dual_skill_bonus(cd.skills)
                score_dict[ch + '+' + cd.item_slug] = combo_value
                combo_values.append(combo_value)
            if debug:
                print([ch, combo_values])
            if debug:
                continue
            combo_values.sort()
            tr[ch] = 0.0
            n = 20 #min(20, len(combo_values))
            if n == 0:
                continue
            total_wt = 0.0
            for i in range(0, n):
                wt = 1/sqrt(i+1)
                total_wt += wt
                if i < len(combo_values):
                    tr[ch] += combo_values[-(i+1)] * wt
            tr[ch] /= total_wt
            #print(tr[ch])
            #tr[ch] += len(combo_values) / 100
            #print(len(combo_values)/100)
        if debug:
            continue
        sorted_x = sorted(tr.items(), key=operator.itemgetter(1))
        maxx = 0.0
        for x in sorted_x:
            maxx = max(maxx, x[1])
        chd = {}
        for x in sorted_x:
            if maxx > 0.001:
                chd[x[0]] = x[1]/maxx
            else:
                chd[x[0]] = 0.0
        for ch in chs:
            rec[ch][bge] = ("%.2f"%chd[ch])
    csv = ' , BGE Score ,sum of top 7,'
    md = '| | BGE Score | Sum of top 7 |'
    for bge in bges:
        csv += bge + ','
        md += bge + '|'
    csv += '\n'
    md += '\n| --- | --- | --- |'
    for bge in bges:
        md +=' --- |'
    md += '\n|'
    idx = 1
    def sum_of_top7_BGE(ch):
        sm = 0.0
        arr = []
        sum_of_factors_BGE = 0.0
        sum_of_factors = 0.0
        for bge in bges:
            BGE_factor = 1.0
            if bge in current_BGE:
                BGE_factor = 3.0
            arr.append((float(rec[ch][bge]))*BGE_factor)
            sum_of_factors_BGE += BGE_factor
            sum_of_factors += 1.0
        arr.sort()
        for i in range(1, NBGE + 1):
            sm += arr[-i]
        return sm * sum_of_factors/sum_of_factors_BGE
    def sum_of_top7(ch):
        sm = 0.0
        arr = []
        for bge in bges:
            BGE_factor = 1.0
            arr.append((float(rec[ch][bge]))*BGE_factor)
        arr.sort()
        for i in range(1, NBGE + 1):
            sm += arr[-i]
        return sm
    if not debug:
        ch_srt = []
        for ch in chs:
            ch_srt.append([ch, sum_of_top7_BGE(ch)])
        ch_srt.sort(key = lambda x : x[1], reverse = True)
        for ch_pair in ch_srt:
            ch = ch_pair[0]
            if not ('lvl' in ch):
                continue
            idx += 1
            csv += ch + ',%.2f,%.2f'%(sum_of_top7_BGE(ch), sum_of_top7(ch))
            md += ch + '| %.2f | %.2f |'%(sum_of_top7_BGE(ch), sum_of_top7(ch))
            for bge in bges:
                csv += rec[ch][bge] + ','
                md += rec[ch][bge] + '|'
            csv += '\n'
            md += '\n|'

        with open('tb.txt', 'w') as f:
            f.write(md)
        with open('scores.json', 'w') as f:
            f.write('data = \'' + json.dumps(score_dict) + '\';')




