from .models import Contact, Person
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import LoginSerializer, ContactSerializer, PersonSerializer, UserSerializer 
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        UserReg = UserSerializer(data= request.data)
        if UserReg.is_valid(raise_exception=True):
             cd = UserReg.data
             register = User.objects.create(
                 username = cd.get("username"),
                 first_name = cd.get("first_name"), 
                 last_name = cd.get("last_name")
             )
             register.set_password(cd.get("password"))
             register.save()
             return Response("registration Successful")
@api_view(['POST'])
def userLogin(request):
    if request.method == 'POST':
        user_login = LoginSerializer(data=request.data)
        if user_login.is_valid(raise_exception=True):
            cd = user_login.data
            user = authenticate(request, username=cd.get('user_name'),
                               password=cd.get('password')
                               )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return Response('Login Succesful')
                else:
                    return Response('Inactive Account')
            else:
               return Response('user doesnot exist')
        

@api_view(["POST"])
@login_required
#this function adds personal details of the contact
def AddContact(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            add_contact=PersonSerializer(data = request.data)
            if add_contact.is_valid():
                cd = add_contact.data
                create = Person.objects.create(
                    user=request.user, 
                    first_name = cd.get("first_name"), 
                    last_name = cd.get("last_name"), 
                    middle_name = cd.get("middle_name"),
                    Gender = cd.get("Gender")
                )
                picture = request.FILES.get("photo")
                if picture is not None:
                    create.photo = picture
                    create.save()
                else:
                    create.save()
                
                contact_details = Contact.objects.create(
                    contactee = create
                )
                return Response("Personal Detail Added")

#this function updates both the personal details and contact details
@api_view(["GET", "POST"])
def contactUpdate(request, id):
    try:
        person = Person.objects.get(id=id, user=request.user)
        contact_details = Contact.objects.all().filter(contactee = person)
        if request.method == "POST":
            person_update = PersonSerializer(person, data = request.data)
            contact_update = ContactSerializer(contact_details, data = request.data)
            if person_update.is_valid(raise_exception=True) and contact_update.is_valid():
                if request.FILES.get("photo") is not None:
                    person_update.photo = request.FILES.get('photo')
                    person_update.save()
                    contact_update.save()
                else:
                    person_update.save()
                    contact_update.save()
                return Response('update successful')
    except ObjectDoesNotExist:
        return Response('contact does not exist')

#allows you to view all your contacts
@api_view(['GET'])
def viewAllContacts(request):
    mycontacts = Person.objects.all(user = request.id)
    mycontactsdata = PersonSerializer(mycontacts, many=True).data
    return Response(mycontactsdata)

#allows you to view a particular contact
@api_view(['GET'])
def viewContact(request, id):
    try:
        contact = Person.objects.get(id=id, user = request.user)
        contact_details = Contact.objects.get(contactee =  contact)
        contact_data = PersonSerializer(contact)
        contact_details_data = ContactSerializer(contact_details)
        context = {
            'contact_data':contact_data, 
            'contact_details_data': contact_details_data
        }
        return Response(context)
    except ObjectDoesNotExist:
        return Response('contact does not exist')
    
#delete a contact
def deleteContact(request, id):
    try:
        contact = Person.objects.get(id=id, user=request.data)
        contact.delete()
        return Response('successfully deleted contact')
    except ObjectDoesNotExist:
        return Response('contact does not exist')













