function upload() {
    loginXhttpRequest = new XMLHttpRequest();
    loginXhttpRequest.open("GET", "api/isAuthrized");
    loginXhttpRequest.addEventListener("load", function () {
        json = JSON.parse(loginXhttpRequest.responseText);
        if (json.result) {
            alert("구현중입니다");
        } else {
            alert("Require Sign-In");
        }
    });

    loginXhttpRequest.send(null);
}
