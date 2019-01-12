
var analyse_card_list = function(chs, its, skill = 'deck-power'){
    var mydict = skills[skill];
    if (['deck-power', 'all-skill'].indexOf(skill) >= 0){
      mydict = mydata;
    }
    var total_scores = {};
    var scores_arr = {};
    chs.forEach(function(ch){total_scores[ch]=0.0; scores_arr[ch] = [];});
    its.forEach(function(it){total_scores[it]=0.0; scores_arr[it] = [];});
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
    var sharpness =parseFloat(document.getElementById("sharpness").value);
    var sh_a = 0.1;
    var sh_b = 10;
    if (sharpness < sh_a){ sharpness = sh_a;}
    else if (sharpness > sh_b) {sharpness = sh_b;}
    else if ((sharpness >= sh_a - 0.01) && (sharpness <=sh_b + 0.01)) { sharpness = sharpness;}
    else {sharpness = 1.0;}
    //console.log("Sharpness = " + sharpness.toString());
    var factor_foo = (i)=>{
        var x = Math.exp(sharpness *  Math.log(i)); return x;
    };
    its.forEach(function(it){
        if (total_scores[it] > 0.1) return;
        scores_arr[it].sort();
        for (var i = 1; i <= scores_arr[it].length; i++){
            var sc = scores_arr[it][scores_arr[it].length - i];
            if (sc < 2) sc = 0.0;
            else if (sc < 2.5) sc = sc*0.5;
            else if (sc < 3) sc = sc * 0.8;
            total_scores[it] += sc/factor_foo(i);
        }
      }
    );
    chs.forEach(function(ch){
        if (total_scores[ch] > 0.1) return;
        scores_arr[ch].sort();
        for (var i = 1; i <= scores_arr[ch].length; i++){
            var sc = scores_arr[ch][scores_arr[ch].length - i];
            if (sc < 2) sc = 0.0;
            else if (sc < 2.5) sc = sc*0.5;
            else if (sc < 3) sc = sc * 0.8;
            total_scores[ch] +=sc/factor_foo(i);
        }
      }
    );
    chs.sort(function(c1, c2){return total_scores[c2]-total_scores[c1]});
    its.sort(function(c1, c2){return total_scores[c2]-total_scores[c1]});
    var eva = 0.0;
    var eva_c = 0.0;
    var eva_i = 0.0;
    var fct = 1.0;
    chs.forEach(function(ch){eva_c += total_scores[ch]*fct;});
    fct = 1.0;
    its.forEach(function(it){eva_i += total_scores[it]*fct;});
    eva = Math.min(eva_c, eva_i)*10;// + Math.max(eva_c, eva_i);
    return [mydict, chs, its, total_scores, eva, eva_c*10, eva_i*10];
};

var find_worst = function(chs, its, skill = 'deck-power', item_only = false){
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
    else if (item_only){
        return its[its.length - 1];
    }
    else{
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
var remove_worst = function(chs, its, skill = 'deck-power', item_only = false){
    var cd = find_worst(chs, its, skill, item_only);
    if (cd == 'none') return;
    if (item_only){
        remove_subset(its, [cd]);
    }
    else{
        remove_subset(its, [cd]);
        remove_subset(chs, [cd]);
    }
};
var filter_cards = function(clist = get_clist() ) {
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
var gen_sel = function*(set, num, start = 0){
    if (num == 0){ yield []; }
    else if (start + num == set.length) {
        var nss = [];
        for (var i = start; i < set.length; i++) nss.push(set[i]);
        yield nss;
    }
    else if (start + num > set.length) {}
    else if (num == 1){
        for (var i = start; i < set.length; i++) yield [set[i]];
    }
    else{
        for (var subset of gen_sel(set, num - 1, start + 1)){
            var nss = [];
            for (var x of subset) nss.push(x);
            nss.push(set[start]);
            yield(nss);
        }
        yield* gen_sel(set, num, start + 1);
    }
};
var gen_sel_opt = function*(set, num){
    if (num * 2 < set.length){
        yield*gen_sel(set, num);
    }
    else{
        yield*gen_sel(set, num);
    }
}
var remove_subset = function(set, _subset){
    var subset = [];
    for (var x of _subset) subset.push(x); 
    while (subset.length){
        var x = subset[subset.length - 1];
        var i = 0;
        var flag = 0;
        while (i < set.length){
            if (set[i] == x){
                set[i] = set[set.length - 1];
                set.pop();
                subset.pop();
                flag = 1;
                break;
            }
            i ++;
        }
        if (!flag){
            return;
        }
    }
}
var deep_optimize = function(_chs, _its, has_fixed_slots){
    var max_sc = 0.0;
    var mchs, mits;
    var chs = [];
    //var ress = [];
    for (var x of _chs) chs.push(x); 
    var scores = [];
    var char_num = 12;
    if (has_fixed_slots){
        char_num -= fixed_slots.length;
    }
    var cts = 0;
    console.log(['Choose', chs.length, char_num]);
    for (var _subset of gen_sel(chs, char_num)){
        cts += 1;
        var nchs = [];
        for (var x of _subset) nchs.push(x); 
        var its = [];
        for (var x of _its) its.push(x);
        if (has_fixed_slots){
            for (var x of fixed_slots) {
                nchs.push(x);
            }
        }
        while (its.length > 12){
            remove_worst(nchs, its, 'deck-power', true);
        }
        var nsc = analyse_card_list(nchs, its)[4];
        scores.push(nsc);
        if (nsc > max_sc){
            max_sc = nsc;
            //ress.push([max_sc, nchs, its])
            mchs = [];
            mits = [];
            for (var x of nchs) mchs.push(x);
            for (var x of its) mits.push(x);
        }
    }
    console.log(['cts', cts]);
    scores.sort();
    if (max_sc  > 0.1){
        var h = make_table(mchs, mits, 'deck-power');
        document.getElementById('table').innerHTML = h;    
        //document.getElementById('card-list-input').value = mchs.join('\n') + '\n' +mits.join('\n');
        best_combo(mchs.concat(mits));
    }
};
var optimize_deck = function(has_fixed_slots = false){
    var worst_card = '';
    while (worst_card != 'none'){
        var fres = filter_cards();
        var chs = fres[0];
        var its = fres[1];
        worst_card = find_worst(chs, its, 'deck-power');
        if (worst_card == 'none'){ break; }
        if (has_fixed_slots){
            remove_subset(chs, fixed_slots);
        }
        else{
            fixed_slots = [];
        }
        if (chs.length + fixed_slots.length <= 15){
            deep_optimize(chs, its, has_fixed_slots);
            return;
        }
        delete_card(worst_card);
    }
    go();
}
