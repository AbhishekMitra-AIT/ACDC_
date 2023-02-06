# below code takes text from acdc lectures
# removes newlines from them and writes
# back to a new text file(convereted)
# ACDC_practise
with open('point_cloud.txt',mode='r') as file:
    txt = file.read().split(sep='\n')

with open('converted.txt',mode='w') as file:
    file.write(str(txt))