import pickle, operator

class at_card:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp
        self.trait = 'none'
        self.skills = []
    def prt(self):
        print([self.atk, self.hp, self.trait, self.skills])

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
        ]

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
    'strike': 1.2, #'punch',
    'armored': 1, #'sturdy',
    'berserk': 3.5, #'crazed',
    'outlast': 0.5, #'recover',
    'invigorate': 0.7, #'boost',
    'counter': 1.1, #'payback',
    'weaken': 0.5, #'cripple',
    'leech': 1.6, #'leech',
    'weakenall': 0.9, #'cripple-all',
    'barrier': 0.7, #'shield',
    'barrierall': 1.1, #'shield-all',
    'rallyall': 0.8, #'cheer-all',
    'rally': 0.5, #'cheer',
    'heal': 0.7, #'heal',
    'healall': 0.8, #'heal-all',
    'shrapnel': 2.6, #'bomb',
    'hijack': 0.4, #'hijack',
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
                bonus *= 1.3
            if 'armored' in st:
                bonus *= 1.2
            if 'pierce' in st:
                bonus *= 1.15
            if 'strike' in st:
                bonus *= 1.1
        elif 'berserk' in st:
            if 'leech' in st:
                bonus *= 1.3
            if 'armored' in st:
                bonus *= 1.2
            if 'pierce' in st:
                bonus *= 1.15
            if 'strike' in st:
                bonus *= 1.1
        elif 'counter' in st:
            if 'leech' in st:
                bonus *= 1.3
        if 'leech' in st:
            if 'poison' in st:
                bonus *= 1.2
        return bonus

    debug = False 
    verbose = {'bge': 'artistic', 'ch': 'mythic-peggy'}
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
                combo_value = 0.0
                combo_value += cd.atk/maxm['atk'] * 1.2
                combo_value += cd.hp/maxm['hp'] * 1
                #print([0, combo_value])
                for sk in cd.skills:
                    combo_value += sk[1]/maxm[sk[0]] * skill_factor[sk[0]] * lack_of_skill_factor(len(cd.skills))
                combo_value *= dual_skill_bonus(cd.skills)
                combo_values.append(combo_value)
                if debug:
                    print([cd.slug, cd.skills, combo_value])
                    print([1, combo_value])
            combo_values.sort()
            if debug:
                print([ch, combo_values])
            tr[ch] = 0.0
            n = min(20, len(combo_values))
            if n == 0:
                continue
            total_wt = 0.0
            for i in range(0, n):
                total_wt += 1/(i+1)
                tr[ch] += combo_values[-(i+1)]/(i+1)
            tr[ch] /= total_wt
            print(tr[ch])
            tr[ch] += len(combo_values) / 100
            print(len(combo_values)/100)
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
            rec[ch][bge] = str(chd[ch])
    csv = ',sum of top 7,'
    for bge in bges:
        csv += bge + ','
    csv += '\n'
    idx = 1
    def sum_of_top6(ch):
        sm = 0.0
        arr = []
        for bge in bges:
            arr.append(float(rec[ch][bge]))
        arr.sort()
        for i in range(1, 8):
            sm += arr[-i]
        return sm
    for ch in chs:
        idx += 1
        csv += ch + ',%f,'%sum_of_top6(ch)
        for bge in bges:
            csv += rec[ch][bge] + ','
        csv += '\n'

with open('tb.csv', 'w') as f:
    f.write(csv)




