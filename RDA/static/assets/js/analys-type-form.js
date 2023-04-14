function addAnalysisForm() {
    let select_info = document.getElementById('add-analysis-info');
    select_info.style.display = "none";

    let select = document.getElementById('add-analysis-form-select');
    let block = document.querySelectorAll('.selected-form');
    let lastIndex = 0; // После каждой смены опции, сохраняем сюда индекс предыдущего блока

    select.addEventListener('change', function() {
      block[lastIndex].style.display = "none";
      // Чтобы сразу делать именно его невидимым при следующей смене

      let index = select.selectedIndex; // Определить индекс выбранной опции
      block[index].style.display = "block"; // Показать блок с соответствующим индексом

      lastIndex = index; // Обновить сохраненный индекс.
    });
}

//function addValuesForm() {
//
//    let select_info = document.getElementById('add-analysis-info');
//    select_info.style.display = "none";
//
//
//    let select = document.getElementById('add-analysis-form-select');
//    let block = document.querySelectorAll('.selected-form');
//    let lastIndex = 0; // После каждой смены опции, сохраняем сюда индекс предыдущего блока
//
//    select.addEventListener('change', function() {
//      block[lastIndex].style.display = "none";
//      // Чтобы сразу делать именно его невидимым при следующей смене
//
//      let index = select.selectedIndex; // Определить индекс выбранной опции
//      block[index].style.display = "block"; // Показать блок с соответствующим индексом
//
//      lastIndex = index; // Обновить сохраненный индекс.
//    });

//    select.addEventListener('change', function() {
//
//    }
//    }
//    let block = document.querySelectorAll('.selected-form');

}


//  function addAnalysisForm() {
//
//// Ничего не выбрано
//      var passElement = document.querySelectorAll('input[value="pass"]');
//      var passSelectedOptionBlockElement = document.getElementById("pass-selected");
//
//      // Выбран общий анализ крови
//      var a1Element = document.querySelectorAll('input[value="a1"]');
//      var a1SelectedOptionBlockElement = document.getElementById("a1-selected");
//
//      // Выбран общий анализ мочи
//      var a2Element = document.querySelectorAll('input[value="a2"]');
//      var a2SelectedOptionBlockElement = document.getElementById("a2-selected");
//
//      // Выбран анализ на с-реактивный белок
//      var a3Element = document.querySelectorAll('input[value="a3"]');
//      var a3SelectedOptionBlockElement = document.getElementById("a3-selected");
//
//      // Выбран ревматоидный фактор
//      var a4Element = document.querySelectorAll('input[value="a4"]');
//      var a4SelectedOptionBlockElement = document.getElementById("a4-selected");
//
//      // Выбран аццп
//      var a5Element = document.querySelectorAll('input[value="a5"]');
//      var a5SelectedOptionBlockElement = document.getElementById("a5-selected");
//
//      if (passElement && passSelectedOptionBlockElement) {
//        passSelectedOptionBlockElement.style.display = "block";
//        a1SelectedOptionBlockElement.style.display = "none";
//        a2SelectedOptionBlockElement.style.display = "none";
//        a3SelectedOptionBlockElement.style.display = "none";
//        a4SelectedOptionBlockElement.style.display = "none";
//        a5SelectedOptionBlockElement.style.display = "none";
//      }
//
//      if (a1Element && a1SelectedOptionBlockElement) {
//        passSelectedOptionBlockElement.style.display = "none";
//        a1SelectedOptionBlockElement.style.display = "block";
//        a2SelectedOptionBlockElement.style.display = "none";
//        a3SelectedOptionBlockElement.style.display = "none";
//        a4SelectedOptionBlockElement.style.display = "none";
//        a5SelectedOptionBlockElement.style.display = "none";
//      }
//
//      if (a2Element && a2SelectedOptionBlockElement) {
//        passSelectedOptionBlockElement.style.display = "none";
//        a1SelectedOptionBlockElement.style.display = "none";
//        a2SelectedOptionBlockElement.style.display = "block";
//        a3SelectedOptionBlockElement.style.display = "none";
//        a4SelectedOptionBlockElement.style.display = "none";
//        a5SelectedOptionBlockElement.style.display = "none";
//      }
//
//      if (a3Element && a3SelectedOptionBlockElement) {
//        passSelectedOptionBlockElement.style.display = "none";
//        a1SelectedOptionBlockElement.style.display = "none";
//        a2SelectedOptionBlockElement.style.display = "none";
//        a3SelectedOptionBlockElement.style.display = "block";
//        a4SelectedOptionBlockElement.style.display = "none";
//        a5SelectedOptionBlockElement.style.display = "none";
//      }
//
//      if (a4Element && a4SelectedOptionBlockElement) {
//        passSelectedOptionBlockElement.style.display = "none";
//        a1SelectedOptionBlockElement.style.display = "none";
//        a2SelectedOptionBlockElement.style.display = "none";
//        a3SelectedOptionBlockElement.style.display = "none";
//        a4SelectedOptionBlockElement.style.display = "block";
//        a5SelectedOptionBlockElement.style.display = "none";
//      }
//
//      if (a5Element && a5SelectedOptionBlockElement) {
//        passSelectedOptionBlockElement.style.display = "none";
//        a1SelectedOptionBlockElement.style.display = "none";
//        a2SelectedOptionBlockElement.style.display = "none";
//        a3SelectedOptionBlockElement.style.display = "none";
//        a4SelectedOptionBlockElement.style.display = "none";
//        a5SelectedOptionBlockElement.style.display = "block";
//      }
//    }