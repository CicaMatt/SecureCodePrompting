import csv
import os
import re

from prompting.codellama import send_prompt_codellama
from prompting.gemini import send_prompt_gemini
from prompting.gpt import send_prompt_gpt

question_id = "123"

question_files = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/Problem Descriptions"
languages_files = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/Problem Languages"

csv_path = "/Users/matteocicalese/Downloads/infos.csv"
secure_prompt_patterns_path = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/Secure prompt patterns (PC)"
to_validate_path = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/To Validate"
secure_prompt_patterns_filled_path = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/Secure prompt patterns (Filled)"
full_answers_path = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/Full Answers"

validation_path = "/Users/matteocicalese/Library/CloudStorage/OneDrive-Personale/Paper/Paper Data/Validation"


def create_questions_files(output_folder, csv_file):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open and read the CSV file
    with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            so_id = row.get('so_id')
            question = row.get('question')
            if so_id is None or question is None:
                print(f"Skipping row with missing 'so_id' or 'question': {row}")
                continue

            # Define the full path for the new .txt file
            txt_file_path = os.path.join(output_folder, f"{so_id}.txt")

            # Write the question content into the file
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(question)
            print(f"Created {txt_file_path}")

def create_languages_files(output_folder, csv_file):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open and read the CSV file
    with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            so_id = row.get('so_id')
            language = row.get('language')
            question = row.get('question')
            if so_id is None or question is None:
                print(f"Skipping row with missing 'so_id' or 'question': {row}")
                continue

            # Define the full path for the new .txt file
            txt_file_path = os.path.join(output_folder, f"{so_id}.txt")

            # Write the question content into the file
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(language)
            print(f"Created {txt_file_path}")


def replace_question_placeholder(text, question_text, placeholder ="[Problem Statement]"):
    quoted_question_text = f'"{question_text}"'
    return text.replace(placeholder, quoted_question_text)

def replace_language_placeholder(text, language_text, placeholder ="[Solution Language]"):
    return text.replace(placeholder, language_text)


def match_question_to_template(secure_templates_dir, problems_dir, languages_dir):
    # Iterate over each programming language folder (e.g., Java, Python, PHP)
    for language in os.listdir(secure_templates_dir):
        language_path = os.path.join(secure_templates_dir, language)
        if not os.path.isdir(language_path):
            continue  # Skip files; we expect directories here

        # For each question directory inside the language folder:
        for question_id in os.listdir(language_path):
            question_id_path = os.path.join(language_path, question_id)
            if not os.path.isdir(question_id_path):
                continue

            # Construct the path to the corresponding problem file.
            # Here we assume the problem file is named "<question_id>.txt".
            problem_file = os.path.join(problems_dir, f"{question_id}.txt")
            if not os.path.exists(problem_file):
                print(f"Problem file for question ID '{question_id}' not found. Skipping.")
                continue

            # Read the content of the problem file.
            with open(problem_file, "r", encoding="utf-8", errors="replace") as pf:
                problem_text = pf.read()

            language_file = os.path.join(languages_dir, f"{question_id}.txt")
            if not os.path.exists(language_file):
                print(f"Language file for question ID '{question_id}' not found. Skipping.")
                continue

            # Read the content of the language file.
            with open(language_file, "r", encoding="utf-8", errors="replace") as pf:
                language_text = pf.read()

            # Now iterate over the CWE directories (subdirectories within the question id folder)
            for cwe_dir in os.listdir(question_id_path):
                cwe_dir_path = os.path.join(question_id_path, cwe_dir)
                if not os.path.isdir(cwe_dir_path):
                    continue

                # Iterate over the prompt files (GPT, Gemini, Codellama)
                for prompt_filename in os.listdir(cwe_dir_path):
                    if prompt_filename.startswith('.'):
                        continue  # Skip hidden files like .DS_Store
                    file_path = os.path.join(cwe_dir_path, prompt_filename)
                    if not os.path.isfile(file_path):
                        continue

                    # Read the current content of the file, handling decoding errors.
                    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
                        content = file.read()

                    # Replace the placeholder with the problem text.
                    new_content_1 = replace_question_placeholder(content, problem_text)
                    new_content_2 = replace_language_placeholder(new_content_1, language_text)

                    # Write the new content back to the file.
                    with open(file_path, "w", encoding="utf-8", errors="replace") as file:
                        file.write(new_content_2)

                    print(f"Updated placeholders in file: {file_path}")

