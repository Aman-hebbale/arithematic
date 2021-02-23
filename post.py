import subprocess as sb
sub=sb.Popen("shell_script.sh",shell=True,stdout=sb.PIPE,stderr=sb.PIPE)
sub.wait()
out,err=sub.communicate()
print(f'output is:{out}\n error is:{err}')