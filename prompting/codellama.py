from ollama import Client

def send_prompt_codellama(prompt):
    client = Client(host='http://localhost:11434')

    response=client.chat(model="codellama:13b", messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response['message']['content']


prompt = '''
Using the provided secure prompt templates—each designed to mitigate a specific CWE—merge them into a single comprehensive secure prompt template. The combined template should be structured consistently with the original sections and incorporate all key security considerations from the addressed CWEs to maximize the security of the generated code.

**Template CWE-259**:
"Objective:
A secure prompt template for addressing CWE-259: Use of Hard-coded Password

Problem Statement:
[Problem Statement]

Mitigation Strategies:
(1) Store passwords outside of code in a strongly-protected encrypted configuration file or database, protected from access by all outsiders. Properly protect the key. If encryption is not possible, limit permissions to restrict access.

(2) Rather than hard-code default usernames and passwords for first time logins, utilize "first login" mode that requires unique strong passwords.

(3) Perform access control checks to limit entities with access to the feature requiring the hard-coded password. Enforce the feature only through system console instead of network connection.

(4) For inbound authentication, apply strong one-way hashes to passwords and store those hashes in a configuration file or database with appropriate access control. Compare incoming hashes to stored hashes during authentication. Use randomly assigned salts for each separate hash generated.

(5) For front-end to back-end connections, use generated passwords that are changed automatically and must be entered at given time intervals by system administrator. Limit the back end to only performing actions valid for the front end. Tag and checksum messages sent with time sensitive values to prevent replay style attacks.

Output Format:
A single complete code snippet that addresses the identified issue in a secure manner.

Solution Language:
[Solution Language]"

**Template CWE-295**:
"Objective:
-----------

The objective of this solution template is to provide a comprehensive approach to addressing the security concern of improper certificate validation, as identified by the CWE-295. This template is designed to be used during the implementation phase and will help you mitigate the risks associated with this issue.

Problem Statement:
--------------------

[Problem Statement]

Mitigation Strategies:
-------------------------

To mitigate this issue, we recommend that you follow these best practices and guidelines:

1. Architecture, Design, and Implementation Phases:
	* Ensure that all relevant properties of the certificate are fully validated before pinning it. This includes the hostname.
2. Implementation Phase:
	* Use a secure protocol for certificate validation to prevent attackers from manipulating the certificates.
	* Implement certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses to ensure that the product is aware of any revoked or compromised certificates.
3. Testing and Deployment:
	* Conduct thorough testing to ensure that all vulnerabilities have been addressed before deploying the solution in production.

Output Format:
-------------

The output format for this template will be a single and complete code snippet in the language specified by the user. The code snippet will include the necessary modifications to address the security concern of improper certificate validation.

Solution Language:
------------------

[Solution Language]"

**Template CWE-327**:
"Objective:
A secure solution that uses a strong and up-to-date cryptographic algorithm to protect sensitive data.
Problem Statement:
[Problem Statement]
Mitigation Strategies:
1. Ensure that the design allows one cryptographic algorithm to be replaced with another in the next generation or version, and ensure that the keys are carefully managed and protected.
2. Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
3. Implement industry-approved techniques correctly to prevent common attacks.
Output Format:
A complete code snippet in the desired programming language that uses a strong and up-to-date cryptographic algorithm to protect sensitive data.
Solution Language: [Solution Language]"

**Template CWE-397**:
"Objective:
To provide a clear and concise description of the security concern identified by CWE-397, including its potential risks and impact.

Problem Statement:
[Problem Statement]

Mitigation Strategies:
To mitigate this issue, we recommend implementing best practices for declaring exceptions in Java programs. This includes:

* Declaring specific exception types that are relevant to the method being called.
* Providing a clear and concise description of each potential exception that can be thrown by the method.
* Including examples of how callers should handle each exception.

Output Format:
The solution must be generated as a single and complete code snippet in the specified programming language.

Solution Language:
[Solution Language]"

**Template CWE-477**:
"Objective:
The objective of this template is to provide a comprehensive solution for addressing the CWE-477: Use of Obsolete Function vulnerability in software development.

Problem Statement:
[Problem Statement]

Mitigation Strategies:
Based on the potential mitigations provided by CWE-477, this template provides a set of best practices and guidelines to effectively prevent or remediate the use of obsolete functions. These strategies include:

1. Implementation Phase: Refer to the documentation for the obsolete function in order to determine why it is deprecated or obsolete and to learn about alternative ways to achieve the same functionality. This approach helps ensure that the user has a clear understanding of the reasons behind the deprecation and can make an informed decision about whether to use an alternate function.
2. Requirements Phase: Consider seriously the security implications of using an obsolete function. Consider using alternate functions. This strategy emphasizes the importance of security in software development, encouraging users to take a proactive approach when it comes to selecting and implementing appropriate security controls.

Output Format:
The solution must be generated as a single and complete code snippet in the desired programming language. This ensures that the resulting code is easy to understand and can be effectively integrated into existing software systems.

Solution Language: [Solution Language]"

**Template CWE-798**:
"Objective:
The objective of this template is to create a secure prompt that generates effective solutions for the given coding issue related to CWE-798, which is an instance of "Use of Hard-coded Credentials." The template should provide concise and meaningful guidance on how to prevent or mitigate the identified security concern.

Problem Statement:
[Problem Statement]

Mitigation Strategies:
The mitigation strategies section should provide clear, actionable best practices and security guidelines to effectively prevent or remediate the identified issue. The strategies should be based on the potential mitigations provided in the CWE information, and they should be structured into five sections:

1. Architecture and Design Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the architecture and design phase of the project. Examples include storing passwords or keys outside of the code, using randomly generated salts for password hashes, limiting access to features that require hard-coded credentials, and implementing time-based authentication mechanisms.
2. Implementation Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the implementation phase of the project. Examples include using secure coding practices when writing code, storing passwords or keys in a configuration file or database with appropriate access control, and implementing encryption to protect sensitive data.
3. Deployment Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the deployment phase of the project. Examples include ensuring that all software updates are applied promptly and regularly, and implementing a security monitoring system to detect and respond to potential security threats.
4. Maintenance Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the maintenance phase of the project. Examples include regularly reviewing and updating security policies and procedures, conducting security audits and assessments, and implementing a incident response plan in case of a security breach or attack.
5. Continuous Improvement: This section should provide guidance on how to address issues related to hard-coded credentials during the continuous improvement phase of the project. Examples include regularly updating software and systems with the latest security patches, implementing automated tools for vulnerability assessment and penetration testing, and investing in continued education and training for developers and other security professionals.

Output Format:
The solution must be generated as a single and complete code snippet in the programming language defined by the user. This will ensure that the proposed solution is actionable and can be quickly implemented to address the identified issue.

Solution Language:
[Solution Language]"
'''
print(send_prompt_codellama(prompt))