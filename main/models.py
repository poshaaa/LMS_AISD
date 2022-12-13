from django.db import models

#Преподаватель
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    teacher_profile_img = models.ImageField(blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['id']
    def __str__(self):
        return self.full_name
#Категория курсов
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория курсов'
        verbose_name_plural = 'Категории курсов'
        ordering = ['id']
    def __str__(self):
        return self.title

#Курсы
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    descriprion = models.TextField()
    cousre_img = models.ImageField(blank=True, upload_to='course_imgs/', null=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['id']
    def __str__(self):
        return self.title

#Студент
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    teacher_profile_img = models.ImageField(blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    necessary_categories = models.TextField()

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['id']

    def __str__(self):
        return self.title