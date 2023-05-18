from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from .forms import RegisterForm, LoginForm, NewUserProfile, EditPassword, NewAnalysis, NewAnalysisFields#, NewAnalysisButton
from .models import Patient, Analysis, AnalysisFields

from django.http import JsonResponse
from . import serializers
from rest_framework import generics
# Create your views here.


def landing_page(request):
    return render(request, 'rda_frontend/my_landing.html')


def login_page(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('../account')
        else:
            messages.info(request, 'Логин или пароль введены неверно. Повторите попытку.')
    return render(request, 'rda_frontend/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('../login')


def register_page(request):
    # form = CreateUserForm()
    form = RegisterForm()
    if request.method == 'POST':
        # form = CreateUserForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login')

    context = {'form': form}
    return render(request, 'rda_frontend/register.html', context)


def check_access_group(user):
    return user.patient.access_group.endswith('Verified')



@login_required(login_url='../login', )
def account_page(request):
    form = NewUserProfile()

    if request.method == 'POST':
        form = NewUserProfile(request.POST, instance=request.user.patient)

        if form.is_valid():
            form.save()
            Patient.objects.update(access_group='Verified')

            messages.success(request, 'Данные успешно сохранены')
        # return redirect('../login')

    context = {'form': form}
    return render(request, 'rda_frontend/account.html', context)



@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def edit_profile(request):
    form = EditPassword

    if request.method == 'POST':
        form = EditPassword(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Пароль успешно изменен.')
            return redirect('../account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditPassword(request.user)
    context = {'form': form}
    return render(request, 'rda_frontend/edit-profile.html', context)

@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def documents_page(request):
    return render(request, 'rda_frontend/documents.html')

@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def analysis_page(request):
    db_analysis = Analysis.objects.filter(user_id=request.user.id)
    context = {'db_analysis': db_analysis}
    return render(request, 'rda_frontend/analysis.html', context)


def get_analysis_data(request):
    if request.method == 'GET':
        analysis_id = request.GET.get('analysis_id')  # Получение значения analysis_id из GET-параметра

        try:
            # Выполнение запроса в базу данных для получения объекта AnalysisFields по analysis_id
            analysis = AnalysisFields.objects.get(analysis_id=analysis_id)
            column_names = [field.verbose_name for field in analysis._meta.fields if getattr(analysis, field.name) is not None and getattr(analysis, field.name) != '' and getattr(analysis, field.name) != 'Null']
            column_values = [getattr(analysis, field.name) for field in analysis._meta.fields]

            #column_names = [name for name in column_names if name.value is not None and name.value != '' and name.value != 'Null']
            column_values = [value for value in column_values if value is not None and value != '' and value != 'Null']

            # Создание словаря с данными анализа
            data = {
                'column_values': column_values,
                'column_names': column_names,
            }

            # Удаление пустых значений из словаря
            # data = {key: value for key, value in data.items() if value is not None}
            # data = {key: value for key, value in data.items() if value is not None and value != '' and value != 'Null'}

            return JsonResponse(data)  # Возвращение данных в JSON-формате
        except AnalysisFields.DoesNotExist:
            return JsonResponse({'error': 'Анализ с указанным ID не найден'})  # Обработка случая, если анализ не найден
    else:
        return JsonResponse({'error': 'Некорректный метод запроса'})  # Обработка случая, если запрос не GET


def get_user_id(request):
    if request.method == 'GET':
        user_id = request.user.id
        return JsonResponse({'user_id': user_id})
    else:
        return JsonResponse({'error': 'Not an AJAX request'})



def get_analysis_for_stat(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        try:
            # Выполнение запроса в базу данных для получения объекта Analysis по analysis_id
            analysis = Analysis.objects.filter(user_id=user_id).values_list('analysis_type', flat=True).distinct()
            analysis_types = list(analysis)
            data = {
                'analysis_types': analysis_types
            }
            return JsonResponse(data)  # Возвращение данных в JSON-формате
        except Analysis.DoesNotExist:
            return JsonResponse({'error': 'Анализ с указанным ID не найден'})  # Обработка случая, если анализ не найден
    else:
        return JsonResponse({'error': 'Некорректный метод запроса'})  # Обработка случая, если запрос не GET


def get_analysis_id(request):
    if request.method == 'GET':
        analysis_type = request.GET.get("option")
        user_id = request.GET.get("user_id")
        try:
            # Получаем параметр option из Ajax-запроса

            # Ищем все analysis_id, которые относятся к данному analysis_type
            analysis_ids = Analysis.objects.filter(analysis_type=analysis_type, user_id=user_id).values_list('analysis_id', flat=True)
            # Конвертируем QuerySet в список и отдаем их в JSON-формате
            analysis_list = list(analysis_ids)
            data = {
                'analysis_list': analysis_list
            }
            return JsonResponse(data)
        except Analysis.DoesNotExist:
            return JsonResponse({'error': 'Анализ с указанным ID не найден'})  # Обработка случая, если анализ не найден
    else:
        return JsonResponse({'error': 'Некорректный метод запроса'})  # Обработка случая, если запрос не GET


def get_values_for_stat(request):
    if request.method == "GET":
        print('dsfjbgsdbhnjsdgbsdgfb')
        analysis_ids = request.GET.get("numbers")
        analysis_ids_list = analysis_ids.split() # Разбиваем строку на список числовых значений
        analysis_fields = AnalysisFields.objects.filter(analysis_id__in=analysis_ids_list)
        data = {}
        for analysis_field in analysis_fields:
            analysis_id = analysis_field.analysis_id

            for i in range(1, 31):
                field_name = "value_" + str(i)

                if analysis_id not in data:
                    data[analysis_id] = {}
                if field_name not in data[analysis_id]:
                    data[analysis_id][field_name] = []
                data[analysis_id][field_name].append(getattr(analysis_field, field_name))

                # print(data)
        #print('=================================' + data)
        return JsonResponse({"values": data})


def chart_data(request):
    # Получаем значения analysis_id из HTML-элемента
    ids_str = request.GET.get('ids_str')
    print('ids_str: ' + str(ids_str))
    ids_list = [int(x) for x in ids_str.split(',')]
    print(ids_list)
    # Получаем тип выбранного столбца из выпадающего списка
    column_select = request.GET.get('column_select')
    print(column_select)
    print('column_select: ' + str(column_select))

    # Извлекаем значения выбранного столбца для указанных analysis_id
    result_set = AnalysisFields.objects.filter(
        analysis_id__in=ids_list).values_list(
        'analysis_id', column_select)

    # Возвращаем результаты в JSON-формате
    data = []
    for row in result_set:
        data.append({'analysis_id': row[0], 'value': row[1] or 0})
    print(data)
    return JsonResponse(data, safe=False)


@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def add_analysis_page(request):
    #Analysis.objects.create()

    analysis_info_form = NewAnalysis
    analysis_fields_form = NewAnalysisFields
    # get_id = request.user.id
    # Analysis.objects.create(user_id=get_id)
    if request.method == 'POST':
        analysis_info_form = NewAnalysis(request.POST)
        analysis_fields_form = NewAnalysisFields(request.POST)

        if analysis_info_form.is_valid() and analysis_fields_form.is_valid():
            # analysis_info = analysis_info_form.save()  # Сохраняем analysis_info_form и получаем объект
            # Analysis.objects.update(user_id=request.user.id)
            # analysis_fields_form.save()
            # get_analysis_id = analysis_info.analysis_id
            # AnalysisFields.objects.update(analysis_id=get_analysis_id)  # Передаем analysis_id в update()

            analysis_info = analysis_info_form.save(
                commit=False)  # Устанавливаем commit=False, чтобы отложить сохранение
            analysis_info.user_id = request.user.id  # Устанавливаем значение user_id
            analysis_info.save()  # Сохраняем analysis_info_form и получаем объект

            analysis_fields = analysis_fields_form.save(
                commit=False)  # Устанавливаем commit=False, чтобы отложить сохранение
            analysis_fields.analysis_id = analysis_info.analysis_id  # Устанавливаем значение analysis_id
            analysis_fields.analysis_type = analysis_info.analysis_type  # Устанавливаем значение analysis_id
            analysis_fields.save()  # Сохраняем analysis_fields_form

            #Analysis.objects.update(analysis_status='In process')
            #Analysis.objects.update(analysis_id=10000+int(get_id))
            messages.success(request, 'Показатели анализа успешно введены.')
        else:
            messages.error(request, 'Please correct the error below.')
    #else:
    #    form = NewAnalysis(request.POST)
    context = {'analysis_info_form': analysis_info_form, 'analysis_fields_form': analysis_fields_form}
    return render(request, 'rda_frontend/add-analysis.html', context)


@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def statistics_page(request):
    return render(request, 'rda_frontend/statistics-page.html')


def analysis_details(request, analysis_id):
    # Получаем объект анализа из базы данных
    analysis = get_object_or_404(Analysis, analysis_id=analysis_id)

    # Передаем объект анализа в контекст шаблона
    context = {'analysis': analysis}

    # Возвращаем рендеринг шаблона с передачей контекста
    return render(request, 'rda_frontend/analysis.html', context)


@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def neural_page(request):
    return render(request, 'rda_frontend/neural.html')


class AnalysisDetail(generics.ListCreateAPIView):
    queryset = Analysis.objects.all()
    serializer_class = serializers.AnalysisSerializer

class AnalysisUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analysis.objects.all()
    serializer_class = serializers.AnalysisSerializer


class PatientDetail(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer

class PatientUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer

# def add_analysis_values(request):
#     value_form = NewAnalysisFields
#
#     if request.method == 'POST':
#         value_form = NewAnalysisFields(request.POST)
#
#         if value_form.is_valid():
#             value_form.save()
#             return redirect('../add-analysis')
#         else:
#             messages.error(request, 'Please correct the error below.')
#
#     context = {'form': value_form}
#     return render(request, 'rda_frontend/add-analysis.html', context)


# def analysis_button(request):
#     form = NewAnalysisButton
#
#     if request.method == 'POST':
#         form = NewAnalysisButton(request.POST)
#
#         if form.is_valid():
#             form.save()
#         else:
#         messages.error(request, 'Please correct the error below.')
#
#     context = {'form': value_form}
#     return render(request, 'rda_frontend/add-analysis.html', context)
