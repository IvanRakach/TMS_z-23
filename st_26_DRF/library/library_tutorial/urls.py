from django.urls import path
# from .views import authors_list_create_view
from .views import AuthorListView, AuthorDetailsView

# urlpatterns = {
#     path("authors", authors_list_create_view)
# }

urlpatterns = {
    path("authors/", AuthorListView.as_view()),
    path("authors/<int:pk>/", AuthorDetailsView.as_view())
}