# Time to execute: 45 minutes per 100 prompts
def process_prompts(to_validate_dir, validation_dir):
    processed_prompts = 0

    for language in os.listdir(to_validate_dir):
        language_path = os.path.join(to_validate_dir, language)
        if not os.path.isdir(language_path):
            continue  # Salta eventuali file che non sono directory

        for question_id in os.listdir(language_path):
            question_id_path = os.path.join(language_path, question_id)
            if not os.path.isdir(question_id_path):
                continue

            for cwe_dir in os.listdir(question_id_path):
                cwe_dir_path = os.path.join(question_id_path, cwe_dir)
                if not os.path.isdir(cwe_dir_path):
                    continue

                for prompt_filename in os.listdir(cwe_dir_path):
                    if prompt_filename.startswith('.'):
                        continue

                    file_path = os.path.join(cwe_dir_path, prompt_filename)
                    if not os.path.isfile(file_path):
                        continue

                    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
                        prompt_content = file.read()


                    llm = os.path.splitext(prompt_filename)[0]
                    print(f"Prompting: {language} - {question_id} - {cwe_dir} to {llm}")
                    # print(f"Question:\n'''{prompt_content}'''\n")
                    if llm == "GPT":
                        response = send_prompt_gpt(prompt_content)
                    elif llm == "Gemini":
                        response = send_prompt_gemini(prompt_content)
                    elif llm == "Codellama":
                        response = send_prompt_codellama(prompt_content)
                    else:
                        print(f"Skipping {file_path} due to unrecognized LLM")

                    # Use same directory structure
                    output_dir = os.path.join(validation_dir, language, question_id, cwe_dir)
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_path = os.path.join(output_dir, prompt_filename)

                    with open(output_file_path, "w", encoding="utf-8") as out_file:
                        out_file.write(response)

                    print(f"Answer produced and saved in: {output_file_path}")
                    processed_prompts += 1
                    print(f"Processed prompts: {processed_prompts}")
                    print(f"-----------------------------------------------------------------------------------------\n\n\n")


