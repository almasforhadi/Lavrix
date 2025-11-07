/*-----------------dropdown (Stable Hover + Click)---------------*/
document.querySelectorAll('.nav-item.dropdown').forEach(function (dropdown) {
  const toggle = dropdown.querySelector('[data-bs-toggle="dropdown"]');
  if (!toggle) return;

  const dropdownInstance = bootstrap.Dropdown.getOrCreateInstance(toggle);

  let hoverTimeout;

  dropdown.addEventListener('mouseenter', function () {
    clearTimeout(hoverTimeout);
    dropdownInstance.show();
  });

  dropdown.addEventListener('mouseleave', function () {
    hoverTimeout = setTimeout(() => {
      dropdownInstance.hide();
    }, 200); // small delay prevents flicker
  });

  // Keep it open when interacting with dropdown items
  dropdown.querySelector('.dropdown-menu').addEventListener('mouseenter', function () {
    clearTimeout(hoverTimeout);
  });
  dropdown.querySelector('.dropdown-menu').addEventListener('mouseleave', function () {
    hoverTimeout = setTimeout(() => {
      dropdownInstance.hide();
    }, 200);
  });
});



/*------------------------------New arrival view more option-------------------------- */
document.addEventListener("DOMContentLoaded", () => {
  const productCards = document.querySelectorAll(".product-card");
  const viewMoreBtn = document.getElementById("viewMoreBtn");
  const maxVisible = 8;

  // hide products after 8
  productCards.forEach((card, i) => {
    if (i >= maxVisible) card.style.display = "none";
  });

  // show all on button click
  viewMoreBtn.addEventListener("click", () => {
    productCards.forEach(card => (card.style.display = "block"));
    viewMoreBtn.style.display = "none";
  });

  // hide button if fewer than maxVisible
  if (productCards.length <= maxVisible) {
    viewMoreBtn.style.display = "none";
  }
});







/*-------------------------popup model--------------------*/

document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("loginModal");
  if (!modal) return;

  // Open modal when unauthenticated user clicks .btn-show-login-modal
  document.body.addEventListener("click", e => {
    const btn = e.target.closest(".btn-show-login-modal");
    if (btn) {
      e.preventDefault();
      modal.style.display = "flex";
      document.body.style.overflow = "hidden";
    }
  });

  // Close modal on Cancel or clicking outside
  modal.addEventListener("click", e => {
    if (e.target.classList.contains("btn-close-modal") || e.target === modal) {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  });

  // Close on ESC key
  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && modal.style.display === "flex") {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  });
});

