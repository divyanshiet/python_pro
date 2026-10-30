def average(nums: list[float]) -> float:
    if len(nums) == 0:
        raise ValueError("Cannot compute average of an empty list")
    return sum(nums) / len(nums)