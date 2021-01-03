# Yitzchok Kaplan - Assignment Project Task 2 Draft
# 1/2/2021
import requests #imports requests library

print("Welcome to Weather.find_with_zip") #display welcome message
def Main():#get zip from user function
  zipCode = input("\nPlease Enter The City's Zip Code: ")

  try:#try get a connection
     #get data from weather server
    link = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=3cfb3ef209130bbc71e87da6c0f41baf".format(zipCode)#the link from where data is retrieved
    request = requests.get(link)#request data
    
      
  except:#if error
    print("Sorry Connection Failed...\nPlease Try Again (Probably an issue with your internet connection)...")
    Main()#restart from Main()
  
  else:#passed try block
    print("Connection successfull...")#print connection successfull (is successfull if got to this point with no error)
    details = request.json()#get in json format
    show_data(details)#call display data function 
  
def AskRestart():#ask if user wants to search again
  ask = input("\nWould You Like To Search The Weather For Another Location? (Y/N): ")
  if ask == "Y":#if yes
    Main()
  elif ask == "N":#if no
   print("Thank You For Using Weather.find_with_zip, We Hope You Will Visit Us Again. Good Bye! ")
   return
  
  else:#invalid input
    print("Invalid Input Please Try Again...")
    AskRestart()#reask for input

def show_data(details):#digest data from server
    #extracting data into variables
    code = details["cod"]    
    #display weather
    if code == 200:#Found zipcode
      print("City found...")
      temp = details["main"]["temp"]
      hightemp = details["main"]["temp_max"]
      lowtemp = details["main"]["temp_min"]
      wind_speed = details["wind"]["speed"]
      press = details["main"]["pressure"]
      latitude = details["coord"]["lat"]
      longitude = details["coord"]["lon"]
      humid = details["main"]["humidity"]
      description = details["weather"][0]["description"]
      print("\nThe Current Temperature Is : {} Degree(s) Fahrenheit".format(temp))
      print("The High Temperature Is : {} Degree(s) Fahrenheit".format(hightemp))
      print("The Low Temperature Is : {} Degree(s) Fahrenheit".format(lowtemp))
      print("The Winds Speed Is : {} Meters A Second".format(wind_speed))
      print("The Pressure Is : {} hecto Pascals".format(press))
      print("The Latitude Is : {}".format(latitude))
      print("The Longitude Is : {}".format(longitude))
      print("The Humidity Is : {} Percent".format(humid))
      print("The Description Is : {}".format(description))
      AskRestart()#ask if user wants to go again
    elif code == "404": #if resource not found
      message = details["message"]
      if message == "city not found":#if invalid zip
        print("You entered an invalid ZIP code...")
        print("Please try again...")
        Main()
    else:
      print("A unknown error occurred, please try again...")
      AskRestart()

    
Main() #call main function
  