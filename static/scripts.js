/** @format */

// Select gallery and initialize scroll position
const gallery = document.querySelector(".gallery");
let scrollPosition = 0;

// Function to get gallery item width dynamically
function getGalleryItemWidth() {
  const galleryItem = document.querySelector(".gallery-item");
  return (
    galleryItem.offsetWidth +
    parseInt(window.getComputedStyle(galleryItem).marginRight)
  ); // Include margin
}

// Function to reset the scroll position to fit within bounds when resizing
const resetScrollPosition = () => {
  const galleryWidth = gallery.scrollWidth;
  const visibleWidth = gallery.clientWidth;

  // If the scroll position is out of bounds after resize, reset to the max possible position
  if (scrollPosition > galleryWidth - visibleWidth) {
    scrollPosition = galleryWidth - visibleWidth;
    gallery.style.transform = `translateX(-${scrollPosition}px)`;
  }
};

// Scroll step: dynamically calculate the width of a gallery item
const updateScroll = () => {
  const scrollStep = getGalleryItemWidth();

  // Left Button Click - Scroll Left
  document.getElementById("gallery-prev").addEventListener("click", () => {
    if (scrollPosition > 0) {
      scrollPosition -= scrollStep;
      if (scrollPosition < 0) scrollPosition = 0; // Prevent overscrolling
      gallery.style.transform = `translateX(-${scrollPosition}px)`;
    }
  });

  // Right Button Click - Scroll Right
  document.getElementById("gallery-next").addEventListener("click", () => {
    const maxScrollPosition = gallery.scrollWidth - gallery.clientWidth;
    if (scrollPosition < maxScrollPosition) {
      scrollPosition += scrollStep;
      if (scrollPosition > maxScrollPosition)
        scrollPosition = maxScrollPosition; // Prevent overscrolling
      gallery.style.transform = `translateX(-${scrollPosition}px)`;
    }
  });

  // Recalculate the scroll position on window resize
  window.addEventListener("resize", () => {
    resetScrollPosition(); // Reset scroll position on resize
  });
};

// Initial call to set up scroll functionality
updateScroll();
resetScrollPosition(); // Call reset scroll position to handle load

// Example of a fade-in animation
document.addEventListener("DOMContentLoaded", function () {
  let elements = document.querySelectorAll(".card");
  elements.forEach((element) => {
    element.classList.add("fade-in");
  });
});
