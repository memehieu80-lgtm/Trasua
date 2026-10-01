import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="CAMLOR Milk Tea",
    page_icon="🧋",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #fff8f2;
}

.title {
    text-align: center;
    color: #ff7043;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
}

.store-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid #eee;
}

.product-box {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #eee;
    margin-bottom: 15px;
}

.total {
    font-size: 25px;
    font-weight: bold;
    color: #e64a19;
}

.order-box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 2px dashed #ff7043;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# THÔNG TIN QUÁN
# =========================================================

STORE_NAME = "CAMLOR MILK TEA"
STORE_ADDRESS = "Thủ Dầu Một, Bình Dương"
STORE_PHONE = "0900 000 000"
STORE_TIME = "08:00 - 22:00"


# =========================================================
# MENU
# =========================================================

products = [

    {
        "id": 1,
        "name": "Trà sữa truyền thống",
        "category": "Trà sữa",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1558857563-b371033873b8"
    },

    {
        "id": 2,
        "name": "Trà sữa matcha",
        "category": "Trà sữa",
        "price": 35000,
        "image": "https://images.unsplash.com/photo-1571934811356-5cc061b6821f"
    },

    {
        "id": 3,
        "name": "Trà sữa khoai môn",
        "category": "Trà sữa",
        "price": 35000,
        "image": "https://images.unsplash.com/photo-1544145945-f90425340c7e"
    },

    {
        "id": 4,
        "name": "Trà sữa socola",
        "category": "Trà sữa",
        "price": 35000,
        "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"
    },

    {
        "id": 5,
        "name": "Trà đào cam sả",
        "category": "Trà",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc"
    },

    {
        "id": 6,
        "name": "Trà vải",
        "category": "Trà",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1546173159-315724a31696"
    },

    {
        "id": 7,
        "name": "Trà chanh",
        "category": "Trà",
        "price": 25000,
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc"
    },

    {
        "id": 8,
        "name": "Matcha Latte",
        "category": "Đá xay",
        "price": 40000,
        "image": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7"
    },

    {
        "id": 9,
        "name": "Socola đá xay",
        "category": "Đá xay",
        "price": 42000,
        "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"
    },

    {
        "id": 10,
        "name": "Cà phê sữa",
        "category": "Cà phê",
        "price": 28000,
        "image": "https://images.unsplash.com/photo-1511081692775-05d0f180a065"
    },

    {
        "id": 11,
        "name": "Bạc xỉu",
        "category": "Cà phê",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735"
    },

    {
        "id": 12,
        "name": "Americano",
        "category": "Cà phê",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd"
    },

    {
        "id": 13,
        "name": "Gà rán",
        "category": "Đồ ăn",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1562967914-608f82629710"
    },

    {
        "id": 14,
        "name": "Khoai tây chiên",
        "category": "Đồ ăn",
        "price": 25000,
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"
    },

    {
        "id": 15,
        "name": "Xúc xích",
        "category": "Đồ ăn",
        "price": 25000,
        "image": "https://images.unsplash.com/photo-1612392062631-94dd858cba88"
    },

    {
        "id": 16,
        "name": "Bánh ngọt",
        "category": "Đồ ăn",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307"
    }

]


# =========================================================
# TOPPING
# =========================================================

toppings = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
    "Thạch dừa": 5000
}


# =========================================================
# SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = []


# =========================================================
# HÀM TIỀN
# =========================================================

def money(value):
    return f"{value:,.0f} ₫".replace(",", ".")


def add_to_cart(product, quantity, size, topping_list):

    topping_price = sum(
        toppings[t] for t in topping_list
    )

    price = product["price"]

    if size == "L":
        price += 5000

    final_price = price + topping_price

    item = {
        "name": product["name"],
        "size": size,
        "toppings": topping_list,
        "price": final_price,
        "quantity": quantity
    }

    st.session_state.cart.append(item)


def remove_item(index):

    st.session_state.cart.pop(index)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🧋 CAMLOR MILK TEA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Trà sữa • Trà • Cà phê • Đồ ăn • Topping</div>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# THÔNG TIN QUÁN
# =========================================================

