<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CAMLOR Milk Tea</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

body {
    background: #fff7f0;
    color: #333;
}

header {
    background: linear-gradient(135deg, #ff7b54, #ffb26b);
    color: white;
    text-align: center;
    padding: 30px 15px;
}

header h1 {
    font-size: 36px;
    margin-bottom: 8px;
}

header p {
    font-size: 16px;
}

.store-info {
    background: white;
    margin: 20px auto;
    padding: 20px;
    max-width: 1100px;
    border-radius: 15px;
    box-shadow: 0 3px 12px #00000015;
}

.store-info h2 {
    color: #ff7043;
    margin-bottom: 10px;
}

.container {
    max-width: 1100px;
    margin: auto;
    padding: 15px;
}

.search {
    width: 100%;
    padding: 14px;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin-bottom: 20px;
    font-size: 16px;
}

.menu {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 20px;
}

.product {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 3px 12px #00000015;
    transition: .2s;
}

.product:hover {
    transform: translateY(-4px);
}

.product img {
    width: 100%;
    height: 180px;
    object-fit: cover;
}

.product-info {
    padding: 15px;
}

.product h3 {
    margin-bottom: 8px;
}

.price {
    color: #ff5722;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 12px;
}

button {
    border: none;
    cursor: pointer;
    border-radius: 8px;
    padding: 10px 15px;
    background: #ff7043;
    color: white;
    font-weight: bold;
}

button:hover {
    background: #e64a19;
}

.cart {
    background: white;
    margin-top: 30px;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 3px 12px #00000015;
}

.cart h2 {
    color: #ff7043;
    margin-bottom: 15px;
}

.cart-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #eee;
    padding: 12px 0;
    gap: 10px;
}

.quantity button {
    padding: 5px 9px;
}

.total {
    text-align: right;
    font-size: 22px;
    font-weight: bold;
    color: #e64a19;
    margin-top: 20px;
}

.customer {
    background: white;
    margin-top: 30px;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 3px 12px #00000015;
}

.customer h2 {
    color: #ff7043;
    margin-bottom: 15px;
}

.customer input,
.customer textarea,
.customer select {
    width: 100%;
    padding: 13px;
    margin-bottom: 12px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 15px;
}

.customer textarea {
    height: 90px;
    resize: vertical;
}

.order-btn {
    width: 100%;
    margin-top: 15px;
    padding: 15px;
    font-size: 17px;
}

.receipt {
    display: none;
    background: white;
    margin-top: 30px;
    padding: 25px;
    border-radius: 15px;
    border: 2px dashed #ff7043;
}

.receipt h2 {
    color: #ff7043;
    margin-bottom: 15px;
}

footer {
    margin-top: 40px;
    padding: 25px;
    text-align: center;
    background: #333;
    color: white;
}

