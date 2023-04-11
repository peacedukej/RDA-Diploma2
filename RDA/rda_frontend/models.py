from django.db import models
from django.contrib.auth.models import User
import psycopg2

# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    patronymic = models.CharField(max_length=30, null=True)
    passport = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(null=True, max_length=10)
    address = models.CharField(max_length=50, null=True)
    #password = models.CharField(max_length=30, null=True)
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
    analysis_id = models.IntegerField()
    # analysis_id = models.IntegerField(primary_key=True)
    analysis_type = models.CharField(max_length=50, null=True)
    date_of_upload_analysis = models.DateTimeField(null=True)
    place_of_analysis = models.CharField(max_length=50, null=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # user_id = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    analysis_user_name = models.CharField(max_length=50, null=True)
    date_of_analysis = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('user_id', 'analysis_id')
    # class Meta:
    #     constraints = [
    #         models.PrimaryKeyConstraint(fields=['analysis_id', 'user_id']),
    #         models.ForeignKeyConstraint(
    #             ['user_id'], ['user.user_id'], on_delete=models.CASCADE
    #         ),
    #     ]











