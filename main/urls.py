from django.urls import path
from . import views

urlpatterns = [
#Преподаватели
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login',views.teacher_login),
#Категории
    path('category/',views.CategoryList.as_view()),
    path('course/',views.CourseList.as_view()),
    path('teacher-courses/<int:teacher_id>/',views.TeacherCourseList.as_view()),
]