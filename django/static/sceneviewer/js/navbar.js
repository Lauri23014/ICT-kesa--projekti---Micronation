document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("navbar-toggle");
  const navLinks = document.querySelector("#navlinks ul");

  toggleBtn.addEventListener("click", function () {
    navLinks.classList.toggle("visible");
    toggleBtn.classList.toggle("active");
  });
});
