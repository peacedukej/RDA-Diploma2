from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from .forms import RegisterForm, LoginForm, NewUserProfile, EditPassword, NewAnalysis, NewAnalysisFields#, NewAnalysisButton
from .models import Patient, Analysis, AnalysisFields

from django.http import JsonResponse


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

            # Создание словаря с данными анализа
            data = {
                'analysis_type': analysis.analysis_type,
                'value_1': analysis.value_1,
                'value_2': analysis.value_2,
                'value_3': analysis.value_3,
                'value_4': analysis.value_4,
                'value_5': analysis.value_5,
                'value_6': analysis.value_6,
                'value_7': analysis.value_7,
                'value_8': analysis.value_8,
                'value_9': analysis.value_9,
                'value_10': analysis.value_10
            }

            # Удаление пустых значений из словаря
            data = {key: value for key, value in data.items() if value is not None}

            return JsonResponse(data)  # Возвращение данных в JSON-формате
        except AnalysisFields.DoesNotExist:
            return JsonResponse({'error': 'Анализ с указанным ID не найден'})  # Обработка случая, если анализ не найден
    else:
        return JsonResponse({'error': 'Некорректный метод запроса'})  # Обработка случая, если запрос не GET


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
