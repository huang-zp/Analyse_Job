import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在known_hosts文件上的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
a = ssh.connect(hostname="139.199.184.43", port=22, username="root", password="huangzp123")
print(a)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls -l')
# 获取结果
result = stdout.read().decode()

# 获取错误提示（stdout、stderr只会输出其中一个）
err = stderr.read()
# 关闭连接
ssh.close()
result_lists = result.split('\n')
for result in result_lists[1:-1]:
    info = ' '.join(result.split())
    info_list = info.split(' ')
    print(info_list[3], info_list[4], info_list[-1])
