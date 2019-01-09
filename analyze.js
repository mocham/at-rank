
var analyse_card_list = function(chs, its, skill = 'deck-power'){
    var mydict = skills[skill];
    if (['deck-power', 'all-skill'].indexOf(skill) >= 0){
      mydict = mydata;
    }
    var total_scores = {};
    var scores_arr = {};
    chs.forEach(ch=>{total_scores[ch]=0.0; scores_arr[ch] = [];});
    its.forEach(it=>{total_scores[it]=0.0; scores_arr[it] = [];});
    chs.forEach(
      function(ch){
        if (scores_arr[ch].length > 0) return;
        its.forEach(
            function(it){
                var cm_factor = 1.0;
                var cm = 0.0;
                if (combos[(ch + '+' + it)] in cmdata){
                    cm = cmdata[combos[ch + '+' + it]];
                    cm_factor += cm/10;
                }
                if ((ch + '+' + it) in mydict){
                    scores_arr[ch].push(mydict[ch + '+' + it] * cm_factor);
                    scores_arr[it].push(mydict[ch + '+' + it] * cm_factor);
                }
            }
        );
    }
    );
    its.forEach(it=>{
        if (total_scores[it] > 0.1) return;
        scores_arr[it].sort();
        for (var i = 1; i <= scores_arr[it].length; i++){
            var sc = scores_arr[it][scores_arr[it].length - i];
            if (sc < 2) sc = 0.0;
            else if (sc < 2.5) sc = sc*0.5;
            else if (sc < 3) sc = sc * 0.8;
            total_scores[it] += sc/( + Math.sqrt(i));
        }
      }
    );
    chs.forEach(ch=>{
        if (total_scores[ch] > 0.1) return;
        scores_arr[ch].sort();
        for (var i = 1; i <= scores_arr[ch].length; i++){
            var sc = scores_arr[ch][scores_arr[ch].length - i];
            if (sc < 2) sc = 0.0;
            else if (sc < 2.5) sc = sc*0.5;
            else if (sc < 3) sc = sc * 0.8;
            total_scores[ch] += sc/( + Math.sqrt(i));
        }
      }
    );
    chs.sort((c1, c2)=>{return total_scores[c2]-total_scores[c1]});
    its.sort((c1, c2)=>{return total_scores[c2]-total_scores[c1]});
    var eva = 0.0;
    chs.forEach((ch)=>{eva += total_scores[ch];});
    its.forEach((it)=>{eva += total_scores[it];});
    return [mydict, chs, its, total_scores, eva];
};

var find_worst = function(chs, its, skill = 'deck-power'){
    var ares = analyse_card_list(chs, its, skill);
    var mydict = ares[0];
    chs = ares[1];
    its = ares[2];
    var total_scores = ares[3];
    if (chs.length <= 12){
        if (its.length > 12) { return its[its.length-1]; }
        else {return 'none';}
    }
    else if (its.length <= 12) {
        if (chs.length > 12) { return chs[chs.length-1]; }
        else {return 'none';}
    }
    else {
        it1 = its[its.length - 1];
        it2 = its[its.length - 2];
        ch1 = chs[chs.length - 1];
        ch2 = chs[chs.length - 2];
        it0 = its[0];
        ch0 = chs[0];
        if ((total_scores[it2]+total_scores[it0])/total_scores[it1]> (total_scores[ch2]+total_scores[ch0])/total_scores[ch1]){
            return it1;
        }
        else{
            return ch1;
        }
    }
};
var filter_cards = (clist = get_clist() ) =>{
    var chs = [];
    var its = [];
    clist.forEach(
      function(cd){
        if (is_char(cd)) {chs.push(cd);}
        else {its.push(cd);}
      }
    );
    return [chs, its];
};
var optimize_deck = ()=>{
    while (worst_card != 'none'){
        var fres = filter_cards();
        var chs = fres[0];
        var its = fres[1];
        var worst_card = find_worst(chs, its, 'deck-power');
        console.log("Worst = " + worst_card);
        if (worst_card == 'none'){ break; }
        delete_card(worst_card);
    }
    go();
}
