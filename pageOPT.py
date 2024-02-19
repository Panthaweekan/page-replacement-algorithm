# Function to simulate the page replacement algorithm for a given capacity and reference string
def page_replacement(capacity, reference_string):
    # Convert the reference string into a list of integers
    s = list(map(int, reference_string.split()))
    f, fault, pf = [], 0, 'No'
    occurance = [None for i in range(capacity)]
    
    # Print header
    print("frame number : ", capacity)
    print("reference string : " + reference_string)
    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i+1, end=' ')
    print("Fault\n   ↓\n")
    
    # Iterate over each page in the reference string
    for i in range(len(s)):
        # If the page is not in the frame
        if s[i] not in f:
            # If there is space in the frame, add the page to the frame
            if len(f) < capacity:
                f.append(s[i])
            # If the frame is full, replace the page using the OPT algorithm
            else:
                for x in range(len(f)):
                    if f[x] not in s[i+1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i+1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = s[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        # Print the page reference and frame state for each step
        print("   %d\t\t" % s[i], end='')
        for x in f:
            print(x, end=' ')
        for x in range(capacity - len(f)):
            print(' ', end=' ')
        print(" %s" % pf)
    
    # Print the total requests, total page faults, fault rate, and hit rate
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%\nHit Rate: %0.2f%%\n" % (len(s), fault, (fault / len(s)) * 100 , 100 - ((fault / len(s)) * 100)))

# Functions defining different reference cases
def ref_1():
    reference_string = "1 2 6 4 0 1 7 9 6 4 1 1 1 8 0 6 5 5 5 2 7 9 2 4 9 3 3 9 5 2"
    for i in range(6):
        capacity = 3+i
        page_replacement(capacity, reference_string)

def ref_2():
    reference_string = "2 9 3 7 8 8 8 9 0 7 9 4 1 1 7 2 1 3 7 5 4 9 4 9 2 2 7 3 6 3 4 3 5 1 8 3 5 6 3 6 8 9 3 7 3 0 5 9 0 7"
    for i in range(6):
        capacity = 4+i
        page_replacement(capacity, reference_string)

def ref_3():
    reference_string = "9 4 8 3 2 8 5 6 4 4 1 5 0 7 6 1 0 3 9 8 3 4 5 3 5 8 3 6 3 5 3 4 1 2 8 2 7 1 9 4 2 6 2 6 9 5 4 7 2 9 6 9 8 0 2 5 9 6 2 5 3 3 1 1 4 7 4 3 3 5 9 6 7 7 5 3 5 4 1 8 6 3 4 0 2 8 1 5 2 7 9 9 5 0 7 2 6 1 9 3"
    for i in range(6):
        capacity = 5+i
        page_replacement(capacity, reference_string)

# Function to switch between different reference cases
def switch_case(case):
    func = switch.get(case, lambda: print("Invalid case"))
    func()

# Dictionary mapping user input to reference cases
switch = {
    "1": ref_1,
    "2": ref_2,
    "3": ref_3
}

# Prompt the user to select a reference case and execute it
print("select reference case 1-30 pages 2-50 pages 3-100 pages: ", end="")
switch_case(input())