old_password = "Hello123"
new_password = "Goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "Goodbye321"
compare_new = new_password == repeat_new_password

print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced correctly? {compare_new}")


sams_age = 16
too_young = sams_age < 17
car_driver = sams_age >= 17

print(f"Is Sam too young to drive? {too_young}")
print(f"Can Sam drive a car? {car_driver}")

age = 15
adult_ticket = age >= 12

print(f"Buy one adult ticket: {adult_ticket}")
