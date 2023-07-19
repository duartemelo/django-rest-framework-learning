from .models import Bar, Drink
from .serializers import DrinkSerializer, BarSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):
  if request.method == 'GET':
    # get all the drinks
    # serialize them 
    # return JSON
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
  try:
    drink = Drink.objects.get(pk=id)
  except Drink.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = DrinkSerializer(drink)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = DrinkSerializer(drink, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    drink.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

@api_view(['GET', 'POST'])
def bars_list(request):
  if request.method == 'GET':
    bars = Bar.objects.all()
    serializer = BarSerializer(bars, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    pass
    # serializer = DrinkSerializer(data=request.data)
    # if serializer.is_valid():
    #   serializer.save()
    #   return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def bar_detail(request, id):
  try:
    bar = Bar.objects.get(pk=id)
    drinks = bar.drinks.all()
  except Bar.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    bar_serializer = BarSerializer(bar)
    drinks_serializer = DrinkSerializer(drinks, many=True)
    return Response({
      **bar_serializer.data,
      'drinks': drinks_serializer.data
    })
  elif request.method == 'PUT':
    pass
    # serializer = DrinkSerializer(drink, data=request.data)
    # if serializer.is_valid():
    #   serializer.save()
    #   return Response(serializer.data)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    pass
    # drink.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def bar_drinks_detail(request, id):
  try:
    bar = Bar.objects.get(pk=id)
    drinks = bar.drinks.all()
  except Bar.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    drinks_serializer = DrinkSerializer(drinks, many=True)
    return Response(drinks_serializer.data)
  elif request.method == 'POST':
    drinks_ids = request.data.get('drinks_ids', [])  # Get the list of drink IDs from the request body
    drinks_to_add = Drink.objects.filter(pk__in=drinks_ids)  # Get the Drink instances based on the IDs

    bar.drinks.add(*drinks_to_add)  # Associate the drinks with the bar

    drinks_serializer = DrinkSerializer(drinks_to_add, many=True)
    return Response(drinks_serializer.data, status=status.HTTP_201_CREATED)
  elif request.method == 'DELETE':
    drinks_ids = request.data.get('drinks_ids', [])  # Get the list of drink IDs from the request body
    drinks_to_remove = Drink.objects.filter(pk__in=drinks_ids)  # Get the Drink instances based on the IDs

    bar.drinks.remove(*drinks_to_remove) 

    drinks_serializer = DrinkSerializer(drinks_to_remove, many=True)
    return Response(drinks_serializer.data, status=status.HTTP_200_OK)