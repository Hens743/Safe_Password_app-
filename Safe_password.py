import streamlit as st
import secrets
import string
import math

def calculate_entropy(length, include_letters=True, include_digits=True, include_punctuation=True, include_specials=False, include_scandinavian=False, include_icelandic=False):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    if include_specials:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/~`£µ"
    if include_scandinavian:
        characters += "åäöÅÄÖåÅäÄöÖøØæÆ"  # Scandinavian characters
    if include_icelandic:
        characters += "áÁðÐéÉíÍóÓúÚýÝþÞ"  # Icelandic characters
    
    if not characters:
        return 0
    
    N = len(characters)
    entropy = math.log2(N ** length)
    return entropy

def estimate_strength(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 56:
        return "Weak"
    elif entropy < 84:
        return "Moderate"
    elif entropy < 112:
        return "Strong"
    else:
        return "Very Strong"

def generate_password(length, include_letters=True, include_digits=True, include_punctuation=True, include_specials=False, include_scandinavian=False, include_icelandic=False):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    if include_specials:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/~`£µ"
    if include_scandinavian:
        characters += "åäöÅÄÖåÅäÄöÖøØæÆ"  # Scandinavian characters
    if include_icelandic:
        characters += "áÁðÐéÉíÍóÓúÚýÝþÞ"  # Icelandic characters
    
    if not characters:
        st.error("Please select at least one character type.")
        return
    
    password = ''.join((secrets.choice(characters) for _ in range(length)))
    return password

st.title("Secure Password Generator")

# Options for generating the password
length = st.number_input("Length of Password", min_value=1, value=8, step=1)
include_letters = st.checkbox("Include Letters", value=True)
include_digits = st.checkbox("Include Digits", value=True)
include_punctuation = st.checkbox("Include Punctuation", value=True)
include_specials = st.checkbox("Include Special Characters", value=False)
include_scandinavian = st.checkbox("Include Scandinavian Characters", value=False)
include_icelandic = st.checkbox("Include Icelandic Characters", value=False)

if st.button("Generate Password"):
    entropy = calculate_entropy(length, include_letters, include_digits, include_punctuation, include_specials, include_scandinavian, include_icelandic)
    password = generate_password(length, include_letters, include_digits, include_punctuation, include_specials, include_scandinavian, include_icelandic)
    if password:
        strength = estimate_strength(entropy)
        st.success(f"Generated Password: {password}\nStrength: {strength}\nEntropy: {entropy} bits")

# Recommended guidelines
st.sidebar.markdown("### Common Guidelines")
st.sidebar.markdown("""
- Consider a minimum password length of 8 characters as a general guide. Both the US and UK cyber security departments recommend long and easily memorable passwords over short complex ones.
- Generate passwords randomly where feasible.
- Avoid using the same password twice (e.g. across multiple user accounts and/or software systems).
- Avoid character repetition, keyboard patterns, dictionary words, and sequential letters or numbers.
- Avoid using information that is or might become publicly associated with the user or the account, such as the user name, ancestors' names, or dates.
- Avoid using information that the user's colleagues and/or acquaintances might know to be associated with the user, such as relatives or pet names, romantic links (current or past), and biographical information (e.g. ID numbers, ancestors' names or dates).
- Do not use passwords that consist wholly of any simple combination of the aforementioned weak components. 
Source (https://en.wikipedia.org/wiki/Password_strength)
""")
