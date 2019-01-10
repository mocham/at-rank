var my_cm = {
    'cigarette-addicts': 1,
    'dolphin-rider-peter': 1,
    'guidance-counselor': 1,
    'assasin-bender': 1,
    'betsy': 1,
    'cleaning-wench': 1,
    'clobberella': 1,
    'crayon-drawing': 1,
    'devil-hank': 1,
    'dr-bobbenstein': 1,
    'egg-vs-tornado': 1,
    'future-meg': 1,
    'high-school-bill': 1,
    'karate-stewie': 1,
    'nun-francine': 1,
    'one-man-musical': 1,
    'pirate-cannon-peter': 1,
    'prison-meg': 1,
    'sexy-cat': 1,
    'sister-peter': 1,
    'the-billdozer': 1,
    'trippy-zoidberg': 1,
    'tweaker-peter': 1,
    'umbriel': 1,
    'viking-peter': 1,
    'chicken-fight': 2,
    'claw-machine': 1,
    'golfer-amy': 2,
    'medicated-stewie': 1,
    'obedience-school-brian': 1,
    'wingnut-amy': 2,
};

var my_deck = [
    'peter_lvl_18',
    'peter_lvl_18',
    'mythic-bob_lvl_1',
    'dr-amy-wong',
    'mythic-dr-zoidberg_lvl_1',
    'eugene-belcher_lvl_18',
    'eugene-belcher',
    'mythic-hayley_lvl_1',
    'mythic-stan_lvl_1',
    'hank-hill_lvl_18',
    //'hank-hill',
    'mythic-peggy_lvl_1',
    'mythic-bobby_lvl_1',
    'bobby',
    'bill-dauterive_lvl_18',
    //'bill-dauterive',
    'bill-dauterive_lvl_18',
    //'bill-dauterive',
    'dr-cahill_lvl_18',
    'stuffington-academy_lvl_18',
    'dr-banjo',
    'student-lucky',
    'quahog-preschool',
    'groff-community-college',
    'professor-lerner',
    'bending-school',
    'tom-landry-middle-school_lvl_18',
    'quahog-martial-arts-academy_lvl_18',
    'horse-camp_lvl_18',
    'ski-mask_lvl_18',
    'leon-petard',
    'leon-petard_lvl_18',
    'hypnotoad',
    'francine-smith',
    'book-of-spells',
    'bucks-stud',
    'caulk-gun',
    'cuddles',
    'fart-school-jimmy-jr',
    'finger-gun-gayle',
    'iraq-lobster',
    'mobile-oppression-palace',
    'mr-business',
    'push-ups',
    'legendary-toad-licking',
    'toxic-shock',
    'wine-bucket',
    'meg-griffin_lvl_18',
    'bandit',
    'arcturan-kung-fu',
    'bunny-costume',
    'long-stick-with-sharp-rock',
    'napkin-art',
    'peters-drawing',
    'welcome-mojitos',

];
var mine = function() {
    var s = my_deck[0];
    for (var i = 1; i < my_deck.length; i++) s += '\n' + my_deck[i];
    document.getElementById('card-list-input').value = s;
    var s1 = '';
    Object.keys(my_cm).forEach(
        function(cm){
            for (var i = 0; i < my_cm[cm]; i++){
                s1 += '\n' + cm;
            }
        }
    );
    document.getElementById('cm-list-input').value = s1.slice(1);
};
var def_deck = function(){
    var s = "bucks-stud,leon-petard,mythic-dr-zoidberg_lvl_1,eugene-belcher_lvl_18,mythic-stan_lvl_1,hank-hill,hank-hill,mythic-peggy_lvl_1,mythic-bobby_lvl_1,bobby,bill-dauterive,bill-dauterive,bill-dauterive,bill-dauterive,dr-cahill_lvl_18,stuffington-academy_lvl_18,dr-banjo,student-lucky,quahog-preschool,groff-community-college,professor-lerner,leon-petard_lvl_18,hypnotoad,quahog-martial-arts-academy_lvl_18";
    document.getElementById('card-list-input').value = s;
};





var skill_dict = {
    'all-skill': 'all-skill',
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
};
var rare_chs = [
    'bill', 'gene', 'hayley', 'hermes', 'klaus', 'luanns', 'meg', 'professor-farnsworth', 'quagmire', 'teddy',    
];
var common_chs = [
    'bullock', 'chris', 'dale', 'dr-zoidberg', 'fry', 'hank', 'linda', 'lois', 'mort', 'stevs',    
];
var epic_chs = [
    'amy', 'bob', 'boomhauer', 'brian', 'francine', 'leela', 'louise', 'peggy', 'stan', 'stewie',     
];
var leg_chs = [
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
];
var mythic_chs = [
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
];
var chs = [
    'bullock', 'chris', 'dale', 'dr-zoidberg', 'fry', 'hank', 'linda', 'lois', 'mort', 'stevs',    
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
    ];

mythic_chs.forEach(
    function (ch){
        chs.push(ch + '_lvl_1');
    }
);
leg_chs.forEach(
    function (ch){
        chs.push(ch + '_lvl_18');
    }
);
var is_char = function(card){
    for (var i = 0; i < chs.length; i++){
        if (chs[i] == card) { return true; }
    }
    return false;
};
