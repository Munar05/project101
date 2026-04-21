var cart = [];

function add(name, price) {
    cart.push({n: name, p: price});
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Добавлено");
}

function showCart() {
    var data = localStorage.getItem("cart");

    if (data) {
        cart = JSON.parse(data);
    }

    var ul = document.getElementById("c");
    var s = 0;

    for (var i = 0; i < cart.length; i++) {
        var li = document.createElement("li");
        li.innerHTML = cart[i].n + " - " + cart[i].p;
        ul.appendChild(li);
        s += cart[i].p;
    }

    document.getElementById("sum").innerHTML = "Сумма: " + s;
}