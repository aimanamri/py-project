import util as u

class Calculator:
    def get_input(self):
        while True:
            num_1 = input('Enter num_1 : ').strip()
            num_2 = input('Enter num_2 : ').strip()
            operator = input('Input a math operator  :  ').strip()
            return num_1,num_2,operator

    def calculate(self,num_1,num_2,operator):
        if operator == 'add' or operator == '+':
            print(f'{num_1} + {num_2} = ',u.add(num_1,num_2))
        elif operator == 'subtract' or operator == '-':
            print(f'{num_1} - {num_2} = ',u.subtract(num_1,num_2))
        elif operator == 'multiply' or operator == '*':
            print(f'{num_1} x {num_2} = ',u.multiply(num_1,num_2))
        elif operator == 'divide' or operator == '/':
            print(f'{num_1} ÷ {num_2} = ',u.divide(num_1,num_2))
        else:
            print('INVALID INPUT')
        print('#-----------------------#')

    def main(self):
        print('''
************************BASIC CALCULATOR****************************************
|   Press 'q' to quit or press 'c' to reset number before input the operator.  | 
|   add      :  +                                                              |
|   subtract :  -                                                              |
|   multiply :  *                                                              |
|   divide   :  /                                                              |
********************************************************************************
''')
        while True:
            num_1,num_2,operator = self.get_input()
            self.calculate(num_1,num_2,operator)
            again =input("Calculate again ?  (y/n) \n").lower()
            if again == 'n':
                print('Bye ! See you later.')
                break
            elif again == 'y':
                self.main()

if __name__ == '__main__':
    result = Calculator()
    result.main()