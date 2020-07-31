#!/bin/env python3

import re
import random
import os
import sys
import parsegrammar as gram
import pexpectparser as pp
import authReader as aRead

def getFileList(rootDir, pattern):
    return [os.path.join(r,filename) for r, _, f in os.walk(rootDir) for filename in f if re.search(pattern, filename) != None ]

def createParseGraph(vpnCommand, endSymbol, authfile):
    authList = aRead.readAuthFromFile(authfile, 2)
    sudoAuth = authList[0]
    vpnAuth = authList[1]
    username = vpnAuth.getUser()
    password = vpnAuth.getPassword()
    userPrompt = "Enter Auth Username: "
    passPrompt = "Enter Auth Password"
    graph = gram.Graph()
    graph.addEdge(vpnCommand, f"{sudoAuth.getUser()}: $", sudoAuth.getPassword())
    graph.addEdge(sudoAuth.getPassword(), userPrompt, username)
    graph.addEdge(username, passPrompt, password)
    graph.addEdge(username, passPrompt, password)
    graph.addEdge(password, 'Initialization Sequence Completed', endSymbol)
    graph.addEdge(password, 'AUTH FAILED', endSymbol)
    return graph

def getVpnFile(rootDir):
    fileList = getFileList(rootDir, 'ovpn$')
    random.seed()
    index = random.randrange(len(fileList))
    return fileList[index]

def createParserGrammar(endSymbol, authfile):
    vpnFlavour = "sudo openvpn"
    vpnFile = getVpnFile("./config")
    vpnCommand = f'{vpnFlavour} {vpnFile}'
    pgraph = createParseGraph(vpnCommand, endSymbol, authfile)
    pGrammar = gram.Grammar(vpnCommand, endSymbol, pgraph)
    return pp.Parser(pGrammar)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough arguments.")
        print("Provide the credentials file location as argument")
    else:
        authfile = sys.argv[1]
        parser = createParserGrammar("###END###", authfile)
        try:
            child = parser.run()
        except Exception as e:
            child.close()
            print(e.message)
        else:
            print("VPN Connected")
            child.interact()
