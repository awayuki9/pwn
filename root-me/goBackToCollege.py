from pwn import *



conn = remote('irc.root-me.org',6667)

name = "SnowNeko9"
bot  = "candy"

print conn.recvuntil('instead.')
print 'send NICK'
conn.send('NICK {0}\r\n'.format(name))
print 'send USER'
conn.send('USER Awayuki * * :ChallengeBot\r\n') #'USER {0} irc.root-me.org root-me :ChallengeBot\r\n'
conn.send('JOIN #root-me_challenge')

print conn.recvuntil('MODE {0}'.format(name))


conn.send('PRIVMSG {0}\r\n'.format(bot))
print conn.recvuntil('End of /NAMES list.')

sleep(1)

conn.send('PRIVMSG {0} :!ep1\r\n'.format(bot))
print conn.recvline() #1 blank line

rev=conn.recvline()
cal = rev.replace(':','/').replace(' ','').replace('\r\n','').split('/')
ans = round(math.sqrt(int(cal[2])) * int(cal[3]),2)
conn.send('PRIVMSG {0} :!ep1 -rep {1}\r\n'.format( bot ,str(ans).encode("ASCII") ) )

print conn.recvline()


while(True):
	rev=conn.recvline()
	print rev
	cal = rev.replace(':','/').replace(' ','').replace('\r\n','').split('/')
	print cal
	if cal[0]=='PING':
		print 'Send PONG'
		conn.send('PONG\r\n')
		






