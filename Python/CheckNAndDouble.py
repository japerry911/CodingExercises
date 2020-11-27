def checkIfExist(self, arr: List[int]) -> bool:
    for indx, element in enumerate(arr):
        doubled = element * 2

        new_arr = arr.copy()
        del new_arr[indx]

        if doubled in new_arr:
            return True

    return False
