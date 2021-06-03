from django.urls import include, path
import api.views as api_views

comment_methods = [
    path('comment/create/', api_views.CommentCreate.as_view()),
    path('comment/get/', api_views.CommentList.as_view()),

]

mark_methods = [
    path('marks/get/', api_views.MarkList.as_view()),
    path('marks/self_mark/', api_views.StudentMarkList.as_view()),
    path('marks/create/', api_views.CreateMark.as_view()),
    path('marks/<pk>/', api_views.MarkRUD.as_view()),
    path('marks/<mark_id>/', include(comment_methods))

]

homework_solution_methods = [
    path('solutions/get/', api_views.HomeworkSolutionList.as_view()),
    path('solutions/self_solutions/', api_views.HomeworkStudentSolutionList.
         as_view()),
    path('solutions/create/',
         api_views.HomeworkSolutionCreate.as_view()),
    path('solutions/<pk>/', api_views.HomeworkSolutionRUD.as_view()),
    path('solutions/<solution_id>/', include(mark_methods))
]

homework_methods = [
    path('homework/get/', api_views.HomeworkList.as_view()),
    path('homework/create/', api_views.HomeworkCreate.as_view()),
    path('homework/<pk>/', api_views.HomeworkRUD.as_view()),
    path('homework/<homework_id>/', include(homework_solution_methods))
]
lectures_methods = [
    path('lectures/get/', api_views.LectureList.as_view()),
    path('lectures/create/', api_views.LectureCreate.as_view()),
    path('lectures/<pk>/', api_views.LectureRUD.as_view()),
    path('lectures/<lecture_id>/', include(homework_methods))
    ]

urlpatterns = [
    path('courses/Teacher/', api_views.TeacherCourseList.as_view()),
    path('courses/Student/', api_views.StudentCourseList.as_view()),
    path('courses/create/', api_views.CourseCreate.as_view()),
    path('courses/<pk>/', api_views.CourseRUD.as_view()),
    path('courses/<course_id>/', include(lectures_methods))
    ]
