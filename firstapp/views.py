from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note,Book,Students
from .serializers import Noteserializer,BookSerializer,StudentsSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


class NoteCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        queryset = Note.objects.all()
        serializer = Noteserializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Noteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, pk):

        note=get_object_or_404(Note,pk=pk)
        serializer=Noteserializer(note)
        return Response(serializer.data)
    def put(self, request, pk):
        note=get_object_or_404(Note,pk=pk)
        self.check_object_permissions(request,note)
        serializer=Noteserializer(note,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note=get_object_or_404(Note,pk=pk)
        self.check_object_permissions(request.note)
        note.delete()
        return Response(status=204)


# class BookLIstAPIView(APIView):

#     def get(self, request):
#         book=Book.objects.all()
#         serializer=BookSerializer(book, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer=BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class BookDetailAPIView(APIView):

#     def get(self, request, pk):
#         book=get_object_or_404(Book, pk=pk)
#         serializer=BookSerializer(book)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         book=get_object_or_404(Book, pk=pk)
#         serializer=BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         book=get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=204)


class BookCreate(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class Bookupdate(RetrieveUpdateDestroyAPIView):
     queryset=Book.objects.all()
     serializer_class=BookSerializer

class StudentsCreate(APIView):
    def get(self, request):
        student=Students.objects.all()
        serializer=StudentsSerializer(student,many=true)
        return Response(serializer.data)
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serailizer.data)
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
class StudentsUpdate(APIView):
    def get(self, request, pk):
        student=get_object_or_404(Students,pk=pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student=get_object_or_404(Student, pk=pk)
        serializer=StudentSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        student=get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=204)

from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    




# def put(self, request, pk):
#     note=get_object_or_404(Note,pk=pk)
#     self.check_object_permissions(request,note)
#     serializer=NoteSerializer(note,data=request.data)
#     if serializer.is_valid():
#         serilizer.save()
#         return Response(serializer.data)
#     return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

#  def delete(self,request,pk):
#     note=get_object_or_404(Note,pk=pk)
#     self.check_object_permissions(request,note)
#     note.delete()
#     return Response(status=204)