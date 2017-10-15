from pwn import *

def rot(cipherText):
	strl = "abcdefghijklmnopqrstuvwxyz"
	stru = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	temp = []
	rot = 13
	print cipherText
	for i in cipherText:
		if i.isdigit():
			temp.append(i)
		elif i.isupper():
			temp.append(stru[(stru.index(i)+rot)%26])
		elif i.islower():
			temp.append(strl[(strl.index(i)+rot)%26])
	ans = ''.join(temp)
	return ans


conn = remote('irc.root-me.org',6667)

name = "SnowNeko9"
bot  = "candy"

print conn.recvuntil('instead.')
conn.send('NICK {0}\r\n'.format(name))
conn.send('USER {0} irc.root-me.org root-me :ChallengeBot\r\n'.format(name))
conn.send('JOIN #root-me_challenge')

print conn.recvuntil('MODE {0}'.format(name))


conn.send('PRIVMSG {0}\r\n'.format(bot))
print conn.recvuntil('End of /NAMES list.')

sleep(1)

conn.send('PRIVMSG {0} :!ep3\r\n'.format(bot))
print conn.recvline() #1 blank line

rev=conn.recvline()
cal = rev.replace(':','/').replace(' ','').replace('\r\n','').split('/')

conn.send('PRIVMSG {0} :!ep3 -rep {1}\r\n'.format( bot ,str(rot(cal[2])) ) )

print conn.recvline()




