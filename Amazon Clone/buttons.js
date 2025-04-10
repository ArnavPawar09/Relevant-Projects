const button_r = document.getElementById("scroll_btn_R");
const button_l = document.getElementById("scroll_btn_L");

button_r.onclick = function() {
    document.getElementById("back_ads").scrollLeft += 1520;
    
};

button_l.onclick = function() {
    document.getElementById("back_ads").scrollLeft -= 1520;
};

const button_r_1 = document.getElementById("c2_btn_R");
const button_l_1 = document.getElementById("c2_btn_L");

button_r_1.onclick = function() {
    document.getElementById("c2_imgs").scrollLeft += 700;
    
};

button_l_1.onclick = function() {
    document.getElementById("c2_imgs").scrollLeft -= 700;
};

const button_r_2 = document.getElementById("c3_btn_R");
const button_l_2 = document.getElementById("c3_btn_L");

button_r_2.onclick = function() {
    document.getElementById("c3_imgs").scrollLeft += 700;
    
};

button_l_2.onclick = function() {
    document.getElementById("c3_imgs").scrollLeft -= 700;
};