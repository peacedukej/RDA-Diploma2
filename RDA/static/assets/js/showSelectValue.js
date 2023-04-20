function createSelectContainer() {
  let container = document.createElement("div");
  container.className = "card-body";

  let rowDiv = document.createElement("div");
  rowDiv.className = "row";

  let titleDiv = document.createElement("div");
  titleDiv.className = "col-lg-1";

  let title = document.createElement("h5");
  title.className = "form-label h5"
  title.textContent = "Показатель: ";
  titleDiv.appendChild(title);

  let selectDiv = document.createElement("div");
  selectDiv.className = "col-lg-2";

  let table = document.getElementById('basic-datatable');
  let headerRow = table.rows[0];
  let headers = [];

  for (let i = 1; i < headerRow.cells.length; i++) {
    headers.push(headerRow.cells[i].textContent);
  }

  let selectList = document.createElement("select");
  selectList.className = "form-control form-select"
  selectList.class;
  for (let i = 0; i < headers.length; i++) {
    let option = document.createElement("option");
    option.text = headers[i];
    option.value = headers[i];
    selectList.appendChild(option);
  }

  selectDiv.appendChild(selectList);

  rowDiv.appendChild(titleDiv);
  rowDiv.appendChild(selectDiv);

  container.appendChild(rowDiv);

  let prevSibling = document.querySelector("#show_select_values ~ div.card > div.card-body");
  if (prevSibling) {
    prevSibling.after(container);
  } else {
    let showSelectValues = document.getElementById("show_select_values");
    showSelectValues.appendChild(container);
  }

  container.style.display = "block";
}

// Создаем экземпляр MutationObserver
const observer = new MutationObserver(mutations => {
  mutations.forEach(mutation => {
    let addedNodes = Array.from(mutation.addedNodes);
    let removedNodes = Array.from(mutation.removedNodes);
    if (addedNodes.some(node => node.id === "analysis-data-values")) {
      createSelectContainer();
    }
    if (removedNodes.some(node => node.id === "analysis-data-values")) {
      let container = document.querySelector("#show_select_values > div.card-body");
      if (container) {
        container.remove();
      }
    }
  });
});

// Начинаем отслеживание изменений в дереве DOM
observer.observe(document.documentElement, {
  childList: true,
  subtree: true
});