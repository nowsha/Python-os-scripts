import os

def count_phrase_in_file(filepath, phrase):
    """Counts the number of times a phrase appears in a file.

    Args:
        filepath: The path to the file.
        phrase: The phrase to search for.

    Returns:
        The number of times the phrase appears in the file.
    """
    count = 0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                count += line.lower().count(phrase.lower())
    except FileNotFoundError:
         return f"Error: File not found at {filepath}"
    return count

def find_file(filename, search_path):
    """
    Finds a file within a specified directory and its subdirectories.

    Args:
        filename (str): The name of the file to find.
        search_path (str): The root directory to begin the search from.

    Returns:
        str: The absolute path of the file if found, otherwise None.
    """
    for root, _, files in os.walk(search_path):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))
    return None

def find_files(filename, search_path):
    """
    Finds all occurrences of a file within a specified directory and its subdirectories.

    Args:
        filename: The name of the file to search for.
        search_path: The root directory to begin the search from.

    Returns:
        A list of strings, where each string is the full path to a found file.
        Returns an empty list if the file is not found.
    """
    results = []
    for root, _, files in os.walk(search_path):
        if filename in files:
            results.append(os.path.join(root, filename))
    return results

def replace_string_in_file(filename, old_string, new_string):
    """
    Replaces all occurrences of old_string with new_string in the file specified by filename.

    Args:
        filename (str): The path to the file.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.
    """
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
         print(f"Error: File not found: {filename}")
         return

    updated_content = file_content.replace(old_string, new_string)

    with open(filename, 'w') as file:
        file.write(updated_content)