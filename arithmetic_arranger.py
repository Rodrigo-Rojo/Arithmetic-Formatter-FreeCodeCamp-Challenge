def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    arranged_problems = arranged_problems2 = result_line = result = ""
    spaces = {"1": " ","2": "  ","3": "   ","4": "    ","5": "     "}
    dashes = {"1": "---","2": "----","3": "-----","4": "------",}
    nums1, symbols, nums2 = [x for x, y, p in [problem.split() for problem in problems]], [x for y, x, p in [problem.split() for problem in problems]], [x for y, p, x in [problem.split() for problem in problems]]
    for i in range(len(nums1)):
        if len(nums1[i]) > 4 or len(nums2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if "-" != symbols[i] != "+":
            return "Error: Operator must be '+' or '-'."
        try:
            int(nums1[i]), int(nums2[i])
        except:
            return "Error: Numbers must only contain digits."
        if symbols[i] == "+":
            solved = str(int(nums1[i]) + int(nums2[i]))
        else:
            solved = str(int(nums1[i]) - int(nums2[i]))
        if i == len(nums1) - 1:
            arranged_problems += f"{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 2 - len(nums1[i]))]}{nums1[i]}\n"
            arranged_problems2 += f"{symbols[i]}{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 1 - len(nums2[i]))]}{nums2[i]}\n"
            result_line += dashes[str(max([len(nums1[i]), len(nums2[i])]))]
            if answer:
                result += f"{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 2 - len(solved))]}{solved}"
        else:
            arranged_problems += f"{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 2 - len(nums1[i]))]}{nums1[i]}    "
            arranged_problems2 += f"{symbols[i]}{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 1 - len(nums2[i]) )]}{nums2[i]}    "
            result_line += f"{dashes[str(max([len(nums1[i]), len(nums2[i])]))]}    "
            if i == 0:
                if answer:
                    result += f"\n{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 2 - len(solved))]}{solved}    "
            elif i != 0 and answer:
                result += f"{spaces[str(max([len(nums1[i]), len(nums2[i])]) + 2 - len(solved))]}{solved}    "

    return arranged_problems + arranged_problems2 + result_line + result
