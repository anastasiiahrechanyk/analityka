class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.deque = [0] * k
        self.front = -1
        self.rear = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.k - 1
        else:
            self.front -= 1
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == self.k - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.k - 1:
            self.front = 0
        else:
            self.front += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.k - 1
        else:
            self.rear -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.k == self.front


if __name__ == "__main__":
    myCircularDeque = MyCircularDeque(3)
    print(myCircularDeque.insertLast(1))  
    print(myCircularDeque.insertLast(2))  
    print(myCircularDeque.insertFront(3)) 
    print(myCircularDeque.insertFront(4)) 
    print(myCircularDeque.getRear())      
    print(myCircularDeque.isFull())       
    print(myCircularDeque.deleteLast())   
    print(myCircularDeque.getFront())     











ChatGPT can make mistakes. Check important info. See Cookie Preferences.
