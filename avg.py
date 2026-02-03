# def average_of_five(nums):
#     """
#     nums: list of 5 numbers
#     return: average
#     """
#     # TODO: implement this function
#     pass

# if __name__ == "__main__":
#     nums = list(map(float, input().split()))
#     print(average_of_five(nums))
def average_of_five(nums):
    return sum(nums) / 5


if __name__ == "__main__":
    nums = list(map(float, input().split()))
    print(average_of_five(nums))
