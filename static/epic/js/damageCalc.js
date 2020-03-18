var charactorSelecter = document.getElementById("CharactorSelect");
var critivalInput = document.getElementById("criticalDamage");
var attackInput = document.getElementById("attack");
var attackRankInput = document.getElementById("attacRank");
var otherInput = document.getElementById("other");
var otherRankInput = document.getElementById("otherRank");
var powInput = document.getElementById("Pow");
var defenseInput = document.getElementById("Dep");
var extendDamageInput = document.getElementById("extendDamage");
var elementWinInput = document.getElementById("elementWin");
var calcedDamageOut = document.getElementById("calcedDamage");
var rankViewer = document.getElementById("RankList");
var isSpeed = document.getElementById("isSpeed");
function dropOut0(value) {
    if (value < 0) return 0;
    return value;
}
function calculate() {
    var attack = attackInput.value;
    damage = attack * attackRankInput.value;
    attack = otherInput.value * otherRankInput.value;
    if (isSpeed.checked) {
        damage = (attack + 1) * damage * powInput.value;
    } else {
        damage = (damage + attack) * powInput.value;
    }
    damage = (critivalInput.value * damage) / 100;
    damage = damage / (defenseInput.value / 300 + 1);
    temp = dropOut0(extendDamageInput.value / 100);
    damage = (temp + 1) * damage;
    if (elementWinInput.checked) {
        damage = damage * 1.1;
    }
    damage = damage * 1.871;
    calcedDamageOut.innerText = parseInt(damage * 100) / 100;
}

function getSkillRank() {
    selectedValue =
        charactorSelecter.options[charactorSelecter.selectedIndex].value;
    var req = new XMLHttpRequest();
    req.open("GET", "https://api.epicsevendb.com/api/hero/" + selectedValue);
    req.addEventListener("load", function() {
        if (req.status != 200) {
            console.log("failed to load");
            return;
        }
        json = JSON.parse(req.responseText);
        data = json["results"][0]["skills"];
        rankViewer.innerHTML = "";
        for (i = 0; i < data.length; i++) {
            str = "<td>";
            validSoulBurn = parseFloat(data[i].soulBurn) != 0;
            damageModifiers = data[i].damageModifiers;
            for (DM in damageModifiers) {
                dm = damageModifiers[DM];
                str += dm.name + " : " + String(dm.value);
                if (validSoulBurn == true) {
                    str += "<small> ( " + String(dm.soulburn) + " )</small>";
                }
                str += "<br>";
            }
            str += "</td>";
            rankViewer.innerHTML += str;
        }
    });
    req.send(null);
}
