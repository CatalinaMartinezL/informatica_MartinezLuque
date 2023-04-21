#!/usr/bin/env python3

import re

def mail_correcto(string):
    return bool(re.search('^\w+[.-]\w*[@][a-z]+[.]?[a-z]+[.]?[a-z]?$'), string)
print(mail_correcto('catalinamartinezluque@gmail.com'))
print(mail_correcto('catalina&martinezluqu@gmail.com'))
