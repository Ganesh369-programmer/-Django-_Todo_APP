 function changeColor(clickedDiv) {
    clickedDiv.style.backgroundColor = 'green'; // Change the color of the clicked div to red
  }


  function openSlider(title, description) {
    document.getElementById("slider-title").innerText = title;
    document.getElementById("slider-desc").innerText = description;
    document.getElementById("todo-slider").classList.add("open");
}

function closeSlider() {
    document.getElementById("todo-slider").classList.remove("open");
}
