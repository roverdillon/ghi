function cont2010() {
    document.getElementById('cont2010').style.display = 'block';
    document.getElementById('cont2013').style.display = 'none';
}
function cont2013() {
    document.getElementById('cont2013').style.display = 'block';
    document.getElementById('cont2010').style.display = 'none';
}
function yearclick(showthis,hidethis) {
    document.getElementById(hidethis).style.display = 'none';
    document.getElementById(showthis).style.display = 'block';
}
function dropNav() {
    document.getElementById("navBar").classList.toggle("show");
    if (document.getElementById("abtBar").classList.contains('show')) {
        document.getElementById("abtBar").classList.remove('show');
    }
}
function abtNav() {
    document.getElementById("abtBar").classList.toggle("show");
    if (document.getElementById("navBar").classList.contains('show')) {
        document.getElementById("navBar").classList.remove('show');
    }
}
// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.navbtn')) {

        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
function scrolltop() {
    window.scrollBy(0, 500)
}