st.markdown("""
<div class="store-box">

<h2>🏪 Thông tin quán</h2>

<p>📍 <b>Địa chỉ:</b> Thủ Dầu Một, Bình Dương</p>

<p>📞 <b>Hotline:</b> 0900 000 000</p>

<p>🕐 <b>Giờ mở cửa:</b> 08:00 - 22:00</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TÌM KIẾM
# =========================================================

search = st.text_input(
    "🔎 Tìm món",
    placeholder="Nhập tên món..."
)


# =========================================================
# LỌC DANH MỤC
# =========================================================

categories = [
    "Tất cả",
    "Trà sữa",
    "Trà",
    "Đá xay",
    "Cà phê",
    "Đồ ăn"
]

category = st.selectbox(
    "📋 Danh mục",
    categories
)


filtered_products = products

if category != "Tất cả":

    filtered_products = [
        p for p in filtered_products
        if p["category"] == category
    ]

if search:

    filtered_products = [
        p for p in filtered_products
        if search.lower() in p["name"].lower()
    ]


# =========================================================
# HIỂN THỊ MENU
# =========================================================

st.header("🍽️ MENU")


for start in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    row_products = filtered_products[start:start + 3]

    for col, product in zip(cols, row_products):

        with col:

            st.image(
                product["image"],
                use_container_width=True
            )

            st.subheader(product["name"])

            st.write(
                f"💰 **{money(product['price'])}**"
            )

            size = st.selectbox(
                "Size",
                ["M", "L"],
                key=f"size_{product['id']}"
            )

            selected_toppings = st.multiselect(
                "Topping",
                list(toppings.keys()),
                key=f"topping_{product['id']}"
            )

            quantity = st.number_input(
                "Số lượng",
                min_value=1,
                max_value=20,
                value=1,
                key=f"quantity_{product['id']}"
            )

            if st.button(
                "🛒 Thêm vào giỏ",
                key=f"add_{product['id']}",
                use_container_width=True
            ):

                add_to_cart(
                    product,
                    quantity,
                    size,
                    selected_toppings
                )

                st.success(
                    f"Đã thêm {product['name']}"
                )


# =========================================================
# GIỎ HÀNG
# =========================================================

st.divider()

st.header("🛒 Giỏ hàng")


if len(st.session_state.cart) == 0:

    st.info("Giỏ hàng đang trống.")

else:

    total = 0

    for index, item in enumerate(
        st.session_state.cart
    ):

        item_total = (
            item["price"] *
            item["quantity"]
        )

        total += item_total

        col1, col2, col3 = st.columns(
            [5, 2, 1]
        )

        with col1:

            topping_text = ", ".join(
                item["toppings"]
            )

            st.write(
                f"**{item['name']}** "
                f"(Size {item['size']})"
            )

            if topping_text:

                st.caption(
                    f"Topping: {topping_text}"
                )

        with col2:

            st.write(
                f"{item['quantity']} × "
                f"{money(item['price'])}"
            )

        with col3:

            if st.button(
                "🗑️",
                key=f"delete_{index}"
            ):

                remove_item(index)
                st.rerun()


    st.markdown(
        f'<div class="total">Tổng tiền: {money(total)}</div>',
        unsafe_allow_html=True
    )


# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================

st.divider()

st.header("👤 Thông tin người mua")

customer_name = st.text_input(
    "Họ và tên *",
    placeholder="Nguyễn Văn A"
)

customer_phone = st.text_input(
    "Số điện thoại *",
    placeholder="0901234567"
)

customer_address = st.text_area(
    "📍 Địa chỉ nhận hàng *",
    placeholder="Số nhà, đường, phường/xã..."
)

delivery = st.radio(
    "🚚 Hình thức nhận hàng",
    [
        "Nhận tại quán",
        "Giao hàng"
    ]
)


# =========================================================
# PHƯƠNG THỨC THANH TOÁN
# =========================================================

payment = st.selectbox(
    "💳 Phương thức thanh toán",
    [
        "Tiền mặt",
        "Chuyển khoản",
        "Thanh toán khi nhận hàng"
    ]
)


# =========================================================
# ĐẶT HÀNG
# =========================================================

st.divider()

if st.button(
    "🧾 ĐẶT HÀNG",
    type="primary",
    use_container_width=True
):

    if len(st.session_state.cart) == 0:

        st.error(
            "❌ Bạn chưa chọn món!"
        )

    elif not customer_name:

        st.error(
            "❌ Vui lòng nhập họ tên!"
        )

    elif not customer_phone:

        st.error(
            "❌ Vui lòng nhập số điện thoại!"
        )

    elif not customer_address:

        st.error(
            "❌ Vui lòng nhập địa chỉ!"
        )

    else:

        total = sum(
            item["price"] * item["quantity"]
            for item in st.session_state.cart
        )

        order_code = (
            "CAM"
            + datetime.now().strftime(
                "%d%m%H%M%S"
            )
        )

        # =========================================
        # HIỂN THỊ HÓA ĐƠN
        # =========================================

        st.markdown(
            '<div class="order-box">',
            unsafe_allow_html=True
        )

        st.success(
            f"🎉 Đặt hàng thành công! "
            f"Mã đơn: {order_code}"
        )

        st.subheader("🧾 HÓA ĐƠN")

        st.write(
            f"**Mã đơn:** {order_code}"
        )

        st.write(
            f"**Khách hàng:** {customer_name}"
        )

        st.write(
            f"**Số điện thoại:** {customer_phone}"
        )

        st.write(
            f"**Địa chỉ:** {customer_address}"
        )

        st.write(
            f"**Hình thức:** {delivery}"
        )

        st.write(
            f"**Thanh toán:** {payment}"
        )

        st.divider()

        for item in st.session_state.cart:

            item_total = (
                item["price"]
                * item["quantity"]
            )

            st.write(
                f"• {item['name']} "
                f"× {item['quantity']} "
                f"— {money(item_total)}"
            )

        st.divider()

        st.markdown(
            f"### 💰 Tổng cộng: {money(total)}"
        )

        st.write(
            f"🏪 **{STORE_NAME}**"
        )

        st.write(
            f"📍 {STORE_ADDRESS}"
        )

        st.write(
            f"📞 {STORE_PHONE}"
        )

        st.write(
            f"🕐 {STORE_TIME}"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )
