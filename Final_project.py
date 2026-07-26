import tkinter as tk
import requests 

API_KEY = "506978399b34ac4c7dc48975f7ec53ab"

window = tk.Tk()
window.title("Weather Forecast")
window.minsize(width=250, height=100)
window.rowconfigure([0, 10], minsize=100)
window.columnconfigure([0, 4], minsize=250)

def search():
    city = entry.get()
    if not city:
        label1.config(text=" Please enter a city ")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    if data.get("cod") != 200:
        label1.config(text="City not found")
        return
    else:
        label1.config(text="City is available")
  
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    precipitation = data.get("rain", {}).get("1h", 0)

    label2.config(text=f"Temperature: {temperature}°C")
    label3.config(text=f"Humidity: {humidity}%")
    label4.config(text=f"Wind Speed: {wind_speed} m/h")
    label5.config(text=f"Pressure: {pressure} hPa")
    label6.config(text=f"Precipitation: {precipitation}%")
    
   


label_entry = tk.Label(window, text="Location:", fg="black", font=("Arial", 16, "bold"), width=25 ,height=1)
label_entry.grid(row=0, column=1, sticky="e", padx=10, pady=10)

button = tk.Button(window, text="Search", command=search, relief="raised")
button.grid(row=0, column=3, padx=10, pady=10)

entry = tk.Entry(window,textvariable="location", relief="raised", border=2, font=("Arial", 16, "bold") )
entry.grid(row=0, column=2, padx=2, pady=2)

    

label1 = tk.Label(window, text=" ", fg="red", font=("Arial", 16, "bold"), width=25, height=1)

label2 = tk.Label(window, text="Temperature:", fg="black", font=("Arial", 16, "bold"),  width=10, height=1)

label3 = tk.Label(window, text="Humidity:", fg="black", font=("Arial", 16, "bold") , width=10, height=1 )

label4 = tk.Label(window, text="Wind Speed:", fg="black", font=("Arial", 16, "bold") , width=10, height=1)

label5 = tk.Label(window, text="Pressure:", fg="black", font=("Arial", 16, "bold") , width=10, height=1)

label6 = tk.Label(window, text="Precipitation:", fg="black", font=("Arial", 16, "bold") , width=10, height=1)

label1.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
label2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
label3.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
label4.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)
label5.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)
label6.grid(row=6, column=0, sticky="nsew", padx=10, pady=10)

window.mainloop()