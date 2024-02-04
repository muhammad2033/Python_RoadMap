import os , sys
# assuming /tmp/foo.text exists and has read/write permissions 

ret = os.access("/files_input_output/methods/chdir_method.txt",os.F_OK)
print("f_ok - return value %s"%(ret))

ret = os.access("/files_input_output/methods/chdir_method.txt",os.R_OK)
print("R_ok - return value %s"%(ret))

ret = os.access("/files_input_output/methods/chdir_method.txt",os.W_OK)
print("W_ok - return value %s"%(ret))

ret = os.access("//files_input_output/methods/chdir_method.txt",os.X_OK)
print("X_ok - return value %s"%(ret))
