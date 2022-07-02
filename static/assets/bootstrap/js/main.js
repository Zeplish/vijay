
function predict_sample(){
    var str = 
`>seq1
EGDVFIMPAAHPVAI
>seq2
AAVAAAASVPAA
>seq3
NVLHSAFEVG
>seq4
DNVLHSAFEV
>seq5
FRDRARVPLTSNNGI
>seq6
DVVPMSQQPFQIELN`
    document.getElementById("input_area").value = str;
}
function design_sample(){
    var str =`FFYTPMSRREVED`

    document.getElementById("design_input_area").value =str;
}
function protein_sample(){
    var str =`DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVIAFGISNYCQIYPPNANKIREALAQPQRYCREVDVPGIDPNACHYMKCPLVKGQQYDIKYTWIVPKIAPKSEN`
    document.getElementById("pro_input_area").value =str;
}
document.getElementById("threshold").value = 0.06
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}