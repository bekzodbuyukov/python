# collections module'idan defaultdict sub-class'ni import qilamiz
from collections import defaultdict


# mavjud bo'lmagan qiymatlar (value) uchun default qiymat
def return_default_value():
    return "Value doesn't exist"


# default dict asosida dictionary yaratamiz
test_dict = defaultdict(return_default_value)

# dictionary'ga key:value syntax'si asosida ma'lumot kiritamiz
test_dict["a"] = "Letter: a"
test_dict["b"] = "Letter: b"

if __name__ == "__main__":
    # dictionary elementlarini chop etamiz
    print(test_dict["a"])
    print(test_dict["b"])
    # dictionary'ning mavjud bo'lmagan elementini chop etamiz
    print(test_dict["c"])
    # natijada "Value doesn't exist" qiymatini olamiz
    # Sinab ko'ring!