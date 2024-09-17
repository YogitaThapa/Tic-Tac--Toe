import tkinter as tk
import requests

def convert_currency():
    try:
        amount = float(entry_amount.get())
        base_currency = base_currency_var.get()
        target_currency = target_currency_var.get()
        
        # Fetch exchange rates from the API
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        data = response.json()
        
        # Check if the response is valid
        if 'rates' in data:
            conversion_rate = data['rates'][target_currency]
            converted_amount = amount * conversion_rate
            
            # Display the result
            result_label.config(text=f"{converted_amount:.2f} {target_currency}")
        else:
            result_label.config(text="Error fetching data.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Amount input
label_amount = tk.Label(window, text="Amount:")
label_amount.pack(pady=5)
entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

# Base currency dropdown
label_base_currency = tk.Label(window, text="Base Currency:")
label_base_currency.pack(pady=5)
base_currency_var = tk.StringVar(window)
base_currency_var.set("USD")  # Default value
base_currency_dropdown = tk.OptionMenu(window, base_currency_var, "USD", "EUR", "GBP", "INR")
base_currency_dropdown.pack(pady=5)

# Target currency dropdown
label_target_currency = tk.Label(window, text="Target Currency:")
label_target_currency.pack(pady=5)
target_currency_var = tk.StringVar(window)
target_currency_var.set("EUR")  # Default value
target_currency_dropdown = tk.OptionMenu(window, target_currency_var, "USD", "EUR", "GBP", "INR")
target_currency_dropdown.pack(pady=5)

# Convert button
button_convert = tk.Button(window, text="Convert", command=convert_currency)
button_convert.pack(pady=10)

# Result display
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the application
window.mainloop()