$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/get_user_id/',  // Укажите URL-путь к вашему Django-виду представления
        data: {},  //
        success: function(data) {

            var userID = data.user_id;
            $.ajax({
                type: 'GET',
                url: '/get_analysis_for_stat/',  // Укажите URL-путь к вашему Django-виду представления
                data: {user_id: userID},  // Передаем параметры на сервер (в данном случае user_id)
                success: function(data) {
                var analysisTypes = data.analysis_types.join('</option><option>');
                    $('#availableOptions').html(`
                        <select class="form-control select2 form-select" id="availableOptions" placeholder='Выберите доступный тип анализа'>

                            <option>${analysisTypes}</option>
                        </select>
                                        `);  // Обновляем содержимое контейнера
                 },
                 error: function(xhr, status, error) {
                     console.error(error);
                 }
            });
        }
    });
});