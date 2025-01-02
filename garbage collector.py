import gc #garbage collector module
gc.enable()
gc.disable()

l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage Collection"
del l1
del d1
del s1
#gc.set_threshold(1,2,2)
print("Current Threshold",gc.get_threshold())
collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")
