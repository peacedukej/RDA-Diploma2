
$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/get_user_id/',  // Укажите URL-путь к вашему Django-виду представления
        data: {},  //
        success: function(data) {

            var userID = data.user_id;
            // Обрабатываем изменение выбора в выпадающем списке
            $(document).on('change', '#availableOptions select', function(e) {
                // Получаем выбранный вариант
                var selectedOption = $(this).find(":selected").text();
                // Выполняем ajax-запрос на сервер
                $.ajax({
                    type: 'GET',
                    url: '/get_analysis_id/', // URL вашего обработчика
                    data: { option: selectedOption, user_id: userID }, // Параметры запроса
                    success: function(data) {
                        var analysisIDs = data.analysis_list.join(" ");
                            $('#results').html(`

                             <h5 class="form-label h5">${analysisIDs}</h5>


                           `);
                    },
                    error: function(xhr, status, error) {
                        // Обработка ошибки
                        console.error(error);
                    }
                });
            });
        }
    });
});