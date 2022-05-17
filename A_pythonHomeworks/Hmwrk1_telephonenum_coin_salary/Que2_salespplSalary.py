def SalespplSalary():

    salrange = [0,0,0,0,0,0,0,0,0]

    while 1==1:
        ival = input("Please enter sales in this week. Type -1 to quit. \n")

        if ival.isalpha():
            print("Input valid number to continue or any negative number to quit")
            continue

        salethisWeek = float(ival)
        if salethisWeek < 0:
            break

        salary = float(200 + salethisWeek * 0.09)
        int_salary = int(round(salary))
        print(str(int_salary))

        index= -1
        if 200 <=salary<= 299: index= 0
        elif 300<=salary <= 399: index= 1
        elif 400 <= salary <= 499: index = 2
        elif  500<=salary<= 599: index= 3
        elif 600 <= salary <= 699: index = 4
        elif 700 <= salary <= 799: index = 5
        elif 800 <= salary <= 899: index = 6
        elif 900 <= salary <= 999: index = 7
        elif 999 <= salary: index = 8


        print(str(index))
        salrange[index] = salrange[index] + 1

    print("Number of employees having salary 200 to 299 "+str(salrange[0]))
    print("Number of employees having salary 300 to 399 "+str(salrange[1]))
    print("Number of employees having salary 400 to 499 "+str(salrange[2]))
    print("Number of employees having salary 500 to 599 "+str(salrange[3]))
    print("Number of employees having salary 600 to 699 "+str(salrange[4]))
    print("Number of employees having salary 700 to 799 "+str(salrange[5]))
    print("Number of employees having salary 800 to 899 "+str(salrange[6]))
    print("Number of employees having salary 900 to 999 "+str(salrange[7]))
    print("Number of employees having salary 999+ "+str(salrange[8]))

if __name__ == '__main__':
    SalespplSalary()



