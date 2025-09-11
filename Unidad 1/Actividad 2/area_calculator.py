import math

def main():
    print("Area Calculator")
    print("1. Triangle")
    print("2. Square") 
    print("3. Circle")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = (base * height) / 2
        print(f"Triangle area: {area}")
    elif choice == "2":
        side = float(input("Enter side length: "))
        area = side * side
        print(f"Square area: {area}")
    elif choice == "3":
        radius = float(input("Enter radius: "))
        area = math.pi * radius * radius
        print(f"Circle area: {area}")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()