def extract_code_from_llm_response(file_path):
    """
    Extracts the source code from an LLM response stored in a file.

    The function looks for code blocks delimited by either triple backticks (```)
    or triple single quotes ('''), optionally with a language marker (e.g., java, python, php)
    on the opening delimiter. If one or more code blocks are found, the contents inside them
    are concatenated and returned. Otherwise, the entire file content is assumed to be code
    and is returned unchanged.

    Parameters:
        file_path (str): Path to the file containing the LLM response.

    Returns:
        str: The extracted source code.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except IOError as e:
        raise RuntimeError(f"Could not read file {file_path}: {e}")

    # Regular expression to capture code blocks delimited by either ``` or '''
    # The regex breakdown:
    #   (?P<delimiter>```|''')  -> Matches and names the opening delimiter as "delimiter"
    #   (?:\s*(\w+))?           -> Optionally matches a language identifier (e.g., java, python, php)
    #   \s*\n                  -> Matches any whitespace and a newline right after the opening delimiter
    #   (.*?)                  -> Lazily captures everything until the closing delimiter (the code)
    #   \n?(?P=delimiter)      -> Optionally matches a newline before the closing delimiter, which must match the opening one
    pattern = re.compile(
        r"(?P<delimiter>```|''')"   # Opening delimiter (either ``` or ''')
        r"(?:\s*(\w+))?"            # Optional language identifier (captured in group 2)
        r"\s*\n"                   # Optional whitespace and newline after the opening delimiter
        r"(.*?)"                   # Lazily capture the code (captured in group 3)
        r"\n?(?P=delimiter)",      # Optional newline then the same delimiter as the opening one
        re.DOTALL                  # DOTALL to ensure newlines are included in the match
    )

    matches = pattern.findall(content)
    if matches:
        # Each match is a tuple: (delimiter, language (if any), code)
        # We only need the code portion.
        code_blocks = [match[2].rstrip() for match in matches]
        return "\n".join(code_blocks).strip()
    else:
        # No code block delimiters found; assume the entire content is code.
        return content.strip()


def response_to_code(full_answers_path, only_code_path):
    for language in os.listdir(full_answers_path):
        language_path = os.path.join(full_answers_path, language)
        if not os.path.isdir(language_path):
            continue

        for question_id in os.listdir(language_path):
            question_id_path = os.path.join(language_path, question_id)
            if not os.path.isdir(question_id_path):
                continue

            for cwe_dir in os.listdir(question_id_path):
                cwe_dir_path = os.path.join(question_id_path, cwe_dir)
                if not os.path.isdir(cwe_dir_path):
                    continue

                for prompt_filename in os.listdir(cwe_dir_path):
                    if prompt_filename.startswith('.'):
                        continue

                    file_path = os.path.join(cwe_dir_path, prompt_filename)
                    if not os.path.isfile(file_path):
                        continue

                    extracted_code = extract_code_from_llm_response(file_path)
                    llm = os.path.splitext(prompt_filename)[0]
                    destination = ""
                    if language == "Python":
                        destination = llm + ".py"
                    elif language == "Java":
                        destination = llm + ".java"
                    elif language == "PHP":
                        destination = llm + ".php"


                    output_dir = os.path.join(only_code_path, language, question_id, cwe_dir)
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_path = os.path.join(output_dir, destination)

                    with open(output_file_path, "w", encoding="utf-8") as out_file:
                        out_file.write(extracted_code)


def is_code_matching_language(file_path):
    """
    Analyzes a code snippet file and prints a message only if the code does not
    appear to match the language implied by the file extension (.py, .java, or .php).

    Parameters:
        file_path (str): Path to the code snippet file.
    """
    ext = os.path.splitext(file_path)[1].lower()

    # Determine the expected language based on the file extension.
    if ext == '.py':
        expected_language = 'python'
    elif ext == '.java':
        expected_language = 'java'
    elif ext == '.php':
        expected_language = 'php'
    else:
        print(f"Unsupported file extension: {ext}")
        return

    # Read the file content.
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return

    # Define and apply language-specific heuristics.
    if expected_language == 'python':
        python_patterns = [
            r'^\s*def\s+\w+\(.*\):',  # function definitions
            r'^\s*class\s+\w+\(?.*\)?:',  # class definitions
            r'^\s*import\s+\w+',  # import statements
            r'if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:'  # main guard
        ]
        # Check for any of the Python patterns, including a shebang line.
        match_found = any(re.search(pattern, code, re.MULTILINE) for pattern in python_patterns) \
                      or re.search(r'#!.*python', code, re.IGNORECASE)
        if not match_found:
            print(f"Mismatch: '{file_path}' does not appear to be valid Python code.")

    elif expected_language == 'java':
        java_patterns = [
            r'\bpublic\s+class\s+\w+\s*{',  # public class declaration
            r'\bpublic\s+static\s+void\s+main\s*\(',  # main method signature
            r'\bpackage\s+[\w\.]+;',  # package declaration
            r'\bimport\s+java\.'  # java-specific import
        ]
        match_found = any(re.search(pattern, code) for pattern in java_patterns)
        if not match_found:
            print(f"Mismatch: '{file_path}' does not appear to be valid Java code.")

    elif expected_language == 'php':
        # Check for the PHP opening tag.
        if not re.search(r'<\?php', code, re.IGNORECASE):
            print(f"Mismatch: '{file_path}' does not appear to be valid PHP code.")


def check_snippets_adherence(path):
    for language in os.listdir(path):
        language_path = os.path.join(path, language)
        if not os.path.isdir(language_path):
            continue

        for question_id in os.listdir(language_path):
            question_id_path = os.path.join(language_path, question_id)
            if not os.path.isdir(question_id_path):
                continue

            for cwe_dir in os.listdir(question_id_path):
                cwe_dir_path = os.path.join(question_id_path, cwe_dir)
                if not os.path.isdir(cwe_dir_path):
                    continue

                for prompt_filename in os.listdir(cwe_dir_path):
                    if prompt_filename.startswith('.'):
                        continue

                    file_path = os.path.join(cwe_dir_path, prompt_filename)
                    if not os.path.isfile(file_path):
                        continue

                    is_code_matching_language(file_path)




# create_languages_files(languages_files, csv_path)

# process_prompts(to_validate_path, full_answers_path)
# check_snippets_adherence(validation_path)
match_question_to_template(to_validate_path, question_files, languages_files)
