from django.urls import include, path
import api.views as api_views

comment = [
    path('comment/create/', api_views.CommentCreate.as_view()),
    path('comment/get/', api_views.CommentList.as_view()),

]

mark = [
    path('marks/get/', api_views.MarkList.as_view()),
    path('marks/self_mark/', api_views.StudentMarkList.as_view()),
    path('marks/create/', api_views.CreateMark.as_view()),
    path('marks/<pk>/', api_views.MarkRUD.as_view()),
    path('marks/<mark_id>/', include(comment))

]

homework_solution = [
    path('solutions/get/', api_views.HomeworkSolutionList.as_view()),
    path('solutions/self_solutions/', api_views.HomeworkStudentSolutionList.
         as_view()),
    path('solutions/create/',
         api_views.HomeworkSolutionCreate.as_view()),
    path('solutions/<pk>/', api_views.HomeworkSolutionRUD.as_view()),
    path('solutions/<solution_id>/', include(mark))
]

homework = [
    path('homework/get/', api_views.HomeworkList.as_view()),
    path('homework/create/', api_views.HomeworkCreate.as_view()),
    path('homework/<pk>/', api_views.HomeworkRUD.as_view()),
    path('homework/<homework_id>/', include(homework_solution))
]
lectures = [
    path('lectures/get/', api_views.LectureList.as_view()),
    path('lectures/create/', api_views.LectureCreate.as_view()),
    path('lectures/<pk>/', api_views.LectureRUD.as_view()),
    path('lectures/<lecture_id>/', include(homework))
    ]

courses = [
    path('courses/Teacher/', api_views.TeacherCourseList.as_view(),
         name='TeacherCourseList'),
    path('courses/Student/', api_views.StudentCourseList.as_view()),
    path('courses/create/', api_views.CourseCreate.as_view(),
         name='CreateCourse'),
    path('courses/<pk>/', api_views.CourseRUD.as_view()),
    path('courses/<course_id>/', include(lectures)),
]

user_activation = [
    path('activate/<str:uid>/<str:token>/',
         api_views.UserActivationView.as_view())]

user = [path('', include('djoser.urls'))]

users = [path('users/<str:username>/', api_views.UsersList.as_view())]

jwt = [path('', include('djoser.urls.jwt'))]

urlpatterns = [
    path('', include(courses)),
    path('filtering_user/', include(users)),
    path('', include(jwt)),
    path('', include(user)),
    path('', include(user_activation))]
