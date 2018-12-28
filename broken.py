# -*- coding: utf-8 -*-
import cmd

import os
import smtplib
import getpass
import sys
import time
from colorama import init, Style, Back, Fore

class program(cmd.Cmd):

    prompt = '\\'
    intro = """

    ▄█▄    ▄▄ █    ▄   ██     ▄▄▄▄▀ █▄▄▄▄ ████▄
    █▀ ▀▄ █   █     █  █ █ ▀▀▀ █    █  ▄▀ █   █
    █   ▀  ▀▀▀█  █   █ █▄▄█    █    █▀▀▌  █   █
    █▄  ▄▀    █  █   █ █  █   █     █  █  ▀████
    ▀███▀      █ █▄ ▄█    █  ▀        █
                ▀ ▀▀▀    █           ▀
                        ▀     by:r3g3n3r4
    [+] set/mail/check/run
    """

    #defines
    db = {
    'mail':'','password':'','sv':'','mailto':'','mailcontent':'',
    'mailtitle':'', 'setcmds': ['mail','sv','ps'], 'setsvmail': ['gmail','yahoo','hotmail','bol'],
    'mailcmds': ['target','content','title'], 'total':0
    }

    loading

i,n = 0,0
while 1:
    i += 1
    if i % 10 == 0:
        n += 1
    print("[+] Emails sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EMails sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmAils sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmaIls sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmaiLs sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmailS sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] Emails Sent %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmailS sEnt %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmailS seNt %s\r"%n, end="")
    time.sleep(.05)
    print("[+] EmailS senT %s\r"%n, end="")
    time.sleep(.1)
    print("[+] Emails sent %s\r"%n, end="")
    time.sleep(.1)
    print("[+] Emails sent %s\r"%n, end="")
    time.sleep(.1)


    mail = ''
    password = ''
    sv = ''
    mailto = ''
    mailcontent = ''
    mailtitle = ''
    total = 0

    #cmds
    setcmds = ['mail','sv','ps']
    setsvmail = ['gmail','yahoo','hotmail','bol']
    mailcmds = ['target','content','title', 'total']
    norun = 0;

    def do_set(self, arg):
        """set [option] [arg]\nConfigures the sender parameters"""

        arg = arg.split()
        if len(arg) == 0 or len(arg) == 1:
            print("#========================================#")
            print("[+] set mail \t<mail>")
            print("[+] set ps \t<password>")
            print("[+] set sv \t<gmail/yahoo>")
            print("#========================================#")
        elif arg[0] == self.setcmds[0]: #Mail
            self.db = arg[1].lower()
            print("Mail set to %.7s..."%self.mail)
        elif arg[0] == self.setcmds[2]: #SENHA
            self.password = arg[1]
            print("Password set %s."%("*"*len(self.password)))
        elif arg[0] == self.setcmds[1]: #SERVER
            if arg[1].lower() != 'gmail' and arg[1].lower != 'yahoo':
                print("Mail server not found. Please use gmail or yahoo input.")
            else:
                self.sv = arg[1].lower()
                print("Mail server set to %s."%self.sv)

    def complete_set(self, text, line, begidx, endidx):
        if not text:
            out = self.setcmds[:]
        else:
            out = [ f
                    for f in self.setcmds
                    if f.startswith(text)
                    ]
        return out

    #title can be random, or by a list
    def do_mail(self, arg):
        """mail [option] [arg]\nConfigures the mail parameters"""
        arg = arg.split()
        if len(arg) == 0 or len(arg) == 1:
            print("#========================================#")
            print("[+] mail target \t<mail>")
            print("[+] mail content \t<text>")
            print("[+] mail title \t\t<title/random>")
            print("[+] mail total \t\t<number>")
            print("#========================================#")
        elif arg[1]:
            if arg[0] == self.mailcmds[0]:
                self.mailto = arg[1]
                print("Email target was set to %.7s"%self.mailto)
            if arg[0] == self.mailcmds[1]:
                text = ''
                for i in range(len(arg)):
                    if(i):
                        text += (arg[i] + " ")
                    if(i == len(arg)):
                        text += (arg[i])
                self.mailcontent = text
                print("Content was set to %s"%self.mailcontent)
            if arg[0] == self.mailcmds[2]:
                self.mailtitle = arg[1]
                print("Email title was set to %.7s"%self.mailtitle)
            if arg[0] == self.mailcmds[3]:
                self.total = arg[1]
                print("The number os emails to send was set to %s"%self.total)
        else:
            print("[+] mail target <mail>")

    def complete_mail(self, text, line, begidx, endidx):
        if not text:
            out = self.mailcmds[:]
        else:
            out = [ f
                    for f in self.mailcmds
                    if f.startswith(text)
                    ]
        return out

    def do_check(self,line):
        if not line:
            print("#========================================#")
        if self.mail:
            if not line:
                print("[+] Mail from %s."%self.mail)
        else:
            if not line:
                print("[+] Mail from has not been set.")
            self.norun = 1;
        if self.password:
            if not line:
                print("[+] Password %s."%self.password)
        else:
            if not line:
                print("[+] Password has not been set.")
            self.norun = 1;
        if self.sv:
            if not line:
                print("[+] Mail server %s"%self.sv)
        else:
            if not line:
                print("[+] Mail server has not been set.")
            self.norun = 1;
        if self.mailto:
            if not line:
                print("[+] Mail target set to %s"%self.mailto)
        else:
            if not line:
                print("[+] Mail target has not been set.")
            self.norun = 1;
        if self.mailtitle:
            if not line:
                print("[+] Mail title set to %s"%self.mailtitle)
        else:
            if not line:
                print("[+] Mail title has not been set.")
            self.norun = 1;
        if self.mailcontent:
            if not line:
                print("[+] Mail content set to %.7s"%self.mailcontent)
        else:
            if not line:
                print("[+] Mail content has not been set.")
            self.norun = 1;
        if self.total:
            if not line:
                print("[+] Total of mails to send %s"%self.total)
        else:
            if not line:
                print("[+] Number of mails to send has not been set.")
            self.norun = 1;
        if not line:
            print("#========================================#")

    def do_run(self, arg):
        """run\nRuns the script to the target mail"""
        self.do_check(1)
        if(self.norun):
            print("[+] Missing parameters, do 'check' command to see what is missing.")
            self.norun = 0;
        else:
            if self.sv == 'gmail':
                smtp_server = 'smtp.gmail.com'
                port = 587

                try:
                    server = smtplib.SMTP(smtp_server,port)
                    server.ehlo()
                    if smtp_server == "smtp.gmail.com":
                            server.starttls() #segura
                    server.login(user,passwd)
                    for i in range(1, self.total+1):
                        if self.mailtitle.lower() == 'random':
                            subject = os.urandom(9)
                            msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
                            server.sendmail(user,to,msg)
                            print("[+] E-mails sent: %i\r" % i)
                            sys.stdout.flush()
                        else:
                            msg = 'From: ' + user + '\nSubject: ' + self.mailtitle + '\n' + body
                            server.sendmail(user,to,msg)
                            print("[+] E-mails sent: %i\r" % i)
                            sys.stdout.flush()
                    server.quit()
                    print('\n Finished')
                except KeyboardInterrupt:
                    print('[-] Canceled by KeyboardInterrupt')
                except smtplib.SMTPAuthenticationError:
                    print('\n[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps')
                except socket.gaierror:
                    print("[!] Error. Verify your internet connection and try again.")
                except NameError:
                    print("[!] Error. Verify your internet connection and try again.")

            else:
                print("[+] Missing parameters, do 'check' command to see what is missing")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    program().cmdloop()
