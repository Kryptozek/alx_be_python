#Ask the user for the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")
#Weather recommendation based
#If weather is sunny
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
#if weather  is rainy
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
#If weather is cold
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
#if response is different from expected
else:
    print("Sorry, I don't have recommendations for this weather.")