document.getElementById("lpn_check").addEventListener("click", checkLPN);
document.getElementById("confirm").addEventListener("click", confirmLPN)
document.getElementById("re-enter").addEventListener("click", clearField);
// document.getElementById("lpn_remove").addEventListener("click", removeLPN);

function checkLPN(e) {
    e.preventDefault();  // prevent page reload and default actions 
    var lpn = document.getElementById("id_lpn").value;
    var name = document.getElementById("lpn_check").name;
    if (lpn.length > 0) {
        $.ajax({
            type: 'GET',
            url: "vehicleinfo",
            data: {'lpn': lpn},
            success: function(response) {
                // if the vehicle is not registered on another account and
                // the vehicle is in the VehicleDetails table return the 
                // vehicle info
                if (response["valid"]) {
                    var instance = JSON.parse(response["instance"]);
                    console.log(instance)
                    document.getElementById("vehicle_title").innerHTML = `Vehicle Details for <strong>${instance["lpn"]}</strong>`
                    document.getElementById("vehicle_make").innerHTML = `Vehicle Make: <strong>${instance["make"]}</strong>`
                    document.getElementById("vehicle_model").innerHTML = `Vehicle Model: <strong>${instance["model"]}</strong>`
                    document.getElementById("vehicle_colour").innerHTML = `Vehicle Colour: <strong>${instance["color"]}</strong>`
                    document.getElementById("vehicle_class").innerHTML = `Vehicle Class: <strong>${instance["class"]}</strong>`
                    if (name === "signup") {
                        // if called from the signup page, display the <p> 
                        // advising that only one vehicle can be registered 
                        // during signup, and additional vehicles can be added 
                        // once the account is created.
                        document.getElementById("signup").style.display = "block"
                    }
                    $("#vehicleModal").modal("show")
                } else {    
                    // if vehicle is registered clear the field and reload the 
                    // page so that the error toast is displayed
                    location.reload()
                    clearField()
                }
            },
            error: function (response) {
                // if vehicle is no on the VehicleDetails table, clear the
                // field, and reload the page so that the error toast is 
                // displayed
                location.reload()
                clearField()
            }
        })
    }
};

function confirmLPN(e) {
    document.getElementById("lpn_check").style.display = "none"
    document.getElementById("add_vehicle").style.display = "block"
};

function removeLPN(e) {
    for (v in vehicles) {
        if (document.getElementById(`checkbox_${v.lpn}`).checked == true) {
            console.log(v.lpn);
        }
    }
}

function clearField() {
    // clear and refocus on the field
    var vdeets = $("#id_lpn");
    vdeets.val("");
    vdeets.focus();
};