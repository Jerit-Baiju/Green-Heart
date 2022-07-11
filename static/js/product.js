document.getElementById('rs').innerText = main_pack
function refresh_pack() {
  quantity = document.getElementById("pack").value;
  document.getElementById("rs").innerText = "RS. " + pack[quantity - 1] + ".00";
}
