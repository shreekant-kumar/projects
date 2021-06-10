from tkinter import *
import json
import requests
root=Tk()
root.title("Weather application")
root.geometry("500x100")
def Ziplookup():
    #zip.get()
    #ziplabel=Label(root,text=zip.get())
    #ziplabel.grid(row=1,column=0,columnspan=2)
    #FCE95230-AF7B-44A7-80FA-B235E5635096 
    #https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=FCE95230-AF7B-44A7-80FA-B235E5635096
    try:
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=FCE95230-AF7B-44A7-80FA-B235E5635096")
        api=json.loads(api_request.content)
        city=api[0]["ReportingArea"]
        quality=api[0]["AQI"]
        category=api[0]["Category"]["Name"]
        if category=="Good":
            weather_color="#0C0"
        elif category=="Moderate":
            weather_color="#FFFF00"
        elif category=="Unhealthy for Sensitive Groups ":
            weather_color="#ff9900"
        elif category=="Unhealthy":
            weather_color="#FF0000"
        elif category=="Very Unhealthy":
            weather_color="#990066"
        elif category=="Hazardous":
            weather_color="#660000"
        root.configure(background=weather_color)
        mylabel=Label(root,text=city + " Air Quality " + str(quality) + " " + category,font=("Helvetica",15),background=weather_color)
        mylabel.grid(row=1,column=0,columnspan=3)
        
    except Exception as e:
            api="Error..."
zip=Entry(root)
zip.grid(row=0,column=0)
zipbutton=Button(root,text="Enter Zipcode",command=Ziplookup)
zipbutton.grid(row=0,column=1)
root.mainloop()
