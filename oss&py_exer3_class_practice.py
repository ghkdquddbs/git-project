class ComplexCalculator:
    def __init__(self):
        self.real0=0
        self.imaginary0=0
        self.ops=''
        self.real1=0
        self.imaginary1=0
        self.a=0
        self.b=0

    def calculate(self, user_input):
        tokens=user_input.split()
        self.real0=float(tokens[0])
        self.imaginary0=float(tokens[1])
        self.ops=tokens[2]
        self.real1=float(tokens[3])
        self.imaginary1=float(tokens[4])
        match self.ops:
            case'+':
                self.a=self.real0+self.real1
                self.b=self.imaginary0+self.imaginary1
            case'-':
                self.a=self.real0-self.real1
                self.b=self.imaginary0-self.imaginary1
            case'*':
                self.a = self.real0 * self.u - self.y * self.v
                self.b = self.real1 * self.v + self.y * self.u
            case'/':
                self.a=self.real0/self.real1
                self.b=self.imaginary0/self.imaginary1
    def __repr__(self):
        if self.b>0:
            return str(self.a)+'+'+str(self.b)+'i'
        else:
            return str(self.a)+'-'+str(self.b)+'i'

user_input=input('계산식을 다음과 같은 형식으로 입력하시오(ex. "3 4 + 1 2" -> 4+6i ): ')
cp=ComplexCalculator()
cp.calculate(user_input)
print(cp)