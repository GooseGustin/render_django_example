from django.urls import path 
from .views import (
    blogListView,
    blogCreateView, 
    blogDeleteView, 
    blogDetailsView, 
    blogUpdateView, 
    commentCreateView, 
    blogCategoriesView, 
)

app_name = 'core' 
urlpatterns = [
    path('', blogListView, name='home'),
    path('create', blogCreateView, name='create'), 
    path('<int:id>/delete', blogDeleteView, name='delete'), 
    path('<int:id>/', blogDetailsView, name='detail'), 
    path('<int:id>/update', blogUpdateView, name='update'),
    path('<int:id>/comment-create', commentCreateView, name='create-comment'), 
    path('categories', blogCategoriesView, name='categories'),
]