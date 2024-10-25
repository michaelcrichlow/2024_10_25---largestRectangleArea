# This one worked, but ultimately was too slow of a solution.
# 87 / 99 testcases passed
def largestRectangleArea(heights: list[int]) -> int:
    local_array: list[int] = []

    for i in range(len(heights)):
        local_array.append(1)
        for j in range(len(heights)):
            if i != j:
                if heights[i] <= heights[j]:
                    local_array[i] += 1
                elif heights[i] > heights[j]:
                    if j < i:
                        hit_barrier_before = True
                        local_array[i] = 1
                    elif j > i:
                        hit_barrier_after = True
                        break

        local_array[i] = heights[i] * local_array[i]

    # print(local_array)
    return max(local_array)


# LOL This one ALSO worked, but ultimately was too slow of a solution.
# 87 / 99 testcases passed
def largest_rectangle_area(heights: list[int]) -> int:
    temp_val = 0
    max_val = 0
    stack = [1]

    for i in range(len(heights)):
        for j in range(len(heights)):
            if i != j:
                if heights[j] >= heights[i]:
                    stack.append(1)
                if heights[j] < heights[i] and j < i:
                    stack = [1]
                if heights[j] < heights[i] and j > i:
                    break

        temp_val = heights[i] * len(stack)
        stack = [1]
        if temp_val > max_val:
            max_val = temp_val

    return max_val


# This is the one that passed the tests. I still need to fully
# understand this solution. >_<
def largestRectangleArea2(heights: list[int]) -> int:
    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


def main() -> None:
    print(largestRectangleArea2([1, 1]))


if __name__ == '__main__':
    main()
