def find_assistant_professor(org_dict, prof_name, parent=""):
    """
    org_dict: nested dictionary representing IIIT Ranchi org structure
    prof_name: string, (partial) name of Assistant Professor to search
    parent: keeps track of current department path
    """
    # Standardize the search (case-insensitive)
    name_lower = prof_name.strip().lower()

    for key, value in org_dict.items():
        # If current level has a list of assistant professors
        if key == "Assistant Professors":
            for ap in value:
                if name_lower in ap.lower():  # partial match
                    return ap, parent  # return full name + department

        # If value is another nested dictionary, search recursively
        if isinstance(value, dict):
            result = find_assistant_professor(value, prof_name, parent=key)
            if result:
                return result
    return None


def main():
    iiit_ranchi = {
        "Academic": {
            "Computer Science & Engineering": {
                "Assistant Professors": [
                    "Dr. Roshan Singh",
                    "Dr. Rajiv Kumar",
                    "Dr. Priyank Khare",
                    "Dr. Akash Srivastava",
                    "Dr. Abhinav Kumar"
                ]
            },
            "Electronics & Communication Engineering": {
                "Assistant Professors": [
                    "Dr. Bharat Singh",
                    "Dr. Puja Ghosh",
                    "Dr. Nishit Malviya",
                    "Dr. Tarun Biswas"
                ]
            },
            "Mathematics": {
                "Assistant Professors": [
                    "Dr. Shashi Kant",
                    "Dr. Anuj Singh"
                ]
            },
            "Other Departments": {
                "Assistant Professors": [
                    "Dr. Nitika Nigam",
                    "Dr. Rashmi Panda",
                    "Dr. Kirti Kumari",
                    "Dr. Rishikesh Dutta Tiwary",
                    "Dr. Priyabrat Garanayak",
                    "Dr. Ravi Shanker",
                    "Dr. Noopur",
                    "Dr. Ranjan Kumar Behera",
                    "Dr. Gaurav Sundaram",
                    "Dr. N Kishore Babu",
                    "Dr. Ankita Kumari"
                ]
            }
        }
    }

    name = input("Enter the name of the Assistant Professor: ")
    result = find_assistant_professor(iiit_ranchi, name)
    if result:
        full_name, dept = result
        print(f"{full_name} belongs to the department of {dept}.")
    else:
        print(f"Assistant Professor '{name}' was not found in the structure.")


if __name__ == "__main__":
    main()
