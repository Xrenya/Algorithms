ouput = [] 
with open('input.txt') as file:
    bank = {}
    for line in file.readlines():
        operations = list(line.split())
        if len(operations) == 2:
            procedure, percent = operations
            if procedure == "INCOME":
                for client in bank:
                    if bank[client] > 0:
                        bank[client] = bank[client] +int( bank[client] * int(percent)/100)
            if  procedure == "BALANCE":
                if percent not in bank:
                     ouput.append("ERROR")
                else:
                    ouput.append(f"{bank[percent]}")
        if len(operations) == 4:
            procedure, client_1, client_2, sumt = operations
            if procedure == "TRANSFER":
                if client_1 not in bank:
                    bank[client_1] = 0
                if client_2 not in bank:
                    bank[client_2] = 0
                bank[client_1] -= int(sumt)
                bank[client_2] += int(sumt)
        if len(operations) == 3:
            procedure, client, sumt = operations
            if client not in bank:
                bank[client] = 0
            if procedure == "DEPOSIT":
                bank[client] += int(sumt)
            if procedure == "WITHDRAW":
                bank[client] -= int(sumt)
            
with open('output.txt', 'w') as file:
    for key in ouput:
        file.write(f"{key}\n")
