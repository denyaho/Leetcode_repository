# 問題
https://leetcode.com/problems/unique-email-addresses/

#　問題概要
メールアドレスがリストとして与えられるので、特有のメールアドレスがあればその個数を数えて出力する。
localName@domainNameとしてメールアドレスは構成されており、
localNameの部分では+がきたらそれ以降は切り捨て、.がある場合はそれをスキップした文字列をlocalNameとする
例: 
 test.user@local.com -> testuser@local.com
 test.user+domain@local.com -> testuser@local.com

## step1

愚直に、メールアドレスを@でsplitして、local_nameとdomain_nameに区切る(@はこの問題では１個しかないという制約付き)
その後、local_nameに対し「.」と「+」のルールを適用して修正。
得られた後のlocal_nameとdomain_nameでちゃんとしたメールアドレスを作成しsetに入れて、setの長さをreturnする

時間計算量
 emailのリストの長さをnとして、local_nameの長さをm、domain_nameの長さをlとする
 email.split("@")では文字列全体(m + 1程度)を先頭から走査 -> O(m + 1)
 handleLocalNameではO(m)
 - O(n*m)

```
from typing import List

class Solution:
    def handleLocalName(self, local_name: str):
        local_name_without_dots = ""
        for s in local_name:
            if s == "+":
                return local_name_without_dots
            if s == ".":
                continue
            local_name_without_dots += s
        return local_name_without_dots        
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_result = set()
        for email in emails:
            separated_email = email.split("@")
            local_name, domain_name = separated_email[0], separated_email[1]
            email_result.add(self.handleLocalName(local_name) + "@" + domain_name)
        return len(email_result)
```

このコードでは、for文で文字列を毎回新しく作成しているが、
以下の文言より、joinなどを用いるのが良い
```
https://docs.python.org/3/builtins/stdtypes.html#common-sequence-operations

Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below:

if concatenating str objects, you can build a list and use str.join() at the end or else write to an io.StringIO instance and retrieve its value when complete

if concatenating bytes objects, you can similarly use bytes.join() or io.BytesIO, or you can do in-place concatenation with a bytearray object. bytearray objects are mutable and have an efficient overallocation mechanism

if concatenating tuple objects, extend a list instead

for other types, investigate the relevant class documentation
```

* 参考
https://github.com/ksaito0629/leetcode_arai60/pull/13/changes

domain_nameの大きさが4より小さい(.comを満たさない)場合はskipするように修正

```
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_result = set()
        for email in emails:
            separated_email = email.split("@")
            local_name, domain_name = separated_email[0], separated_email[1]
            if len(domain_name) < 4:
                continue
            local_name = local_name.split("+")[0].replace(".", "")
            email_result.add(local_name + "@" + domain_name)
        return len(email_result)
```

ポインタを使う方法
```
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        actual_email = []
         + or @ が来るまで追加
            . は追加しない

        @じゃなくなるまで進む
        """
        if not emails:
            return 0
        actual_emails = set()

        for email in emails:
            actual_email = []
            i = 0
            while email[i] not in '+@':
                if email[i] != '.':
                    actual_email.append(email[i])
                i += 1
            while email[i] != '@':
                i += 1
            actual_email.append(email[i:])
            actual_emails.add(''.join(actual_email))

        return len(actual_emails)
```