document.getElementById("id_username").addEventListener("blur", checkUname);
// document.getElementById("id_email").addEventListener("blur", checkEmail);

function checkUname() {
    var uname = document.getElementById("hint_id_username").innerHTML;
    if (uname.length === 0) {
        // console.log(uname);
        alert(uname);
    }
}

/*
function checkEmail() {
    var email = document.getElementById("id_email").value;
    alert(email);
}
*/