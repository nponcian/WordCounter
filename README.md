# WordCounter

## PURPOSE
Counts the number of occurrences of words within a file. If you're curious on what is the most used word in the essay that you have written, or maybe you are validating that a message doesn't contain some specific words, or you're trying to check the unique words present in a context, or perhaps you are job hunting and badly needs to know what requirements appears the most in multiple employers, then this application would help!

## REQUIREMENTS
1. Git
    ~~~
    sudo apt install git
    ~~~
2. GNU Toolchain (or just Python)
    ~~~
    sudo apt install build-essential
    ~~~

## RUNNING
1. Clone repo
    ```
    git clone https://github.com/nponcian/WordCounter.git
    cd WordCounter
    ```
2. Modify files in ./FilesToProcess directory
    a. ./FilesToProcess/Input.txt - the input file to count the number of occurrences of words
    b. ./FilesToProcess/WordsSeparators.txt - non-space separators that separates words in input file such as comma, slash, etc.
    c. ./FilesToProcess/WordsToCount.txt - if not empty, only the words here would be counted, otherwise all words are counted
    d. ./FilesToProcess/WordsToIgnore.txt - the words here would not be counted
3. Invoke script
    ```
    python3 wordcounter.py
    ```

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
