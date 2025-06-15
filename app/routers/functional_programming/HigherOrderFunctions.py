# Higher Order functions are functions that can take other functions as arguments or return them as results.
#Step 1
def build_email(name, domain):
    """
    Returns an email address for the given name and domain.
    """
    if(domain == "gmail.com"):
        return f"{name}@gmail.com"
    elif(domain == "yahoo.com"):
        return f"{name}@yahoo.com"
    elif(domain == "hotmail.com"):
        return f"{name}@hotmail.com"
    elif(domain == "innideas.com"):
        return f"{name}@innideas.com"
    else:
        return f"{name}@unknown.com"

print(build_email("vijay", "gmail.com"))
print(build_email("kumar", "yahoo.com"))
print(build_email("Ananth", "hotmail.com"))
print(build_email("vk", "innideas.com"))

# Step 2  Without Changing the function signature ,we can try with a higher order function

def gmail_builder(name):
    """
    Returns a Gmail address for the given name.
    """
    return f"{name}@gmail.com"

def yahoo_builder(name):
    """
    Returns a Yahoo address for the given name.
    """
    return f"{name}@yahoo.com"

def hotmail_builder(name):
    """
    Returns a Hotmail address for the given name.
    """
    return f"{name}@hotmail.com"

def innideas_builder(name):
    """
    Returns an InnIdeas address for the given name.
    """
    return f"{name}@innideas.com"

def build_email_with_builder(name, domainbuilder):
    """
    Returns an email address for the given name using the specified builder function.
    """
    return domainbuilder(name)

print(build_email_with_builder("vijay", gmail_builder))
print(build_email_with_builder("kumar", yahoo_builder))
print(build_email_with_builder("Ananth", hotmail_builder))
print(build_email_with_builder("vk", innideas_builder))

# Step 3: Using a higher order function to create a domain-specific email builder



def domain_builder(domain):
    """
    Returns a function that checks if a given email is valid for the specified domain.
    """
    def mail_builder(name):
        return f"{name}@{domain}.com"    
    return mail_builder

gmail_checker = domain_builder("gmail.com")

yahoo_checker = domain_builder("yahoo.com")

hotmail_checker = domain_builder("hotmail.com")

innideas_checker = domain_builder("innideas.com")

print(gmail_checker("vijay"))
print(yahoo_checker("kumar"))
print(hotmail_checker("Ananth"))
print(innideas_checker("vk"))
 