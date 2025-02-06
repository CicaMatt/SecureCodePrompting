import os
from openai import OpenAI

def send_prompt_gpt(prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o",
        )
        return chat_completion.choices[0].message.content

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
CWE-259: Use of Hard-coded Password

Description:
A hard-coded password typically leads to a significant authentication failure that can be difficult for the system administrator to detect. Once detected, it can be difficult to fix, so the administrator may be forced into disabling the product entirely. There are two main variations:
- Inbound: the product contains an authentication mechanism that checks for a hard-coded password.
- Outbound: the product connects to another system or component, and it contains hard-coded password for connecting to that component.
In the Inbound variant, a default administration account is created, and a simple password is hard-coded into the product and associated with that account. This hard-coded password is the same for each installation of the product, and it usually cannot be changed or disabled by system administrators without manually modifying the program, or otherwise patching the product. If the password is ever discovered or published (a common occurrence on the Internet), then anybody with knowledge of this password can access the product. Finally, since all installations of the product will have the same password, even across different organizations, this enables massive attacks such as worms to take place.
The Outbound variant applies to front-end systems that authenticate with a back-end service. The back-end service may require a fixed password which can be easily discovered. The programmer may simply hard-code those back-end credentials into the front-end product. Any user of that program may be able to extract the password. Client-side systems with hard-coded passwords pose even more of a threat, since the extraction of a password from a binary is usually very simple.

Potential Mitigations:
(1) Architecture and Design Phase:
- For outbound authentication: store passwords outside of the code in a strongly-protected, encrypted configuration file or database that is protected from access by all outsiders, including other local users on the same system. Properly protect the key (CWE-320). If you cannot use encryption to protect the file, then make sure that the permissions are as restrictive as possible.
- For inbound authentication: Rather than hard-code a default username and password for first time logins, utilize a "first login" mode that requires the user to enter a unique strong password.
- Perform access control checks and limit which entities can access the feature that requires the hard-coded password. For example, a feature might only be enabled through the system console instead of through a network connection.
- For inbound authentication: apply strong one-way hashes to your passwords and store those hashes in a configuration file or database with appropriate access control. That way, theft of the file/database still requires the attacker to try to crack the password. When receiving an incoming password during authentication, take the hash of the password and compare it to the hash that you have saved.
Use randomly assigned salts for each separate hash that you generate. This increases the amount of computation that an attacker needs to conduct a brute-force attack, possibly limiting the effectiveness of the rainbow table method.
- For front-end to back-end connections: Three solutions are possible, although none are complete.
The first suggestion involves the use of generated passwords which are changed automatically and must be entered at given time intervals by a system administrator. These passwords will be held in memory and only be valid for the time intervals. Next, the passwords used should be limited at the back end to only performing actions valid for the front end, as opposed to having full access. Finally, the messages sent should be tagged and checksummed with time sensitive values so as to prevent replay style attacks.

Modes of introduction:
(1) Implementation Phase: 
- REALIZATION: This weakness is caused during implementation of an architectural security tactic.
'''

# print(send_prompt_gpt(prompt))
