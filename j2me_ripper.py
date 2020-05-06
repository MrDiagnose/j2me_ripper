print("\n==========j2me_ripper(beta)============\n")
jar_header=b'\x50\x4b\x03\x04'
midlet_jar_size_header=b'\x4d\x49\x44\x6c\x65\x74\x2d\x4a\x61\x72\x2d\x53\x69\x7a\x65\x3a\x20'
size=''

num=1
firmwarefile=input("Please enter filename then press enter: ")
file1=open(firmwarefile,'rb')
s=file1.read()
index1=0
for i in s:
    index2=s.find(midlet_jar_size_header,index1)
    print('File handle is at index:'+hex(index2))
    try:
        file1.seek(index2)
    except OSError:
        break
    for j in range(17):
        a=file1.read(1)
        size=size+a.decode("utf-8") #convert bytes to string
    a=b'' #empty byte variable
    jarsize=''
    while (a!=b'\x0d') and (a!=b'\x0a'):
        a=file1.read(1)
        jarsize=jarsize+a.decode("utf-8")
    print(size+jarsize)
    print('File handle is at index:' +hex(file1.tell()))
    jar_header_index=s.find(jar_header,file1.tell())
    print(hex(jar_header_index))
    file1.seek(jar_header_index)
    print('File handle is at index:' +hex(file1.tell()))
    c=b''
    for i in range(int(jarsize)+1):
        c=c+file1.read(1)
    file2=open('output'+str(num)+'.jar','wb')
    file2.write(c)
    file2.close()
    num=num+1
    index1=file1.tell()
    print("completed")
file1.close()
