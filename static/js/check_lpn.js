document.getElementById("lpn_check").addEventListener("click", checkLPN);


function checkLPN(e) {
    e.preventDefault();  // prevent page reload and default actions 
    var lpn = document.getElementById("id_lpn").value;
    if (lpn.length > 0) {
        $.ajax({
            type: 'GET',
            url: "vehicleinfo",
            data: {'lpn': lpn},
            success: function(response) {
                var instance = JSON.parse(response["instance"]);
                if (!response["error"]) {
                    console.log(instance)
                    document.getElementById("vehicle_title").innerHTML = `Vehicle Details for <strong>${instance["lpn"]}</strong>`
                    document.getElementById("vehicle_make").innerHTML = `Vehicle Make: <strong>${instance["make"]}</strong>`
                    document.getElementById("vehicle_model").innerHTML = `Vehicle Model: <strong>${instance["model"]}</strong>`
                    document.getElementById("vehicle_colour").innerHTML = `Vehicle Colour: <strong>${instance["color"]}</strong>`
                    document.getElementById("vehicle_class").innerHTML = `Vehicle Class: <strong>${instance["class"]}</strong>`
                    $("#vehicleModal").modal("show")
                }
            },
            error: function (response) {
                console.log(response);
                alert("Please check the LPN entered as it is not showing on the Department of Motor Vehicles Database!")
                var vdeets = $("#id_lpn");
                vdeets.val("");
                vdeets.focus();
            }
        })
    }
}
