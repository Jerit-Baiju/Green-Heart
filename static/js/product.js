document.getElementById('rate').innerText = "Rate: Rs." + main_pack + ".00/-"
document.getElementById('total').innerText = "Total: Rs." + main_pack + ".00/-"
function refresh_pack() {
  pack = document.getElementById("pack").value;
  quantity = document.getElementById('quantity').value
  alert(quantity)
  rate = price[pack - 1]
  document.getElementById("rate").innerText = "Rate: Rs." +' rate' + ".00";
  total = rate * quantity
  document.getElementById('total').innerText = "Total: Rs." + total + ".00/-"
}