@media(max-width:600px) {
    header h1 {
        font-size: 28px;
    }

    .cart-item {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>
</head>

<body>

<header>
    <h1>🧋 CAMLOR MILK TEA</h1>
    <p>Trà sữa - Trà - Cà phê - Đồ ăn - Topping</p>
</header>

<div class="store-info">
    <h2>🏪 Thông tin quán</h2>
    <p>📍 Địa chỉ: Thủ Dầu Một, Bình Dương</p>
    <p>📞 Hotline: 0900 000 000</p>
    <p>🕐 Thời gian: 08:00 - 22:00</p>
</div>

<div class="container">

    <input
        type="text"
        id="search"
        class="search"
        placeholder="🔎 Tìm món ăn..."
        onkeyup="searchProducts()"
    >

    <div class="menu" id="menu"></div>

    <div class="cart">
        <h2>🛒 Giỏ hàng</h2>

        <div id="cartItems">
            <p>Chưa có sản phẩm nào.</p>
        </div>

        <div class="total">
            Tổng tiền:
            <span id="total">0 ₫</span>
        </div>
    </div>

    <div class="customer">

        <h2>👤 Thông tin người mua</h2>

        <input
            type="text"
            id="customerName"
            placeholder="Họ và tên"
        >

        <input
            type="tel"
            id="customerPhone"
            placeholder="Số điện thoại"
        >

        <textarea
            id="customerAddress"
            placeholder="Địa chỉ nhận hàng"
        ></textarea>

        <select id="delivery">
            <option value="Nhận tại quán">
                🏪 Nhận tại quán
            </option>

            <option value="Giao hàng">
                🛵 Giao hàng
            </option>
        </select>

        <button class="order-btn" onclick="placeOrder()">
            🧾 ĐẶT HÀNG
        </button>

    </div>

    <div class="receipt" id="receipt"></div>

</div>

<footer>
    © 2026 CAMLOR Milk Tea
</footer>

<script>

const products = [

{
    id: 1,
    name: "Trà sữa truyền thống",
    price: 30000,
    image: "https://images.unsplash.com/photo-1558857563-b371033873b8"
},

{
    id: 2,
    name: "Trà sữa matcha",
    price: 35000,
    image: "https://images.unsplash.com/photo-1571934811356-5cc061b6821f"
},

{
    id: 3,
    name: "Trà đào cam sả",
    price: 30000,
    image: "https://images.unsplash.com/photo-1556679343-c7306c1976bc"
},

{
    id: 4,
    name: "Trà vải",
    price: 30000,
    image: "https://images.unsplash.com/photo-1546173159-315724a31696"
},

{
    id: 5,
    name: "Cà phê sữa",
    price: 28000,
    image: "https://images.unsplash.com/photo-1511081692775-05d0f180a065"
},

{
    id: 6,
    name: "Bạc xỉu",
    price: 30000,
    image: "https://images.unsplash.com/photo-1461023058943-07fcbe16d735"
},

{
    id: 7,
    name: "Matcha latte",
    price: 40000,
    image: "https://images.unsplash.com/photo-1515823064-d6e0c04616a7"
},

{
    id: 8,
    name: "Socola đá xay",
    price: 42000,
    image: "https://images.unsplash.com/photo-1572490122747-3968b75cc699"
},

{
    id: 9,
    name: "Khoai tây chiên",
    price: 25000,
    image: "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"
},

{
    id: 10,
    name: "Gà rán",
    price: 45000,
    image: "https://images.unsplash.com/photo-1562967914-608f82629710"
},

{
    id: 11,
    name: "Xúc xích",
    price: 25000,
    image: "https://images.unsplash.com/photo-1612392062631-94dd858cba88"
},

{
    id: 12,
    name: "Bánh ngọt",
    price: 30000,
    image: "https://images.unsplash.com/photo-1551024506-0bccd828d307"

}

];

let cart = [];

function displayProducts(list = products) {

    const menu = document.getElementById("menu");

    menu.innerHTML = "";

    list.forEach(product => {

        menu.innerHTML += `

        <div class="product">

            <img
                src="${product.image}"
                alt="${product.name}"
            >

            <div class="product-info">

                <h3>${product.name}</h3>

                <div class="price">
                    ${formatMoney(product.price)}
                </div>

                <button onclick="addToCart(${product.id})">
                    + Thêm vào giỏ
                </button>

            </div>

        </div>

        `;

    });

}

function addToCart(id) {

    const product = products.find(p => p.id === id);

    const item = cart.find(p => p.id === id);

    if(item) {

        item.quantity++;

    } else {

        cart.push({
            ...product,
            quantity: 1
        });

    }

    updateCart();

}

function changeQuantity(id, amount) {

    const item = cart.find(p => p.id === id);

    if(!item) return;

    item.quantity += amount;

    if(item.quantity <= 0) {

        cart = cart.filter(p => p.id !== id);

    }

    updateCart();

}

function updateCart() {

    const cartItems = document.getElementById("cartItems");

    if(cart.length === 0) {

        cartItems.innerHTML =
            "<p>Chưa có sản phẩm nào.</p>";

        document.getElementById("total").innerText =
            "0 ₫";

        return;

    }

    let total = 0;

    cartItems.innerHTML = "";

    cart.forEach(item => {

        const money =
            item.price * item.quantity;

        total += money;

        cartItems.innerHTML += `

        <div class="cart-item">

            <div>

                <strong>${item.name}</strong>

                <br>

                ${formatMoney(item.price)}
                × ${item.quantity}

            </div>

            <div class="quantity">

                <button onclick="changeQuantity(${item.id}, -1)">
                    −
                </button>

                <button onclick
