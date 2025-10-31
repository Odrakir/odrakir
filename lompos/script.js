const DOT_COLUMNS = 20;
const DOT_ROWS = 14;

function createDotElement() {
  const dot = document.createElement("div");
  dot.classList.add("dot");
  return dot;
}

function populateGrid(gridElement) {
  const fragment = document.createDocumentFragment();

  for (let row = 0; row < DOT_ROWS; row += 1) {
    for (let column = 0; column < DOT_COLUMNS; column += 1) {
      fragment.appendChild(createDotElement());
    }
  }

  gridElement.appendChild(fragment);
}

document.addEventListener("DOMContentLoaded", () => {
  const grid = document.querySelector(".dot-grid");

  if (grid) {
    populateGrid(grid);
  }
});
