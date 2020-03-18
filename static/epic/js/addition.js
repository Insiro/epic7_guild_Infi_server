function go_table() {
    if (arguments.length < 1) {
        location.href = "Tables?table=" + "None";
    } else {
        location.href = "Tables?table=" + arguments[0];
    }
}

function go_detail() {
    //argu[0]:id, argu[1]:table
    if (arguments.length < 1) {
        location.href = "detail?id=" + "None";
    } else {
        location.href = "detail?id=" + arguments[0] + "&table=" + arguments[1];
    }
}

function gotoPost() {
    let isAuthorized = false;
    req = new XMLHttpRequest();
    req.open("GET", "api/isAuthrized");
    req.addEventListener("load", function() {
        if (req.status >= 200 && req.status < 300) {
            json = JSON.parse(loginXhttpRequest.responseText);
            isAuthorized = json.result;
            if (isAuthorized == true) {
                location.href = "/epic/post";
            } else {
                alert("Require Sign-In");
            }
        } else {
            alert("Require Sign-In");
        }
    });
    req.send(null);
}

function nullDialog() {
    var name = document.getElementById("dialogName");
    var detailBtn = document.getElementById("detailBtn");
    var content = document.getElementById("dialogContents");
    content.innerHTML = "None";
    name.innerText = "None";
    detailBtn.addEventListener("click", function() {
        location.href = "detail?id=None";
    });
}
function copyText(st) {
    copyDummy = document.createElement("textarea");
    document.body.appendChild(copyDummy);
    copyDummy.value = st;
    copyDummy.select();
    document.execCommand("copy");
    document.body.removeChild(copyDummy);
}
function MSGDialog(str) {
    var content = document.getElementById("simpleContents");
    content.innerHTML += String(str)
        .split("\n")
        .join("<br>");
    $("#simpleDialog").modal("show");
}
function viewDialog() {
    //arg0=id
    if (arguments.length < 1) nullDialog();
    else {
        var name = document.getElementById("dialogName");
        var detailBtn = document.getElementById("detailBtn");
        var content = document.getElementById("dialogContents");
        var req = new XMLHttpRequest();
        var id = arguments[1];
        var table = arguments[0];
        req.open("GET", "info?table=" + table + "&id=" + id);
        req.addEventListener("load", function() {
            if (req.status != 200) {
                nullDialog();
                return;
            }
            detailBtn.addEventListener("click", function() {
                go_detail(id, table);
            });
            content.innerHTML = "<a href='javascript:;' onclick=\"copyText('insiro.me/epic/detail?table=" + table + "&id=" + id + "')\"><small>주소 복사</small></a>";

            content.innerHTML += "<table id='diatable'></table>";
            var data = JSON.parse(req.responseText);
            name.innerText = data.name;
            content.innerHTML += "<h6>Writer : " + data.writer + "</h6>";
            if (data.linkName != null && data.link != null) content.innerHTML += "<a href = '" + data.link + "'>" + data.linkName + "</a>";
            else if (data.link != null) content.innerHTML += "<a href = '" + data.link + "'>link</a>";
            if (data.contents != null)
                content.innerHTML +=
                    "<p>" +
                    data.contents
                        .split("\n")
                        .join("<br>")
                        .split(" ")
                        .join("&nbsp;")
                        .split("<a&nbsp;")
                        .join("<a ")
                        .split("a&nbsp;>")
                        .join("a>") +
                    "</p>";
            if (data.memo != null)
                content.innerHTML +=
                    "<p>" +
                    data.memo
                        .split("\n")
                        .join("<br>")
                        .split(" ")
                        .join("&nbsp;")
                        .split("<a&nbsp;")
                        .join("<a ")
                        .split("a&nbsp;>")
                        .join("a>") +
                    "</p>";
            if (data.image != null && data.image != "") content.innerHTML += "<img class='modalImg' src='https://insiro.me/media/" + data.image + "'>";
            if (data.imageLink != null && data.imageLink != "") content.innerHTML += "<img class='modalImg'src='" + data.imageLink + "'>";
        });
        req.send(null);
    }
    $("#modalDialog").modal("show");
}

function addFooter() {
    var footerdiv = document.getElementById("footer");
    var footerstr = '<div class="copyright text - center my - auto "> <span > Copyright© Your Website 2019 </span> </div > ';
    footerstr += "";
    footerdiv.innerHTML = footerstr;
}
