from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Contact, SpamNumber
from .serializers import UserSerializer, ContactSerializer, SpamNumberSerializer

# User Registration
@api_view(['POST'])
def user_registration(request):
    name = request.data.get('name')
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    if User.objects.filter(username=phone_number).exists():
        return Response({"error": "Phone number already registered"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=phone_number, password=password)
    user.name = name
    user.save()

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

# User Login
@api_view(['POST'])
def user_login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    user = User.objects.filter(username=phone_number).first()

    if user and user.check_password(password):
        return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Contacts
@api_view(['GET', 'POST'])
def manage_contacts(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Marking Spam Numbers
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def mark_spam(request):

    number = request.data.get('mark_spam_number')
    marked_by = request.data.get('user_number')
    # reported_by = request.user  # Assuming user is authenticated
    # print(request.user)
    try:
        contact_data = Contact.objects.filter(contact_number = marked_by)
        if contact_data:
           spam_number, created =  SpamNumber.objects.get_or_create(number = number, reported_by = contact_data[0])
        # spam_number, created = SpamNumber.objects.get_or_create(number=number, reported_by = reported_by)
        # spam_number.reported_by.add(reported_by)
        return Response({"message": "Number marked as spam"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Searching
@api_view(['GET'])
def search(request):
    query = request.query_params.get('query')
    user = request.user  # Assuming user is authenticated

    # Perform search logic based on the query parameter
    # Logic to search by name or phone number

    # For example:
    matching_contacts = Contact.objects.filter(contact_name__icontains=query) | Contact.objects.filter(contact_number=query)
    serializer = ContactSerializer(matching_contacts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
