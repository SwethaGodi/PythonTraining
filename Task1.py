firstName = input("Enter Your First Name:")
lastName = input("Enter Your Last Name:")
email = input("Enter Your Email ID:")
phone = input("Enter Your Phone Number:")
dob = input("Enter Your Date Of Birth (DD/MM/YYYY):")
gender = input("Enter Your Gender:")
streetAddress = input("Enter Your Street Address:")
city = input("Enter Your City:")
state = input("Enter Your State:")
zipcode = input("Enter Your Zip Code:")
linkedin = input("Enter Your Linkedin Profile URL:")
technology = input("Enter Your Technology:")
experience = input("Enter Your Experience:")
currentCompany = input("Enter Your Current Company:")

# Print the User Information
print("User Information".center(40, "-")) 
print("Full Name         : {} {}".format(firstName.capitalize(), lastName.capitalize()))
print("Email ID          : {}".format(email.lower()))
print("Phone Number      : {}".format(phone))
print("Date of Birth     : {}".format(dob))
print("Gender            : {}".format(gender.capitalize()))
print("Address           : {}, {}, {}, {}".format(streetAddress.title(), city.title(), state.title(), zipcode))
print("Linkedin Address  : {}".format(linkedin.lower()))
print("Technology        : {}".format(technology.title()))
print("Num of Experience : {}".format(experience))
print("Current Company   : {}".format(currentCompany.title()))