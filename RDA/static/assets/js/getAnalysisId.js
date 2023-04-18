$(document).ready(function() {
    // Обрабатываем изменение выбора в выпадающем списке
    $(document).on('change', '#availableOptions select', function(e) {
        // Получаем выбранный вариант
        var selectedOption = $(this).find(":selected").text();
        // Выполняем ajax-запрос на сервер
        $.ajax({
            type: 'GET',
            url: '/get_analysis_id/', // URL вашего обработчика
            data: { option: selectedOption }, // Параметры запроса
            success: function(data) {
            var analysisIDs = data.analysis_list;
                $('#results').html(`
                        ${analysisIDs}
                                        `);
            },
            error: function(xhr, status, error) {
                // Обработка ошибки
                console.error(error);
            }
        });
    });
});