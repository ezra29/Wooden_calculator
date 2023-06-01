from django.shortcuts import render  # Importing render function from django.shortcuts module


# Define a view for the 'wood' page
def wood(request):
    if request.method == 'POST':
        # Debug print statement
        print(request.POST)
        
        # Get the value of the 'zijde' key from the POST data
        zijde = request.POST.get('zijde')

        if zijde == 'rechthoekig':
            # If the value of 'zijde' is 'rechthoekig', get the values of other keys from the POST data
            wood_type = request.POST.get('wood_type')
            length_mm = float(request.POST.get('Lengte'))
            width_mm = float(request.POST.get('Breedte'))

            # Set prices for different types of wood
            berken_price = 9.50
            grenen_price = 8.50
            hardhout_price = 11.50

            # Set initial price to 0.0
            wood_price = 0.0

            # Determine the price based on the type of wood selected
            if wood_type == 'Berken':
                wood_price = berken_price
            elif wood_type == 'Grenen':
                wood_price = grenen_price
            elif wood_type == 'Hardhout':
                wood_price = hardhout_price

            # Convert length and width from millimeters to meters
            length_m = (length_mm / 1000)
            width_m = (width_mm / 1000)

            # Calculate area in square meters
            m2 = (length_m * width_m)

            # Calculate total price and round it to 3 decimal places
            total_price = round((m2 * wood_price), 3)

            # Render the 'wood_cal.html' template with context variables
            return render(request, 'wood_cal.html', {'total_price': total_price,
                                                     'wood_type': wood_type,
                                                     'berken_price': berken_price,
                                                     'grenen_price': grenen_price,
                                                     'hardhout_price': hardhout_price,
                                                     'm2': m2})
        elif zijde == "rond":
            # If the value of 'zijde' is 'rond', get the values of other keys from the POST data
            wood_type = request.POST.get('wood_type')
            diameter_mm = float(request.POST.get('diameter'))

            # Set prices for different types of wood
            berken_price = 9.50
            grenen_price = 8.50
            hardhout_price = 11.50

            # Set initial price to 0.0
            wood_price = 0.0

            # Determine the price based on the type of wood selected
            if wood_type == 'Berken':
                wood_price = berken_price
            elif wood_type == 'Grenen':
                wood_price = grenen_price
            elif wood_type == 'Hardhout':
                wood_price = hardhout_price

            # Calculate radius in meters
            radius_m = (diameter_mm / 2) / 1000

            # Calculate area in square meters
            m2 = (3.14 * radius_m * radius_m)

            # Calculate total price and round it to 3 decimal places
            total_price = round((m2 * wood_price), 3)

            # Render the 'wood_cal.html' template with context variables
            return render(request, 'wood_cal.html', {'total_price': total_price,
                                                     'wood_type': wood_type,
                                                     'berken_price': berken_price,
                                                     'grenen_price': grenen_price,
                                                     'hardhout_price': hardhout_price,
                                                     'm2': m2})
        else: # Return If No Hoek Options is not Selected
            return render(request, 'wood.html', {'zijde':zijde})
    else: #return if If No Post Data At All Option Is Selected
        return render(request, 'wood.html')
def test(request): # Test Function in Django...
    contex = {}
    return render(request, 'test.html',{'contex': contex})


