"""
G-TASK

Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini. """

# Masalaning yechimi


def get(arr):
    return arr.index(max(arr))


print(get([2, 32, 66, 21, 22]))
