import re

pattern = r".*?(\d+)"
compiled = re.compile(pattern)

# match: 先頭で一致する必要がある
a = compiled.match("hoge42fuga") # => <_sre.SRE_Match object; span=(0, 6), match='hoge42'>
# match しなければ None を返す

# 任意の位置でマッチすればよい
a = compiled.search("hoge42fuga") # => <_sre.SRE_Match object; span=(0, 6), match='hoge42'>


a.group() # => 'hoge42'
a.group(1) # => "42"
