let cart = JSON.parse(localStorage.getItem("cart")) || [];

function add(name, price) {
    cart.push({name, price});
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Добавлено в корзину");
}

/* ПОИСК */
function searchProduct(){
    let input = document.getElementById("search").value.toLowerCase();
    let cards = document.querySelectorAll(".card");

    for(let i = 0; i < cards.length; i++){
        let text = cards[i].innerText.toLowerCase();
        cards[i].style.display = text.includes(input) ? "" : "none";
    }
}

/* SIDEBAR */
function openCatalog(){
    document.getElementById("sidebar").style.width = "250px";
}

function closeCatalog(){
    document.getElementById("sidebar").style.width = "0";
}


function showCart(){

    let list = document.getElementById("list");
    let total = document.getElementById("total");

    if(!list) return;

    list.innerHTML = "";

    let sum = 0;

    for(let i = 0; i < cart.length; i++){

        let item = cart[i];

        sum += item.price;

        let div = document.createElement("div");

        div.className = "cart-item";

        div.innerHTML =
            "<span>" + item.name + " - " + item.price + " ₸</span>" +
            "<button onclick='removeItem(" + i + ")'>Удалить</button>";

        list.appendChild(div);

    }

    total.innerHTML = "Итого: " + sum + " ₸";

}

/* УДАЛЕНИЕ */
function removeItem(index){

    cart.splice(index, 1);

    localStorage.setItem("cart", JSON.stringify(cart));

    showCart();

}