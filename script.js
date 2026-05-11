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