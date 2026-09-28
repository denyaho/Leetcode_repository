from typing import List 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result_emails = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            if len(domain_name) < 4:
                continue
            local_name = local_name.split("+")[0].replace(".", "")
            result_emails.add(f"{local_name}@{domain_name}")
        return len(result_emails)