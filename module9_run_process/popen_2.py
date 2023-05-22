import subprocess as SP

result = SP.Popen(["dir"], stdout=SP.PIPE, stderr=SP.PIPE, shell=True)
output, error = result.communicate()
print("result output", output)
print("result error", error)

result1 = SP.Popen(["nodir"], stdout=SP.PIPE, stderr=SP.PIPE, shell=True)
output, error = result1.communicate()
print("result1 output", output)
print("result1 error", error)
