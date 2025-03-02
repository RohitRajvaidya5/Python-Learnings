try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index : "))
    print(l[i])

except:
    print("Some error occurred")

# Finally is keyword which always executed no matter code under try is working or not.
finally:
    print("I am always executed")

