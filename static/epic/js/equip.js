let scoreView = document.getElementById("scnoreValue");
let option4 = document.getElementById("option4");
let value4 = document.getElementById("value4");
let option3 = document.getElementById("option3");
let value3 = document.getElementById("value3");
let option2 = document.getElementById("option2");
let value2 = document.getElementById("value2");
let option1 = document.getElementById("option1");
let value1 = document.getElementById("value1");
let resultViewer = document.getElementById("resultBlock");
function score_calc() {
    score1 = parseFloat(value1.value) * get_multipler(option1.value);
    score2 = parseFloat(value2.value) * get_multipler(option2.value);
    score3 = parseFloat(value3.value) * get_multipler(option3.value);
    score4 = parseFloat(value4.value) * get_multipler(option4.value);
    resultViewer.value = score1 + score2 + score3 + score4 + " 점";
}
function get_multipler(option) {
    multipler = 1;
    switch (option) {
        case "rate":
            multipler = 1.25;
            break;
        case "critical_r":
            multipler = 2;
            break;
        case "critical_d":
            multipler = 1.43;
            break;
        case "attack":
            multipler = 1 / 128;
            break;
        case "hp":
            multipler = 1 / 600;
            break;
        case "def":
            multipler = 1 / 70;
            break;
        case "speed":
            multipler = 2;
            break;
    }
    return multipler;
}
//공/방/체/효저/효적 % 합산*1.25 + 치확*2 + 치피*1.43 + 속도*2 + 10
// 깡공 128
// 깡방 70
// 깡생 600
