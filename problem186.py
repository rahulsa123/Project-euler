"""
2325629

real	0m28.372s
user	0m28.100s
sys	0m0.269s

"""

import sys

sys.setrecursionlimit(10**2)
from collections import deque

class Node:
	def __init__(self, id):
		self.id = id
		self.groupId = id
		self.count = 1

	def getGroupId(self,users):
		if self.groupId == self.id:
			return self.groupId
		self.groupId = users[self.groupId].getGroupId(users)
		return self.groupId



users = {x :Node(x) for x in range(10**6)}

temp = deque([(100003 - 200003*k + 300007*k**3)
			 %1000000 for k in range(1,56)])
recNr = 0
currcount = 0
while True:
	caller, called = temp.popleft(),temp.popleft()
	# add new
	nth = (caller + temp[29])%1000000
	n_1th = (called + temp[30])%1000000
	temp.append(nth)
	temp.append(n_1th)

	if caller == called:
		# misdialled
		continue
	recNr += 1

	# search caller groupid and called groupId
	callerGroupId = users[caller].getGroupId(users)
	# print(recNr,callerGroupId)
	calledGroupId = users[called].getGroupId(users)

	if callerGroupId!=calledGroupId:
		# merger called in caller

		# first add called count in caller
		users[callerGroupId].count += users[calledGroupId].count
		# second change group id of called
		users[calledGroupId].groupId = callerGroupId
		# set count of called to zero
		users[calledGroupId].count = 0
	# check PM groupId count ==990000 99%
	ans = users[users[524287].getGroupId(users)].count
	if  ans== 990000:
		print(recNr)
		break
