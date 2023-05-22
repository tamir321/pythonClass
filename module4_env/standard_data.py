import sys

sys.stdout.write("sys.stdout.write please write somthing \n")





line = sys.stdin.readline()[:-1]  #removes the \n from the end of the line
sys.stdout.write(line)



print("Example 1")
print("Example 2", file=sys.stderr)
sys.stderr.write("Example 3")


