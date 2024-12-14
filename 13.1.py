with open('13.txt') as file:
    lines = file.readlines()

import re
lines = open("13.txt","r").read()
claw_machines = []

for claw_machine in lines.split("\n\n"):
    buttons = re.findall(r"Button (.): X\+(\d+), Y\+(\d+)",claw_machine)
    prize_cords = re.findall(r"Prize: X=(\d+), Y=(\d+)",claw_machine)
    claw_machine = {"ax": int(buttons[0][1]), "ay": int(buttons[0][2]), "bx": int(buttons[1][1]), "by": int(buttons[1][2]),"xprize": int(prize_cords[0][0]), "yprize": int(prize_cords[0][1])}
    claw_machines.append(claw_machine)

a_cost = 3
b_cost = 1

def get_solutions(ax,ay,bx,by,xprize,yprize):
    for a in range(int(xprize/ax)):
        xval_list = []
        solution_list = []
        xval= ax * a
        if (xprize - xval) % bx == 0:
            b = (xprize-xval) / bx
            xval_list.append({"a":a, "b" : b})
        for val in xval_list:
            if ((val["a"] * ay) + (val["b"] * by)) == yprize:
                solution_list.append(val)
        return get_optimal_solution(solution_list)

def get_optimal_solution(solution_list):
    optimal_solution = 0
    if len(solution_list) == 0:
        return 0
    for solution in solution_list:
        if optimal_solution == 0 or (solution["a"] * a_cost + solution["b"]) < optimal_solution:
            optimal_solution = solution["a"] * a_cost + solution["b"]
    return optimal_solution
 
total_tokens = 0
for machine in claw_machines:
    total_tokens += get_solutions(machine["ax"],machine["ay"],machine["bx"],machine["by"],machine["xprize"],machine["yprize"])
print(total_tokens)
