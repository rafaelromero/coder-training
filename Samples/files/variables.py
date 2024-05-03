def main():
   message = "hello world"
   start = 0
   end = 5

   if start < end:
       print(message[start:end])

   if  1 == 1:
       print("1 is equal to 1")

   if 1 < 0:
         print("1 is less than 0")
   
   current_loop = 0
   max_loop = 11

   while current_loop < max_loop:
        print("Current loop is: " + str(current_loop))
        current_loop += 1
   print("\n")
   
   list = ["apple", "banana", "cherry"]

   print(list[0])

   print("\n")

   #for item in list:
   #    print(item)

if __name__ == "__main__":  
    main()



