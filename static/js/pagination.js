  /*------------------------Pagignation-------------------------*/
  
document.addEventListener("click", function (e) {
  const link = e.target.closest(".pagination a");
  if (!link) return;

  e.preventDefault();
  const url = link.getAttribute("href");
  const container = document.querySelector("#product-container");

  // Optional: show loading state
  container.style.opacity = 0.6;

  fetch(url, {
    headers: { "X-Requested-With": "XMLHttpRequest" }
  })
    .then(res => res.text())
    .then(html => {
      container.innerHTML = html;
      container.style.opacity = 1;
      window.scrollTo({ top: container.offsetTop - 80, behavior: "smooth" });
    })
    .catch(err => {
      console.error("Pagination error:", err);
      container.style.opacity = 1;
    });          
});