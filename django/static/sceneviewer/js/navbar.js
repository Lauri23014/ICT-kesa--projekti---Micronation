  document.getElementById("paw-trigger").onclick = function () {
    document.querySelectorAll("#navlinks ul li").forEach(function (li) {
      li.classList.toggle("visible");
    });
  };