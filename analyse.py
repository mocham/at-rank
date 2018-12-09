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
        'hermes-conrad'
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
    'bodyguard': 0.7, #'bodyguard',
    'inspire': 1.5, #'motivate',
    'pierce': 0.6, #'jab',
    'poison': 1.5, #'gas',
    'strike': 1.2, #'punch',
    'armored': 1, #'sturdy',
    'berserk': 3, #'crazed',
    'outlast': 0.4, #'recover',
    'invigorate': 0.6, #'boost',
    'counter': 1.1, #'payback',
    'weaken': 0.5, #'cripple',
    'leech': 1.6, #'leech',
    'weakenall': 1.3, #'cripple-all',
    'barrier': 0.8, #'shield',
    'barrierall': 1.2, #'shield-all',
    'rallyall': 1, #'cheer-all',
    'rally': 0.5, #'cheer',
    'heal': 0.7, #'heal',
    'healall': 0.8, #'heal-all',
    'shrapnel': 2.3, #'bomb',
    'hijack': 0.3, #'hijack',
}

maxm = {'hp': 0, 'atk': 0}
bges = ['none', 'educated', 'hyper', 'addicted', 'rich', 'armed', 'athletic', 'fighter', 'disguised', 'musical', 'animal', 'artistic', 'drunk']
tr = {}

with open('combos', 'rb') as f:
    data = pickle.load(f)
    

    for ch in chs:
        for cd in data[ch]:
            maxm['atk'] = max(maxm['atk'], cd.atk)
            maxm['hp'] = max(maxm['hp'], cd.hp)
            for sk in cd.skills:
                if not sk[0] in maxm:
                    maxm[sk[0]] = 0
                maxm[sk[0]] = max(maxm[sk[0]], sk[1])
            #tr.add(cd.trait)
    #print(maxm)
    #print(tr)
    def skill_bonus(arr):
        st = []
        bonus = 1
        for sk in arr:
            st.append(sk)
        if 'shrapnel' in st:
            pass
    debug = False
    verbose = {'bge': 'educated', 'ch': 'hank-hill'}
    csv = ','
    for ch in chs:
        csv += ch + ','
    csv += '\n'
    for bge in bges:
        csv += bge + ','
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
                combo_value += cd.hp/maxm['hp']
                for sk in cd.skills:
                    combo_value += sk[1] * len(cd.skills)/3 /maxm[sk[0]] * skill_factor[sk[0]]
                combo_values.append(combo_value)
            combo_values.sort()
            #print([ch, combo_values])
            tr[ch] = 0.0
            n = min(8, len(combo_values))
            if n == 0:
                continue
            total_wt = 0.0
            for i in range(0, n):
                total_wt += 1/(i+1)
                tr[ch] += combo_values[-(i+1)]/(i+1)
            tr[ch] /= total_wt
        sorted_x = sorted(tr.items(), key=operator.itemgetter(1))
        maxx = 0.0
        for x in sorted_x:
            maxx = max(maxx, x[1])
        def top5(arr):
            return (arr[-1][0], arr[-2][0], arr[-3][0], arr[-4][0], arr[-5][0])
        #print([bge, top5(sorted_x)])
        print([bge,sorted_x])
        chd = {}
        for x in sorted_x:
            chd[x[0]] = x[1]/maxx
        for ch in chs:
            csv += str(chd[ch]) + ','
        csv += '\n'
with open('tb.csv', 'w') as f:
    f.write(csv)




