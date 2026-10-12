# ICT Club member verification
from pyscript import display, document

# function name
def verify_candidate(e):
    document.getElementById('result').innerHTML = ''
    
    # collecting the input 1
    first_name = document.getElementById('first_name').value.strip()
    
    # collecting the input 2
    last_name = document.getElementById('last_name').value.strip()
    
    # concanteneting the inputs
    full_name = f"{first_name} {last_name}".strip()
    
    # list of members
    ict_members = ['juan dela cruz', 'maria santos', 'jose rizal', 'andres bonifacio', 'halal cartier', 'patricia sagum']
    
    # input rules
    has_valid_inputs = (' ' not in first_name) and (first_name != '') and (last_name != '')
    
    # member checking
    is_in_list = full_name.lower() in ict_members
    is_member = is_in_list and has_valid_inputs
    
    # output of the message
    display_message = (
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    )
    
    # displaying message
    display(display_message[is_member], target='result')