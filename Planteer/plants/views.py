from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from django.http import HttpRequest, HttpResponse
from Planteer.forms import PlantForm


# Create your views here.
def home_view(request:HttpRequest):
    return render(request, 'plants/home.html')

def plant_list_view(request):
    plants = Plant.objects.all()
    return render(request, 'plants/plant_list.html', {'plants': plants})

def plant_detail_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.all()
    return render(request, 'plants/plant_detail.html', {'plant': plant, 'related_plants': related_plants})

def add_plant_view(request):
    plant_form = PlantForm()
    if request.method == 'POST':
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:plant_list_view')
        else:
            print("not valid form")
    return render(request, 'plants/add_plant.html', {'plant_form': plant_form})


def update_plant_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_detail_view', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    
    return render(request, 'plants/update_plant.html', {'plant': plant, 'plant_form': form})


def delete_plant_view(request, plant_id):
    
    plant = get_object_or_404(Plant, id=plant_id)
   
    plant.delete()
   
    return redirect('plants:plant_list_view')



def search_plants_view(request):
    plants = Plant.objects.all()  

    
    query = request.GET.get("search", "")
    category = request.GET.get("category", "")
    is_edible = request.GET.get("is_edible", "")

   
    if query and len(query) >= 3:
        # Filter the plants by name
        plants = plants.filter(name__icontains=query)


    if category:
        plants = plants.filter(category=category)

    
    if is_edible:
        plants = plants.filter(is_edible=(is_edible == 'true'))

    return render(request, 'plants/search_plants.html', {"plants": plants, "query": query, "category": category, "is_edible": is_edible})


