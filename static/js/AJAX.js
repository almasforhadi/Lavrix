// -------AJAX + CART COUNT UPDATE-----------------
document.addEventListener("DOMContentLoaded", () => {
  const drawer = document.getElementById("cart-drawer");
  const drawerBody = document.getElementById("drawer-body");
  const totalEl = document.getElementById("cart-total");
  const countEl = document.getElementById("cart-count");
  const countElMobile = document.getElementById("cart-count-mobile"); // 🆕 mobile badge

  /* 🧮 Update cart count (total quantity) */
  function updateCartCount() {
    fetch("/cart/ajax/detail/")
      .then(res => res.json())
      .then(data => {
        const totalQty = data.items.reduce((sum, i) => sum + i.quantity, 0);
        // Update both desktop and mobile badges
        countEl.textContent = totalQty;
        countElMobile.textContent = totalQty;
        const show = totalQty > 0 ? "inline-block" : "none";
        countEl.style.display = show;
        countElMobile.style.display = show;
      })
      .catch(() => console.warn("Cart count update failed"));
  }

  /* 🧺 Load cart content inside drawer */
  function loadCart() {
    fetch("/cart/ajax/detail/")
      .then(res => res.json())
      .then(data => {
        let html = "";
        data.items.forEach(i => {
          html += `
            <div class="d-flex align-items-center mb-3 border-bottom pb-2">
              <img src="${i.image}" class="rounded me-2" style="width:60px;height:60px;object-fit:cover;">
              <div class="flex-grow-1">
                <h6 class="mb-0">${i.name}</h6>
                <div class="d-flex justify-content-between align-items-center mt-1">
                  <small>Sales price: $${i.sale_price}</small>
                  <small class="text-end">Total: $${i.subtotal}</small>
                </div>
                <div class="d-flex align-items-center mt-2">
                  <button class="btn btn-sm btn-outline-secondary btn-update" data-id="${i.id}" data-action="decrease">-</button>
                  <span class="mx-2">${i.quantity}</span>
                  <button class="btn btn-sm btn-outline-secondary btn-update" data-id="${i.id}" data-action="increase">+</button>
                  <button class="btn btn-sm btn-danger ms-auto btn-remove" data-id="${i.id}">&times;</button>
                </div>
              </div>
            </div>
          `;
        });
        drawerBody.innerHTML = html || "<p>Your cart is empty.</p>";
        totalEl.textContent = data.total;
        updateCartCount(); // refresh navbar count
      });
  }

  /* 🧭 Drawer toggle (open/close on click) */
  const cartIcons = document.querySelectorAll("#cart-icon, #cart-icon-mobile"); // 🆕 both icons
  cartIcons.forEach(icon => {
    icon.addEventListener("click", e => {
      e.preventDefault();
      drawer.classList.toggle("open");
      if (drawer.classList.contains("open")) {
        loadCart();
      }
    });
  });

  document.getElementById("drawer-close").addEventListener("click", () => {
    drawer.classList.remove("open");
  });

  /* ➕ Add to cart */
  document.body.addEventListener("click", e => {
    const btn = e.target.closest(".btn-add-cart");
    if (btn) {
      e.preventDefault();
      const id = btn.dataset.id;
      fetch(`/cart/ajax/add/${id}/`)
        .then(res => res.json())
        .then(() => {
          if (!drawer.classList.contains("open")) {
            drawer.classList.add("open");
          }
          loadCart();
          updateCartCount();
        });
    }
  });

  /* 🔁 Quantity update */
  document.body.addEventListener("click", e => {
    const btn = e.target.closest(".btn-update");
    if (btn) {
      fetch(`/cart/ajax/update/${btn.dataset.id}/?action=${btn.dataset.action}`)
        .then(res => res.json())
        .then(() => {
          loadCart();
          updateCartCount();
        });
    }
  });

  /* ❌ Remove item */
  document.body.addEventListener("click", e => {
    const btn = e.target.closest(".btn-remove");
    if (btn) {
      fetch(`/cart/ajax/remove/${btn.dataset.id}/`)
        .then(res => res.json())
        .then(() => {
          loadCart();
          updateCartCount();
        });
    }
  });

  /* 🚀 Auto load count on page load */
  updateCartCount();
});
