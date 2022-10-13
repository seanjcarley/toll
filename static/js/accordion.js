// the below functions act in the associated panel and ensure that 
// the other panels contract

document.getElementById("acc_login").addEventListener("click", expandLogin);
document.getElementById("acc_vehicle").addEventListener("click", expandVehicle);
document.getElementById("acc_contact").addEventListener("click", expandContact);

function expandLogin() {
    this.classList.toggle("active");
    panel1 = document.getElementById("login_panel");
    panel2 = document.getElementById("vehicle_panel");
    panel3 = document.getElementById("contact_panel");
    if (panel1.style.maxHeight) {
        panel1.style.maxHeight = null;
        panel2.style.maxHeight = null;
        panel3.style.maxHeight = null;
    } else {
        panel1.style.maxHeight = panel1.scrollHeight + "px";
        panel2.style.maxHeight = null;
        panel3.style.maxHeight = null;
    }
}

function expandVehicle() {
    this.classList.toggle("active");
    panel1 = document.getElementById("login_panel");
    panel2 = document.getElementById("vehicle_panel");
    panel3 = document.getElementById("contact_panel");
    if (panel2.style.maxHeight) {
        panel1.style.maxHeight = null;
        panel2.style.maxHeight = null;
        panel3.style.maxHeight = null;
    } else {
        panel1.style.maxHeight = null;
        panel2.style.maxHeight = panel2.scrollHeight + "px";
        panel3.style.maxHeight = null;
    }
}

function expandContact() {
    this.classList.toggle("active");
    panel1 = document.getElementById("login_panel");
    panel2 = document.getElementById("vehicle_panel");
    panel3 = document.getElementById("contact_panel");
    if (panel3.style.maxHeight) {
        panel1.style.maxHeight = null;
        panel2.style.maxHeight = null;
        panel3.style.maxHeight = null;
    } else {
        panel1.style.maxHeight = null;
        panel2.style.maxHeight = null;
        panel3.style.maxHeight = panel3.scrollHeight + "px";
    }
}
