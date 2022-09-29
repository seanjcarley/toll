document.getElementById("lpn_check").addEventListener("click", checkLPN);


function checkLPN(e) {
    e.preventDefault();
    var lpn = document.getElementById("id_lpn").value;
    var pan = document.getElementById("vehicle_panel")
    console.log(lpn);
    if (lpn.length > 0) {
        $.ajax({
            type: 'GET',
            url: "vehicleinfo",
            data: {'lpn': lpn},
            success: function(response) {
                var instance = JSON.parse(response["instance"]);
                if (!response["error"]) {
                    console.log(instance)
                    $("#lpn_table").prepend(
                        `<tr>
                            <td>Vehicle Make: </td>
                            <td>${instance["make"]}</td>
                        </tr>
                        <tr>
                            <td>Vehicle Model: </td>
                            <td>${instance["model"]}</td>
                        </tr>
                        <tr>
                            <td>Vehicle Colour: </td>
                            <td>${instance["color"]}</td>
                        </tr>
                        <tr>
                            <td>Vehicle Class: </td>
                            <td>${instance["class"]}</td>
                        </tr>`
                    )
                    pan.style.maxHeight = pan.scrollHeight
                }
            }
        })
    }
}