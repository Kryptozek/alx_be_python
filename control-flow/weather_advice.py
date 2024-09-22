#Ask the user for the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")
#Weather recommendation based
if (weather == "sunny"):#If weather is sunny
    print("Wear a t-shirt and sunglasses.")
elif(weather == "rainy"):#if weather  is rainy
    print("Don't forget your umbrella and a raincoat.")
elif(weather == "cold"):#If weather is cold
    print("Make sure to wear a warm coat and a scarf.")
else:#if response is different from expected
    print("Sorry, I don't have recommendations for this weather.")