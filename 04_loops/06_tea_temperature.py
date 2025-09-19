'''
You want to simulate tea heating.
It starts at 40°C and boils at 100°C.
Task:
-Use a while loop.
-Increase temperature by 15 until it reaches or exceeds 100.
-Print each temperature step.
'''

temperature = 40

while temperature < 100:
    #  temperature = temperature + 15
     temperature += 15
     print(f"Current temperature: {temperature}")
print("Tea is ready to boil")




'''
ATM Withdrawal Simulator
Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session. Your task is to simulate how the system should handle each request based on the account balance.

Tasks:

1 Use a while loop to iterate through the list named withdrawals.

 2For every withdrawal:

- ✅ If the current balance is enough:

Subtract the amount.

Append a success message: "Withdrawn: {amount}"

❌ If not enough:

Append a message: "Insufficient funds for requested amount: {amount}"

3 After all withdrawals:

- Append the final balance as: "Remaining Balance: balance"

4 Return a list containing all the messages.

solution -



def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    result = []
    index = 0
    while index < len(withdrawals):
        print(len(withdrawals))
        amount = withdrawals[index]
        if amount <= balance:
            balance -= amount
            result.append(f"Withdrawn: {amount}")
        else:
            result.append(f"Insufficient funds for requested amount: {amount}")
        index += 1
    result.append(f"Remaining Balance: {balance}")
    print(result)
    return result
simulate_atm_withdrawals(2000, [1000, 34, 67, 479, 74759])


'''