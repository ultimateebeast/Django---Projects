# checker/views.py
from django.shortcuts import render

def check_number(request):
    result = None
    number_input = ''

    if request.method == 'POST':
        number_input = request.POST.get('number', '')
        try:
            # Try to convert the input to an integer
            number = int(number_input)
            
            # Check if the number is even or odd
            if number % 2 == 0:
                result = f"The number {number} is Even."
            else:
                result = f"The number {number} is Odd."
        
        except ValueError:
            # Handle cases where the input is not a valid number
            if number_input: # If user typed something
                result = f"'{number_input}' is not a valid number. Please enter an integer."
            else: # If user submitted an empty form
                result = "Please enter a number."

    return render(request, 'checker/index.html', {'result': result, 'number_input': number_input})