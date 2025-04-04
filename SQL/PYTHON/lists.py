if __name__ == '__main__':
    N = int(input())
    arr = []
    i = 1
    while i <= N:
        i += 1
        cmd = input().split()
        command = cmd[0]
            
        match command:
            case "insert":
                arr.insert(int(cmd[1]), int(cmd[2]))
            case "print":
                print(arr)
            case "remove":
                arr.remove(int(cmd[1]))
            case "append":
                arr.append(int(cmd[1]))
            case "sort":
                arr.sort()
            case "pop":
                arr.pop()
            case "reverse": 
                arr.reverse()
                    
             