from typing import List

class Solution:
    def handleLocalName(self, local_name: str):
        local_name_without_dots = ""
        for s in local_name:
            if s == "+":
                break
            if s != ".":
                local_name_without_dots += s
        return local_name_without_dots        
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_result = set()
        for email in emails:
            separated_email = email.split("@")
            local_name, domain_name = separated_email[0], separated_email[1]
            email_result.add(self.handleLocalName(local_name) + "@" + domain_name)
        return len(email_result)