from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('<search>', SearchList.as_view(), name='search'),
    path('news/<add>', NewsCreate.as_view(), name='add'),
    path('<int:pk>/edit', NewsUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='delete'),

]
