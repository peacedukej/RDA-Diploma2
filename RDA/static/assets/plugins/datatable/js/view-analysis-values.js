// JavaScript код, связанный с вашей страницей
var analysisButtons = document.getElementsByClassName('btn-analysis-details');
for (var i = 0; i < analysisButtons.length; i++) {
  analysisButtons[i].addEventListener('click', function(event) {
    // Получаем значение data-analysis-id кнопки
    var analysisId = event.target.getAttribute('data-analysis-id');
    // Обновляем заголовок всплывающего окна
    var modalTitle = document.getElementById('modal-title');
    modalTitle.innerText = 'Просмотр значений анализа №' + analysisId;
  });
}