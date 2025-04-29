msg = "Jambo Kenya"
print (msg)
if msg == "Jambo Kenya":
    print("Karibu Kenya")

file_path = "/data/meteo/VRXA00.202310190530"  
print(file_path)

Read file as text and print content
th open(file=file_path) as fh:
file_content = fh.readlines()
int(file_content)

header_list = header.split()
print("list of header elements:")

value=file_content[4].split()[2]
print("value:", value)
print("type of value:", type(value))
print("value as floating point number:", float(value))
print("type of the rounded floating point value:", type(round(float(value))))