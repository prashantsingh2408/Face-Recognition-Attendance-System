import os
#Problem uploadImage.py can't able to open camera after open from this.
#interface
while True:
	print("choose a no(1,2,3,4)")
	print("1.Upload Image(Registration)")
	print("2.train")
	print("3.recognize and take attendence")
	print("4.show attendence")
	choice = int(input())

	base_dir = os.path.dirname(os.path.abspath(__file__))
	os.chdir(base_dir)
	if choice == 1:
		os.system('python uploadImage.py')
	elif choice ==2:
		os.system('python trainner.py')
	elif choice == 3:
		os.system('python recognize.py')
	elif choice == 4:
		os.system('python showAttendence.py')

	if 'y' == input("want to exit(y/n)"):
		break

