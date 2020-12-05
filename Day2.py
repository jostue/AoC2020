
file = open('Day2PuzzleInput.txt','r')
lines = file.readlines()



## Day2.1
validPasswords0 = 0
for line in lines:
    policy, passwort = line.split(":")

    policy_minmax, policy_letter = policy.split()
    policy_min, policy_max = policy_minmax.split("-")

    letterCount = passwort.count(policy_letter)
    if (letterCount >= int(policy_min)) and (letterCount <= int(policy_max)):
        validPasswords0 += 1

print(validPasswords0)

## Day2.2
validPasswords1 = 0
for line in lines:
    policy, passwort = line.split(":")

    policy_minmax, policy_letter = policy.split()
    policy_min, policy_max = policy_minmax.split("-")
    
    if(((policy_letter == passwort[int(policy_min)]) and (policy_letter != passwort[int(policy_max)])) or
       ((policy_letter != passwort[int(policy_min)]) and (policy_letter == passwort[int(policy_max)]))):
        validPasswords1 += 1

print(validPasswords1)