class Stack():
    
    def __init__(self):
        self.state = []

    def empty(self):
        if not self.state:
            return True
        else:
            return False

    def push(self, data):
        self.state.append(data)

    def pop(self):
        if self.empty():
            return None
        return self.state.pop()
    
    def peek(self):
        if self.empty():
            return None
        return self.state[-1:]
        
    
s = Stack()
s.push("New Tab")
running = True

while running:

    if s.empty():
        running = False

    else:
        decision = input()
        
        if decision == "enter":
            data = input()
            s.push(data)
            print(f"{data}입장")

        elif decision == "exit":
            data = s.pop()
            print(f"{data}퇴장")
            print(f"현 상태: {s.peek()}")
    
        else:
            print("잘못된 접근")
            continue
