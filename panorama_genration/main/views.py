from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import cv2
# Create your views here.


def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = HotelForm()
	return render(request, 'uploadImage.html', {'form': form})


def success(request):
	return HttpResponse('successfully uploaded')

def display_hotel_images(request):
 
    if request.method == 'GET':
 
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        for i in Hotels:
            imgLocation = i.hotel_Main_Img.url
            path = imgLocation[1:]
            print(path)
            img = cv2.imread(path)
            img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"{path}" , img)
        return render(request, 'showimage.html',{'hotel_images': Hotels})