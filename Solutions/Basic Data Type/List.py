if __name__ == '__main__':
    n = int(input())
    prompt = []
    
    for _ in range(n):
        command1 = list(input().split())
        if command1[0] =='insert':
            prompt.insert(int(command1[1]),int(command1[2]))
        elif command1[0] =='append':
            prompt.append(int(command1[1]))
        elif command1[0] =='print':
            print(prompt)
        elif command1[0] =='sort':
        
            prompt.sort()
        elif command1[0] =='reverse':
            prompt.reverse()
        elif command1[0] =='pop':
            prompt.pop()
        elif command1[0] =='remove':
            prompt.remove(int(command1[1]))
