document.getElementById("id_username").addEventListener("blur", checkUname);


function checkUname(e) {
    e.preventDefault();
    var uname = $(this).val();
    // console.log(uname);
    if (uname != "") {
        $.ajax({
            type: 'GET',
            url: "checkusername",
            data: {'username': uname},
            success: function (response) {
                if (!response["valid"]) {
                    alert("This Username is not Valid. Please try a new one.")
                    var uName = $("#id_username");
                    uName.val("")
                }
            },
            error: function (response) {
                console.log(response)
            }
        })
    }
}
