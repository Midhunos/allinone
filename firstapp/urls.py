from rest_framework.routers import DefaultRouter
from .views import NoteCreate, NoteDetailAPIView, BookViewSet
from django.urls import path

router = DefaultRouter()
router.register("books", BookViewSet, basename="books")

urlpatterns = [
    path("note/", NoteCreate.as_view(), name="note-get"),
    path("notes/<int:pk>/", NoteDetailAPIView.as_view(), name="single-one"),
]

urlpatterns += router.urls