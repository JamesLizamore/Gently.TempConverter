def main():
    print("Please select one of the following:")
    print("1) Convert Celsius to Fahrenheit")
    print("2) Convert Fahrenheit to Celsius")
    convertMethod = input()
    if convertMethod == "1":
        convertToFahrenheit()
    elif convertMethod == "2":
        convertToCelsius()
    else:
        main()


def convertToFahrenheit():
    print("Please enter the degrees Celsius that you would like to convert to degree Fahrenheit:")
    degreesCelsius = float(input())
    degreesFahrenheit = degreesCelsius * (9/5) + 32
    print(f"{degreesFahrenheit} degrees Fahrenheit") 

def convertToCelsius():
    print("Please enter the degrees Fahrenheit you want to convert to degrees Celsius:")
    degreesFahrenheit = float(input())
    degreesCelsius = (degreesFahrenheit - 32) * (5/9)
    print(f"{degreesCelsius} degrees Celsius")

main()