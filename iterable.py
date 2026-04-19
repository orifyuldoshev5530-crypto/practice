print("==== Iterable objects & RANGE ====")
# Iterable objects > string, dict, tuplr, list, range, map, filter ...

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter:{letter}")
for ele in range_obj:
    print(f"the element:{ele}")

print("==== DICTIONARY ====")
# Dictionary is JSON object!
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print(f"person: {person}")
print(f"the person_obj: {person_obj}")

# method: get()
# name = person_obj["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby}, balance: {balance}")

del person_obj["single"]  # del = delete
for key in person_obj:
    print(f"the key: {key}, the value: {person_obj.get(key)}")


print("==== Error handling system ====")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
