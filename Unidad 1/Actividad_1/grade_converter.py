def main():
    grade = float(input("Enter numeric grade: "))
    
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
    
    print(f"Letter grade: {letter}")

if __name__ == "__main__":
    main()