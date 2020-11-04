#Mickey "likes fittos" Saine
#SDEV 220
# This program is designed to design a class named Account that contains certain the listed text variables
#20 September 2020



class Account:																											#Defines the class created for the program testing
    def __init__(self,id=0,balance=100,annualIntersetRate=0):															#Defines the variables necessary to execute
        self.__id = id
        self.__balance = balance
        self.__annualIntersetRate = annualIntersetRate

    def getId(self):																									#Defines the attributes that that command can do such as get id 
        return self.__id																								#defines the action taken with the attribute given

    def getBalance(self):
        return self.__balance																							#defines the action taken with the attribute given. I really wanna make one of these "meow" after my 14 videos

    def getAnnualIntersetRate(self):
        return self.__annualIntersetRate																				#defines the action taken with the attribute given. I really wanna make one of these "meow" after my 14 videos

    def setId(self,id):
        self.__id = id

    def setBalance(self,balance):
        self.__balance = balance

    def setAnnualIntersetRate(self,annualIntersetRate):
        self.__annualIntersetRate = annualIntersetRate																	#defines the action taken with the attribute given.  I really wanna make one of these "meow" after my 14 videos

    def getMonthlyInterestRate(self):
        return (self.__annualIntersetRate/ 12) /100																		#defines the action taken with the attribute given.  I really wanna make one of these "meow" after my 14 videos

    def getMonthlyInterest(self):
        return self.__balance *self.getMonthlyInterestRate()															#defines the action taken with the attribute given.  I really wanna make one of these "meow" after my 14 videos

    def deposit(self,balance):
        self.__balance += balance																						#defines the action taken with the attribute given.  I really wanna make one of these "meow" after my 14 videos

    def withdraw(self,amount):
        self.__balance -= amount																						#defines the action taken with the attribute given.  I really wanna make one of these "meow" after my 14 videos