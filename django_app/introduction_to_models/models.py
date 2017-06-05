from django.db import models


# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('students', '학생'),
        ('teacher', '선생'),
    )
    person_type = models.CharField(
        '유형',
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0]
    )
    teacher = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name


# INSTALLED_APPS에 이 모델이 속하는 app추가
# makemigrations로 migrations생성
# migrate로 migration을 적용
# admin.py에 Person클래스 등록
# createsuperuser로 슈퍼유저 계정 생성
# runserver후 admin접속해서 Person객체 생성 및 저장해보기

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
