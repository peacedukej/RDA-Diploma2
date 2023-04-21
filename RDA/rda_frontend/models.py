from django.db import models
from django.contrib.auth.models import User
import psycopg2

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    patronymic = models.CharField(max_length=30, null=True)
    passport = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(null=True, max_length=10)
    address = models.CharField(max_length=50, null=True)
    access_group = models.CharField(max_length=30, null=True, default='New')
    photo = models.URLField(null=True)
    # password = models.CharField(max_length=30, null=True)
    # class Meta:
    #     constraints = [models.PrimaryKeyConstraint(fields=['user_id'])]


# class UserInfo(models.Model):
#     user_id = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True
#     )


class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    patronymic = models.CharField(max_length=30, null=True)
    birthday = models.DateTimeField(null=True)
    job = models.CharField(max_length=30, null=True)
    start_of_experience = models.DateTimeField(max_length=20, null=True)

    # class Meta:
    #     constraints = [models.PrimaryKeyConstraint(fields=['doctor_id'])]


class UserDoctor(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    doctor_id = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user_id', 'doctor_id')
    # user_id = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )
    # doctor_id = models.OneToOneField(
    #     Doctor,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )
    #  class Meta:
    #      unique_together = ('user_id', 'doctor_id')


class Disease(models.Model):
    disease_id = models.IntegerField()
    # disease_id = models.IntegerField(primary_key=True)
    category = models.CharField(null=True, max_length=50)
    disease_name = models.CharField(max_length=20, null=True)
    ICD = models.CharField(max_length=20, null=True)

    # class Meta:
    #     constraints = [models.PrimaryKeyConstraint(fields=['disease_id'])]


class UserDisease(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    disease_id = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user_id', 'disease_id')
    # user_id = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )
    # disease_id = models.OneToOneField(
    #     Disease,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )

    # class Meta:
    #     constraints = [
    #         models.PrimaryKeyConstraint(fields=['user_id', 'disease_id']),
    #         models.ForeignKeyConstraint(
    #             ['user_id'], ['user.user_id'], on_delete=models.CASCADE
    #         ),
    #         models.ForeignKeyConstraint(
    #             ['disease_id'], ['disease.disease_id'], on_delete=models.CASCADE
    #         ),
    #     ]


class Files(models.Model):
    file_id = models.IntegerField()
    # file_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=100, null=True)
    date_of_upload_file = models.DateTimeField(null=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # user_id = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )
    file_user_name = models.CharField(max_length=20, null=True)

    class Meta:
        unique_together = ('user_id', 'file_id')

    # class Meta:
    #     constraints = [
    #         models.PrimaryKeyConstraint(fields=['file_id', 'user_id']),
    #         models.ForeignKeyConstraint(
    #             ['user_id'], ['user.user_id'], on_delete=models.CASCADE
    #         ),
    #     ]


class Analysis(models.Model):

    #user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    user_id = models.IntegerField(default=0)
    analysis_id = models.AutoField(primary_key=True) # при нажатии кнопки создавать новый анализ айди /// пока что тут автоинкремент поля
    # analysis_id = models.IntegerField(primary_key=True)
    analysis_type = models.CharField(max_length=50, null=True)
    date_of_upload_analysis = models.DateTimeField(null=True)
    place_of_analysis = models.CharField(max_length=50, null=True)
    analysis_user_name = models.CharField(max_length=50, null=True)
    date_of_analysis = models.DateTimeField(null=True)
    analysis_status = models.CharField(default='Created', max_length=20)


class AnalysisFields(models.Model):
    #analysis_id = models.OneToOneField(Analysis, on_delete=models.CASCADE, primary_key=True)

    analysis_id = models.IntegerField(primary_key=True, verbose_name='ID Анализа')
    analysis_type = models.CharField(max_length=50, null=True, verbose_name='Тип анализа')
    value_1 = models.CharField(max_length=15, null=True, verbose_name='Показатель 1', default='Null')
    value_2 = models.CharField(max_length=15, null=True, verbose_name='Показатель 2', default='Null')
    value_3 = models.CharField(max_length=15, null=True, default='Null')
    value_4 = models.CharField(max_length=15, null=True, default='Null')
    value_5 = models.CharField(max_length=15, null=True, default='Null')
    value_6 = models.CharField(max_length=15, null=True, default='Null')
    value_7 = models.CharField(max_length=15, null=True, default='Null')
    value_8 = models.CharField(max_length=15, null=True, default='Null')
    value_9 = models.CharField(max_length=15, null=True, default='Null')
    value_10 = models.CharField(max_length=15, null=True, default='Null')
    value_11 = models.CharField(max_length=15, null=True, default='Null')
    value_12 = models.CharField(max_length=15, null=True, default='Null')
    value_13 = models.CharField(max_length=15, null=True, default='Null')
    value_14 = models.CharField(max_length=15, null=True, default='Null')
    value_15 = models.CharField(max_length=15, null=True, default='Null')
    value_16 = models.CharField(max_length=15, null=True, default='Null')
    value_17 = models.CharField(max_length=15, null=True, default='Null')
    value_18 = models.CharField(max_length=15, null=True, default='Null')
    value_19 = models.CharField(max_length=15, null=True, default='Null')
    value_20 = models.CharField(max_length=15, null=True, default='Null')
    value_21 = models.CharField(max_length=15, null=True, default='Null')
    value_22 = models.CharField(max_length=15, null=True, default='Null')
    value_23 = models.CharField(max_length=15, null=True, default='Null')
    value_24 = models.CharField(max_length=15, null=True, default='Null')
    value_25 = models.CharField(max_length=15, null=True, default='Null')
    value_26 = models.CharField(max_length=15, null=True, default='Null')
    value_27 = models.CharField(max_length=15, null=True, default='Null')
    value_28 = models.CharField(max_length=15, null=True, default='Null')
    value_29 = models.CharField(max_length=15, null=True, default='Null')
    value_30 = models.CharField(max_length=15, null=True, default='Null')

    #
    # class Meta:
    #     unique_together = ('id', 'analysis_id')
    # class Meta:
    #     constraints = [
    #         models.PrimaryKeyConstraint(fields=['analysis_id', 'user_id']),
    #         models.ForeignKeyConstraint(
    #             ['user_id'], ['user.user_id'], on_delete=models.CASCADE
    #         ),
    #     ]


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance, email=instance.email)


    # @receiver(post_save, sender=Analysis)
    # def update_analysis_fields(sender, instance, created, **kwargs):
    #     if created:
    #         AnalysisFields.objects.create(analysis_id=instance.analysis_id, analysis_type=instance.analysis_type)
        # print(str(Patient.email))
        # print(User.objects.get('email'))
        # email = User.objects.get('email')
        # p = Patient(email=email)
        # # p.save()

