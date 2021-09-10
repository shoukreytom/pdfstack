const dialog = document.getElementById("upload-dialog");
var dialogIsOpen = false;

function toggleDialog() {
    if(dialogIsOpen) {
        dialog.setAttribute("close", true);
        dialog.removeAttribute("open");
        dialogIsOpen = false;
    }
    else {
        dialog.setAttribute("open", true);
        dialog.removeAttribute("close");
        dialogIsOpen = true;
    }
}

const dialogBtn = document.getElementById("dialog-btn");
dialogBtn.addEventListener("click", function(event) {
    event.preventDefault();
    toggleDialog();
});
const closeDialogBtn = document.getElementById("dialog-close");
closeDialogBtn.addEventListener("click", function() {
	toggleDialog();
});
