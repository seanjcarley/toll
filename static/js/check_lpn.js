document.getElementById("lpn_check").addEventListener("blur", checkLPN);


function checkLPN(e) {
    e.preventDefault();
    var lpn = $this.prviousElementSibling.value;
    console.log(lpn);
    if (lpn.length > 0) {
        $.ajax({
            type: 'GET',
            url: "vehicleinfo",
            data: {'lpn': lpn},
            success: function(response) {
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"]
                if (!response["error"]) {
                    
                }
            }
        })
    }
}