google.charts.load('current', {'packages':['corechart']});

function drawChart() {
  var ids_list = [];

  function updateChart() {
    var column_select = $("#column-select").val();
    var column_name = column_select.toLowerCase().replace(' ', '_');

    $.ajax({
      url: "/chart_data/",
      type: 'GET',
      data: {'ids_str': ids_list.join(), 'column_select': column_name},
      dataType: 'json',
      success: function (data) {
        var chartData = new google.visualization.DataTable();
        chartData.addColumn('string', 'Analysis ID');
        chartData.addColumn('number', column_select);

        for (var i = 0; i < data.length; i++) {
          var value = parseFloat(data[i]['value']);
          if (!isNaN(value)) {
            chartData.addRow([data[i]['analysis_id'].toString(), value]);
          }
        }

        var options = {
          title: column_select + ' by Analysis ID',
          curveType: 'function',
          legend: { position: 'bottom' },
          height: 500,
          hAxis: {
            title: 'Analysis ID',
            titleTextStyle: {
              bold: true,
              fontSize: 14,
            },
            slantedText: true, // поворот оси X под углом
            slantedTextAngle: 45,
          },
          vAxis: {
            title: column_select,
            titleTextStyle: {
              bold: true,
              fontSize: 14,
            },
          },
        };

        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(chartData, options);
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
      }
    });
  }

  $("#results").on("DOMNodeInserted", function(event) {
//    var ids_str = $(this).find("h5").eq(-1).text().trim();
    var ids_str = $("#results h5").last().text().trim();
ids_list = ids_str.split(' ').map(function(str) {
  return parseInt(str.trim(), 10);
});
    updateChart();
  });

  $(document).on("change", "#column-select", updateChart);
}

google.charts.setOnLoadCallback(drawChart);