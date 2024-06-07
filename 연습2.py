fxfdgs























class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def set_travel_mode(self,min):
        print(f"{self.name}을 {str(min)}분동안여행모드on")

b1 = BlackBox("까망이",2000)
b1.set_travel_mode(100 )
BlackBox.set_travel_mode(b1,100)