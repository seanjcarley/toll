lst = document.getElementsByClassName("accordion");
ids = [];

for (i = 0; i < lst.length; i++){
	ids.push(lst[i].id);
}

for (j = 0; j < ids.length; j++) {
	document.getElementById(ids[j]).addEventListener("click", expand);
}

function expand() {
	if(this.nextElementSibling.style.maxHeight) {
		this.nextElementSibling.style.maxHeight = null;
	} else {
		this.nextElementSibling.style.maxHeight = this.nextElementSibling.scrollHeight + "px";
	}
}