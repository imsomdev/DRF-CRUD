from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions as rest_exceptions
from django.shortcuts import get_object_or_404

# Custom Imports
from .models import Student
from .serializers import StudentSerializer

# Logging
import logging
from .log_config import setup_logging
setup_logging()


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def get_stu(request):
    stud_obj = Student.objects.all()
    if request.method == 'GET':
        serializer = StudentSerializer(stud_obj, many=True)
        logging.getLogger("INFO").info("Request to fetch Student Data")
        return Response({'msg': 'Student data fetched', 'data': serializer.data}, status=status.HTTP_200_OK)

    logging.getLogger("WARNING").warning("Invalid Request Method at get_stu")
    return Response({'msg': 'Invalid Request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_stu(request):
    if request.method != 'POST':
        return Response({'msg': 'Invalid Request method'}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():

        try:
            serializer.save()
            st_id = serializer.data.get('id')
            logging.getLogger("INFO").info(
                f"Succefully created Student ID: {st_id}")
            return Response({'msg': 'Succefully created Student'}, status=status.HTTP_201_CREATED)
        except rest_exceptions.ValidationError:
            return Response({'msg': 'Please check given inputs'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'msg': 'Please check given inputs'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_stu(request, stu_uid):

    try:
        stu_obj = get_object_or_404(Student, stu_uid=stu_uid)
    except Student.DoesNotExist:
        return Response({'msg': 'Given Id Does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method != 'PUT':
        return Response({'msg': 'Invalid Request method'}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data
    serializer = StudentSerializer(stu_obj, data=data)
    if serializer.is_valid():

        try:
            serializer.save()
            st_id = serializer.data.get('id')
            logging.getLogger("INFO").info(
                f"Succefully Updated Student ID: {st_id}")
            return Response({'msg': 'Succefully updated Student'}, status=status.HTTP_201_CREATED)
        except rest_exceptions.ValidationError:
            return Response({'msg': 'Please check given inputs'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'msg': 'Please check given inputs'}, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
def delete_stu(request, stu_uid):
    print(stu_uid)
    try:
        stu_obj = get_object_or_404(Student, stu_uid=stu_uid)
        st_id = stu_obj.id
    except Student.DoesNotExist:
        return Response({'msg': 'Given Id Does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method != 'DELETE':
        return Response({'msg': 'Invalid Request method'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        stu_obj.delete()
        logging.getLogger("INFO").info(
            f"Succefully Deleted Student ID: {st_id}")
        return Response({'msg': 'Succefully deleted Student'}, status=status.HTTP_200_OK)
    except rest_exceptions.NotFound:
        pass
