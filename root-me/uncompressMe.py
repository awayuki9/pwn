from pwn import *
import zlib
import base64


conn = remote('irc.root-me.org',6667)

name = "SnowNeko9"
bot  = "candy"
level = 4

print conn.recvuntil('instead.')
conn.send('NICK {0}\r\n'.format(name))
conn.send('USER {0} irc.root-me.org root-me :ChallengeBot\r\n'.format(name))
conn.send('JOIN #root-me_challenge')

print conn.recvuntil('MODE {0}'.format(name))


conn.send('PRIVMSG {0}\r\n'.format(bot))
print conn.recvuntil('End of /NAMES list.')

sleep(1)

conn.send('PRIVMSG {0} :!ep{1}\r\n'.format(bot,level))
print conn.recvline() #1 blank line

rev=conn.recvline()
cal = rev.replace(':','/').replace(' ','').replace('\r\n','').split('/')
print cal[2]
deComp = zlib.decompress(str(base64.b64decode(str(cal[2]))))
print deComp
conn.send('PRIVMSG {0} :!ep{1} -rep {2}\r\n'.format( bot ,level ,deComp) )

print conn.recvline()




