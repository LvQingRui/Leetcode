# [1,1,2]
# [1,2...]


def removeDuplicates(nums: list[int]) -> int:
    for x, y in enumerate(sorted(set(nums))):
        nums[x] = y
    return len(set(nums))


if __name__ == "__main__":
    a = removeDuplicates([-1, 0, 0, 0, 0, 3, 3])
    print(a)
