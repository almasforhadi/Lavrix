// --- Chart.js Setup ---
function createGradient(ctx, color) {
  if (!ctx) return color;
  const gradient = ctx.createLinearGradient(0, 0, 0, 300);
  gradient.addColorStop(0, color + "cc");
  gradient.addColorStop(1, color + "00");
  return gradient;
}


// Line Chart: Orders Over Time
const ordersCanvas = document.getElementById("ordersChart");
if (ordersCanvas) {
  const ctx = ordersCanvas.getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
      datasets: [{
        label: "Orders",
        data: [4, 6, 5, 9, 12, 10, 15],
        borderColor: "#0d6efd",
        backgroundColor: createGradient(ctx, "#0d6efd"),
        fill: true,
        tension: 0.4,
        pointRadius: 4,
        pointHoverRadius: 6
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false } },
        y: { beginAtZero: true, ticks: { stepSize: 5 } }
      }
    }
  });
}

// Doughnut Chart: Spending
const spendCanvas = document.getElementById("spendingChart");
if (spendCanvas) {
  const ctx2 = spendCanvas.getContext("2d");
  new Chart(ctx2, {
    type: "doughnut",
    data: {
      labels: ["Electronics", "Fashion", "Shoes", "Home", "Accessories"],
      datasets: [{
        data: [400, 300, 250, 150, 200],
        backgroundColor: ["#0d6efd", "#ffc107", "#198754", "#dc3545", "#6f42c1"],
        borderWidth: 1,
        hoverOffset: 10
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
          labels: { usePointStyle: true, boxWidth: 8, font: { size: 13 } }
        }
      }
    }
  });
}

