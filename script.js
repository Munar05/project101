var cart = JSON.parse(localStorage.getItem("cart")) || [];

function add(name, price) {
    cart.push({name: name, price: price});
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Добавлено в корзину");
}

function showCart() {
    var list = document.getElementById("list");
    var total = document.getElementById("total");

    if (!list) return; // защита если не та страница

    list.innerHTML = "";

    var sum = 0;

    for (var i = 0; i < cart.length; i++) {
        var item = cart[i];
        sum += item.price;

        var div = document.createElement("div");
        div.className = "cart-item";

        div.innerHTML =
            "<span>" + item.name + " - " + item.price + " ₸</span>" +
            "<button onclick='removeItem(" + i + ")'>Удалить</button>";

        list.appendChild(div);
    }

    total.innerHTML = "Итого: " + sum + " ₸";
}

function removeItem(index) {
    cart.splice(index, 1);
    localStorage.setItem("cart", JSON.stringify(cart));
    showCart();
}