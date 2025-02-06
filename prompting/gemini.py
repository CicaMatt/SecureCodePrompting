import os
import google.generativeai as genai

def send_prompt_gemini(prompt):
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error during request: {e}"

prompt = '''
Create a secure prompt template that reliably generates effective solutions for a given coding issue, based on the CWE information provided below. The template must be strictly structured into five sections:
	Objective – A brief description of the security concern, emphasizing its potential risks and impact;
	Problem Statement – A standardized placeholder for the user to describe the issue concisely;
	Mitigation Strategies – A set of clear, actionable best practices and security guidelines to effectively prevent or remediate the identified issue;
	Output Format – Shortly explicit that the solution must be generated as a single and complete code snippet;
	Solution Language - A standardized placeholder for the user to define the desired programming language for the solution.
The template should be concise, meaningful, and optimized to produce highly effective security-focused responses.

Name:
CWE-798: Use of Hard-coded Credentials

Description:
There are two main variations:
- Inbound: the product contains an authentication mechanism that checks the input credentials against a hard-coded set of credentials. In this variant, a default administration account is created, and a simple password is hard-coded into the product and associated with that account. This hard-coded password is the same for each installation of the product, and it usually cannot be changed or disabled by system administrators without manually modifying the program, or otherwise patching the product. It can also be difficult for the administrator to detect.
- Outbound: the product connects to another system or component, and it contains hard-coded credentials for connecting to that component. This variant applies to front-end systems that authenticate with a back-end service. The back-end service may require a fixed password that can be easily discovered. The programmer may simply hard-code those back-end credentials into the front-end product.

Potential Mitigations:
(1) Architecture and Design Phase:
- For outbound authentication: store passwords, keys, and other credentials outside of the code in a strongly-protected, encrypted configuration file or database that is protected from access by all outsiders, including other local users on the same system. Properly protect the key (CWE-320). If you cannot use encryption to protect the file, then make sure that the permissions are as restrictive as possible [REF-7]. In Windows environments, the Encrypted File System (EFS) may provide some protection.
- For inbound authentication: Rather than hard-code a default username and password, key, or other authentication credentials for first time logins, utilize a "first login" mode that requires the user to enter a unique strong password or key.
- If the product must contain hard-coded credentials or they cannot be removed, perform access control checks and limit which entities can access the feature that requires the hard-coded credentials. For example, a feature might only be enabled through the system console instead of through a network connection.
- For inbound authentication using passwords: apply strong one-way hashes to passwords and store those hashes in a configuration file or database with appropriate access control. That way, theft of the file/database still requires the attacker to try to crack the password. When handling an incoming password during authentication, take the hash of the password and compare it to the saved hash.
Use randomly assigned salts for each separate hash that is generated. This increases the amount of computation that an attacker needs to conduct a brute-force attack, possibly limiting the effectiveness of the rainbow table method.
- For front-end to back-end connections: Three solutions are possible, although none are complete.
The first suggestion involves the use of generated passwords or keys that are changed automatically and must be entered at given time intervals by a system administrator. These passwords will be held in memory and only be valid for the time intervals. Next, the passwords or keys should be limited at the back end to only performing actions valid for the front end, as opposed to having full access. Finally, the messages sent should be tagged and checksummed with time sensitive values so as to prevent replay-style attacks.

Modes of Introduction:
(1) Architecture and Design Phase:
- REALIZATION: This weakness is caused during implementation of an architectural security tactic.
'''

# print(send_prompt_gemini(prompt))
