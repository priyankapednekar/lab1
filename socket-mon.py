#!usr/bin/env python


#Author:Priyanka pednekar
#lab1 assigment

import socket
import psutil
from operator import itemgetter
from collections import Counter

def main():

	print("\"pid\",\"laddr\",\"raddr\",\"status\"")
	

	def qoute(val):
		var='"'
		return var+val+var

	def data(pid_val):
		for conn in psutil.net_connections(kind='tcp'):
			if conn.pid == pid_val:
				try:
					if conn.raddr and conn.laddr:
						local_addr = "%s@%s" % (conn.laddr)
						remote_addr ="%s@%s" % (conn.raddr)
						print qoute(str(conn.pid)),qoute(str(local_addr)) or " ",qoute(str(remote_addr)) or " ",qoute(str(conn.status))
				except psutil.NoSuchProcess:
					pass
			
	 
	    			
	#print in sorted order
	conn = psutil.net_connections()
	x = Counter(elem[6] for elem in conn)

	for i in sorted(x.items(), key=itemgetter(1), reverse=True ):
		data(i[0])

	


if __name__ == '__main__':
	main()
