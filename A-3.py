s = "demstiorals is man."
print(len(s))
print(s.index("a"))
print(s[5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print(s.upper())
print(s.lower())
print(s.startswith("demstiorals"))
print(s.endswith("man."))
