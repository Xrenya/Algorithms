class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_filter = []
        for email in emails:
            name, domain = email.split('@')
            name = name.split('+')[0]
            name = name.split('.')
            address = ''.join(name) + '@' + domain
            if address not in email_filter:
                email_filter.append(address)
        return len(email_filter)
      
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_filter = []
        for email in emails:
            name, domain = email.split('@')
            login = ''
            for letter in name.split('+')[0]:
                if letter != '.':
                    login += letter
            if (login + '@' + domain) not in email_filter:
                email_filter.append(login + '@' + domain)
        return len(email_filter)
