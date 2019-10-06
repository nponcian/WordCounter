# WordCounter

## SAMPLE RUN
```
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ echo "" | cat FilesToProcess/WordsSeparators.txt -
!&()=|\{}[]:;"'<>,.?/
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ echo "" | cat FilesToProcess/WordsToCount.txt -

nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ echo "" | cat FilesToProcess/WordsToIgnore.txt -
the
a
in
on
at
and
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ echo "" | cat FilesToProcess/Input.txt -
Company-A

Requirements:
C, C++, Java, Python
analytic / trouble-shooting and debugging skills
TCP, UDP, IP, HTTP, L4-L7, DNS, SSL, tunneling, SIP, Diameter
Linux and OS internals
leadership



Company-B

Requirements:
Percona XtraDB Cluster, Elasticsearch, Cassandra
Hazelcast
Kafka
AngularJS, React
C++, Golang, Python
Android SDK, React Native
Kubernetes (Docker)
Tcp/Ip, http
Linux



Company-C

Requirements:
Python, c++
TCP /IP
Linux

nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ python3 wordcounter.py 
requirements : 3
c++ : 3
python : 3
tcp : 3
ip : 3
linux : 3
http : 2
react : 2
company-a : 1
c : 1
java : 1
analytic : 1
trouble-shooting : 1
debugging : 1
skills : 1
udp : 1
l4-l7 : 1
dns : 1
ssl : 1
tunneling : 1
sip : 1
diameter : 1
os : 1
internals : 1
leadership : 1
company-b : 1
percona : 1
xtradb : 1
cluster : 1
elasticsearch : 1
cassandra : 1
hazelcast : 1
kafka : 1
angularjs : 1
golang : 1
android : 1
sdk : 1
native : 1
kubernetes : 1
docker : 1
company-c : 1
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ cat >> FilesToProcess/WordsToCount.txt # add target words
c
c++
python
linux
docker
http
golang
^C
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ cat FilesToProcess/WordsToCount.txt 
c
c++
python
linux
docker
http
golang
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$ python3 wordcounter.py 
c++ : 3
python : 3
linux : 3
http : 2
c : 1
golang : 1
docker : 1
nponcian@nponcian-VirtualBox-Ubuntu:~/Documents/Scripts/WordCounter$
```
