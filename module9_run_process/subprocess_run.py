import subprocess



result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)

print("result-",result.stdout)
print("*~"*20)



result = subprocess.run(["python", r"C:\Users\tamir\Documents\pythonProject\main2.py"], capture_output=True, text=True)

print("python result" ,result.stdout)