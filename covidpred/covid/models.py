from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from encrypted_model_fields.fields import EncryptedIntegerField,EncryptedTextField,EncryptedDateTimeField,EncryptedBigIntegerField

class Coviddata(models.Model):
    full_name= EncryptedTextField(default='Anonymous')
    age= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    gender= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    fever= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    cough= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    fatigue= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    pains= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    nasal_congestion= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    shortness_of_breath= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    runny_nose= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    sore_throat= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    diarrhea= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    chills= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    headache= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    vomiting= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    lives_in_affected_area= EncryptedIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    result= EncryptedBigIntegerField()
    created_at = EncryptedDateTimeField(auto_now_add=True)

