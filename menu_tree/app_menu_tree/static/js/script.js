var toggler = document.getElementsByClassName("arrow");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested-tree").classList.toggle("active");
    this.classList.toggle("arrow-down");
  });
}