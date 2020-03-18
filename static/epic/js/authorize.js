function login() {
    datas = {
        uid: document.getElementById("login_id").value,
        upw: document.getElementById("login_pwd").value
    };
    data = new FormData();
    data.append("data", JSON.stringify(datas));
    req = new XMLHttpRequest();
    req.open("POST", "api/authorize", true);
    req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=unicode");
    req.addEventListener("load", function() {
        json = JSON.parse(req.responseText);
        reloadLoginState(true);
    });
    req.send(data);
}

function reloadLoginState(loginBox) {
    loginXhttpRequest = new XMLHttpRequest();
    if (loginBox) {
        $("#Login").modal("hide");
    }

    loginXhttpRequest.open("GET", "api/isAuthrized");
    loginXhttpRequest.addEventListener("load", function() {
        var log_in_item = document.getElementById("logged_nav").style;
        var un_log_in_tem = document.getElementById("unlogged_nav").style;
        json = JSON.parse(loginXhttpRequest.responseText);
        if (json.result) {
            log_in_item.display = "none";
            un_log_in_tem.display = "";
        } else {
            log_in_item.display = "";
            un_log_in_tem.display = "none";
        }
    });

    loginXhttpRequest.send(null);
}

function loginRequest() {
    var id = document.getElementById("login_id").value;
    var pw = document.getElementById("login_pwd").value;

    var xhttp = new XMLHttpRequest();

    // Testing Code Only
    xhttp.open("POST", "php/makelogin.php");

    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=utf-8");
    xhttp.addEventListener("load", function() {
        parsedJson = JSON.parse(xhttp.responseText);
        console.log(parsedJson);
        if (parsedJson.success) {
            reloadLoginState(true);
        } else {
            console.error("login error");
        }
    });

    xhttp.send(
        JSON.stringify({
            UID: id,
            UPW: pw
        })
    );
}

function logout() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "api/signOut");

    xhttp.addEventListener("load", function() {
        reloadLoginState(false);
    });

    xhttp.send(null);
}

function signUp(data) {
    if (data.pwd.value != data.check.value) {
        return false;
    }
    return true;
}
