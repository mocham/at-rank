var get_clist = function(){
    var l0 = document.getElementById('card-list-input').value.split('\n');
    var l1 = [];
    l0.forEach(
        function(cd) {
            cd = cd.toLowerCase().replace(/\s+/g, '');
            if (cd.length > 0) l1.push(cd);
        }
    );
    var lcm = document.getElementById('cm-list-input').value.split('\n');
    Object.keys(cmdata).forEach(
        function(cm) {cmdata[cm] = 0;}   
    );
    lcm.forEach(
        function(cd)  {
            cd = cd.toLowerCase().replace(/\s+/g, '');
            if (cd.length > 0){
                cmdata[cd] += 1;
            }
        }
    );
    return l1;
};
var skill_img_tag = function(sk) {
    return '<img src="img/skill_' + sk + '.png" style="max-width:100%;max-height:100%;height:14px;width:14px;">';
};
var bge_img_tag = function(it){
    if (it.includes('_lvl_18')) {
        it = it.slice(0, -7);
    }
    bge = traits[it];
    return '<img src="img/icon_large_' + bge + '.png" style="max-width:100%;max-height:100%;height:20px;width:20px;">';
};
var delete_card = function(slug)  {
    var clist = get_clist();
    var pos = -1;
    for (var i = 0; i < clist.length; i++){
        if (clist[i] == slug) pos = i;
    }
    if (pos < 0) return;
    clist[pos] = clist[clist.length - 1];
    clist.pop();
    document.getElementById('card-list-input').value = clist.join('\n');
    go();
}
var rarity_img_tag = function(ch){
    rarity = 'legendary';
    if (ch.substring(0, 6) == 'mythic') {rarity = 'mythic';}
    for (var i = 0; i < epic_chs.length; i++){
        if (epic_chs[i] == ch) {rarity = 'epic';}
    }
    for (var i = 0; i < rare_chs.length; i++){
        if (rare_chs[i] == ch) {rarity = 'rare';}
    }
    for (var i = 0; i < common_chs.length; i++){
        if (common_chs[i] == ch) {rarity = 'common';}
    }
    return '<img src="img/rarityicon_' + rarity + '.png" style="max-width:100%;max-height:100%;height:20px;width:20px;">';
};
var delete_btn = function(slug, wrap = true){
    var code = 'onclick="delete_card(\'' + slug + '\');" href="javascript:void();" ';
    var h = '';
    if (slug.includes('_lvl_18')){
        slug = slug.slice(0, -7);
        h = '**';
    }
    else if (slug.includes('_lvl_1')){ 
        slug = slug.slice(0, -6);
        h = '';
    }
    else {
        h='*';
    }
    var style = '';
    if (wrap != false){
        var font_size = '14'
        if (slug.length > 20) font_size = '8px;'; 
        else if (slug.length > 18) font_size = '9px;'; 
        else if (slug.length > 16) font_size = '10px;'; 
        else if (slug.length > 14) font_size = '11px;'; 
        else if (slug.length > 12) font_size = '12px;'; 
        else font_size = '13px;';
        style = 'style="word-wrap: break-word;white-space:normal;max-width:74px;font-size:' + font_size + '"' + code + '>' + bge_img_tag(slug) + h;
    }
    else{
        style = code + ' style="width:12vw;">' + rarity_img_tag(slug) + h;
    }
    return '<button ' + style + slug + '</button>';
};
