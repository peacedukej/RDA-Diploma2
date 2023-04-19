$(document).ready(function() {
  $("#get-statistics").click(function() {
    var results = document.getElementById("results"); // Получаем элемент с id "results"
    var h5Element = results.getElementsByTagName("h5")[0]; // Получаем h5-элемент
    var bElement = h5Element.getElementsByTagName("b")[0]; // Получаем b-элемент, который содержит числовые значения
    var numbers = bElement.innerText; // Получаем числовые значения из b-элемента
    var data = {
      "numbers": numbers
    }
    $.ajax({
      type: "GET",
      url: "get_values_for_stat/",
      data: data,
      success: function(response) {
        // Получаем список значений по analysis_id
        var values = response.values;
        // Получаем список analysis_id
        var analysis_ids = Object.keys(values);

        // Формируем таблицу
        var table = '<table class="table table-bordered text-nowrap border-bottom dataTable no-footer" id="basic-datatable" role="grid" aria-describedby="basic-datatable_info">';
        // Формируем заголовок таблицы
        table += '<thead><tr><th>Analysis ID</th>';
        // Формируем заголовки столбцов
        for (var i = 1; i <= 30; i++) {
          table += '<th>Value ' + i + '</th>';
        }
        table += '</tr></thead>';
        // Формируем тело таблицы
        table += '<tbody>';
        // Проходим по каждому analysis_id в списке
        for (var j = 0; j < analysis_ids.length; j++) {
          var analysis_id = analysis_ids[j];
          // Формируем строку таблицы для каждого analysis_id
          table += '<tr><td>' + analysis_id + '</td>';
          // Проходим по каждому value для текущего analysis_id
          for (var i = 1; i <= 30; i++) {
            var field_name = "value_" + i;
            var value = values[analysis_id][field_name];
            if (value != null) {
              // Преобразуем значение в строку
//              value = String(value);
            } else {
              value = 'd';
            }
            // Вставляем значение в строку таблицы
            table += '<td>' + value + '</td>';
          }
          table += '</tr>';
        }
        table += '</tbody></table>';

        // Вставляем таблицу в элемент с id "analysis_values"
        $("#analysis_values").html(table);
      },
    });
  });
});