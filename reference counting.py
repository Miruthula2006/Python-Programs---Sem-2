#tracks the number of references pointing to it
import sys
a=[1,2,3]#ref_count=2
b=a#ref_count=2+1=3
c=a#ref_count=3+1=4
ref_count=sys.getrefcount(a)
print("Reference count is",ref_count)
