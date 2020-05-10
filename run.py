import os
#Problem uploadImage.py can't able to open camera after open from this.
#interface
print("choose a no(1,2,3,4)")
print("1.Upload Image")
print("2.train")
print("3.recognize and take attendence")
print("4.show attendence")
choice = int(input())

base_dir = os.path.dirname(os.path.abspath(__file__))
if choice == 1:
	path = os.path.join(base_dir, "uploadImage.py")
elif choice ==2:
	path = os.path.join(base_dir,"tranner.py")
elif choice == 3:
	path = os.path.join(base_dir,"showAttendence.py")

#run module
os.system(path)