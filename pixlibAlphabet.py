from pixlib import pixlibObject
from legacySubroutines import legacyUpdatePixel

class pixlibChar(pixlibObject):
    def __init__(self, achar, aposition, acolour):
        self.colour = acolour
        super().__init__(aposition, 7, 4)
        self.char = achar
        self.visualStates = {
            'A': [
                [[1,None],[2,self.colour],[1,None]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[4,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]]
            ],
            'B': [
                [[3,self.colour],[1,None]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[3,self.colour],[1,None]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[3,self.colour],[1,None]]
            ],
            'C': [
                [[1,None],[3,self.colour]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[1,None],[3,self.colour]]
            ],
            'D': [
                [[3,self.colour],[1,None]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[1,self.colour],[2,None],[1,self.colour]],
                [[3,self.colour],[1,None]]
            ],
            'E': [
                [[4,self.colour]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[4,self.colour]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[4,self.colour]]
            ],
            'F': [
                [[4,self.colour]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[4,self.colour]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]],
                [[1,self.colour],[3,None]]
            ]
        }
        self.currentState = str(achar)



def about(specific = ''):
    if specific == '':
        print("""This library aims to replicate this font: http://www.onextrapixel.com/wp-content/uploads/2013/04/munro.jpg
        Characters will therefore have a standard width of 4 pixels, however some symbols and lower case characters may diverge from this.
        Characters will also have a standard height of 7 pixels, although some symbols may exceed this. A recommended spacing between lines of text is 
        """)
    elif specific == 'help':
        print("""List of 'Help' Functions
            - About This Library: ''
            - Help: Well you're already here dummy
            - List of Edge Cases: 'edge cases'""")

#charWidths = {'A': 4,'B': 4,'C': 3,'D': 4,'E': 3,'F': 3,'G': 4,'H': 4,'I': 3,'J': 4,'K': 4,'L': 3,'M': 5,'N': 4,'O': 4,'P': 4,'Q': 4,'R': 4,'S': 3,'T': 3,'U': 4,'V': 5,'W': 5,'X': X,'Y': Y,'Z': Zthree,'Z3': Zthree,'Z5': Zfive,
#        #Letters (Lower Case)
#        'a': a,'b': b,'c': c,'d': d,'e': e,'f': f,'g': g,'h': h,'i': i,'j': j,'k': k,'l': l,'m': m,'n': n,'o': o,'p': p,'q': q,'r': r,'s': s,'t': t,'u': u,'v': v,'w': w,'x': x,'y': y,'z': z,
#        #Numbers
#        '0': O,'zero': O,'1': one,'one': one,'2': two,'two': two,'3': three,'three': three,'4': four,'four': four,'4diag': fourDiag,'fourdiag': fourDiag,'5': five,'five': five,'6': six,'six': six,'7': seven,'seven': seven,'8': eight,'eight': eight,'9': nine,'nine': nine,}

def drawChar(char,screen,pixels,colour,initpos):
    supportedChars = {
        #Letters (Capital)
        'A': A,'B': B,'C': C,'D': D,'E': E,'F': F,'G': G,'H': H,'I': I,'J': J,'K': K,'L': L,'M': M,'N': N,'O': O,'P': P,'Q': Q,'R': R,'S': S,'T': T,'U': U,'V': V,'W': W,'X': X,'Y': Y,'Z': Zthree,'Z3': Zthree,'Z5': Zfive,
        #Letters (Lower Case)
        'a': a,'b': b,'c': c,'d': d,'e': e,'f': f,'g': g,'h': h,'i': i,'j': j,'k': k,'l': l,'m': m,'n': n,'o': o,'p': p,'q': q,'r': r,'s': s,'t': t,'u': u,'v': v,'w': w,'x': x,'y': y,'z': z,
        #Numbers
        '0': O,'zero': O,'1': one,'one': one,'2': two,'two': two,'3': three,'three': three,'4': four,'four': four,'4diag': fourDiag,'fourdiag': fourDiag,'5': five,'five': five,'6': six,'six': six,'7': seven,'seven': seven,'8': eight,'eight': eight,'9': nine,'nine': nine,
        #Symbols
    }


    for key in supportedChars:
        if key == char:
            supportedChars[key](screen,pixels,initpos[0],initpos[1],colour)
            charFound = True
    if charFound == False:
        raise ValueError('This character does not have a method, you may have to code this method yourself.')
    
def A(screen,pixels,initialx,initialy,colour):    
    for i in range(1,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+3],colour)

def B(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+1],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+5],colour)

def C(screen,pixels,initialx,initialy,colour):
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)

def D(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+6],colour)

def E(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)

def F(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)

def G(screen,pixels,initialx,initialy,colour):   
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+5],colour)

def H(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)

def I(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx+1][initialy+i],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)

def J(screen,pixels,initialx,initialy,colour):
    for i in range(0,6):
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i],colour)
    for i in range(0,4):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+5],colour)

def K(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+0],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+1],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+5],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+6],colour)

def L(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+6],colour)

def M(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+4][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+2],colour)

def N(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+3],colour)

def O(screen,pixels,initialx,initialy,colour):
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+6],colour)

def P(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)

def Q(screen,pixels,initialx,initialy,colour):
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,5):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+5],colour)

def R(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+1],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+5],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+6],colour)

def S(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+1],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+5],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+3],colour)

def T(screen,pixels,initialx,initialy,colour):
    for i in range(1,7):
        legacyUpdatePixel(screen,pixels[initialx+1][initialy+i],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)

def U(screen,pixels,initialx,initialy,colour):
    for i in range(0,6):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)

def V(screen,pixels,initialx,initialy,colour):
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+4][initialy+i],colour)
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+1][initialy+i+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i+5],colour)

def W(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+4][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+4],colour)

def X(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+4][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+5],colour)
        legacyUpdatePixel(screen,pixels[initialx+4][initialy+i+5],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+4],colour)

def Y(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+4][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+3][initialy+2],colour)
    for i in range(3,7):
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i],colour)

def Zthree(screen,pixels,initialx,initialy,colour):
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+1],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+5],colour)

def Zfive(screen,pixels,initialx,initialy,colour):
    for i in range(0,5):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
    for i in range(0,5):
        legacyUpdatePixel(screen,pixels[initialx+4-i][initialy+i+1],colour)

def a(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+2],colour)
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+4],colour)
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+5],colour)
    for i in range(3,7):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)

def b(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+2],colour)
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+6],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i+3],colour)

def c(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+2],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+6],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+3],colour)

def d(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+2],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+6],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+3],colour)
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)

def e(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+2],colour)
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+4],colour)
        legacyUpdatePixel(screen,pixels[initialx+1+i][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i+3],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+3],colour)

def f(screen,pixels,initialx,initialy,colour):
    for i in range(1,7):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
    for i in range(1,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+2],colour)

def g():
    pass

def h():
    pass

def i():
    pass

def j():
    pass

def k():
    pass

def l():
    pass

def m():
    pass

def n():
    pass

def o():
    pass

def p():
    pass

def q():
    pass

def r():
    pass

def s():
    pass

def t():
    pass

def u():
    pass

def v():
    pass

def w():
    pass

def x():
    pass

def y():
    pass

def z():
    pass

def one(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx+1][initialy+i],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+1],colour)

def two(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+1+i],colour)
        legacyUpdatePixel(screen,pixels[initialx][initialy+4+i],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+3],colour)

def three(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i+1],colour)
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i+4],colour)

def four(screen,pixels,initialx,initialy,colour):
    for i in range(0,5):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i+2],colour)
    for i in range(1,4):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+4],colour)

def fourDiag(screen,pixels,initialx,initialy,colour):
    for i in range(0,7):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)
    for i in range(0,5):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+4],colour)
    legacyUpdatePixel(screen,pixels[initialx][initialy+3],colour)
    legacyUpdatePixel(screen,pixels[initialx+1][initialy+2],colour)
    legacyUpdatePixel(screen,pixels[initialx+2][initialy+1],colour)

def five(screen,pixels,initialx,initialy,colour):
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx][initialy+1+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+i+4],colour)

def six(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i+4],colour)
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx][initialy+i],colour)

def seven(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+2][initialy+1+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+1][initialy+3+i],colour)
        legacyUpdatePixel(screen,pixels[initialx+0][initialy+5+i],colour)
    for i in range(0,3):
        legacyUpdatePixel(screen,pixels[initialx+i][initialy],colour)

def eight(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i+1],colour)
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i+4],colour)
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+1],colour)
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+4],colour)

def nine(screen,pixels,initialx,initialy,colour):
    for i in range(0,2):
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+3],colour)
        legacyUpdatePixel(screen,pixels[initialx+i+1][initialy+6],colour)
        legacyUpdatePixel(screen,pixels[initialx][initialy+i+1],colour)
    for i in range(1,6):
        legacyUpdatePixel(screen,pixels[initialx+3][initialy+i],colour)

def debugDRAWALL(screen,pixels,colour):
    drawChar('A',screen,pixels,colour,[0,0])
    drawChar('B',screen,pixels,colour,[5,0])
    drawChar('C',screen,pixels,colour,[10,0])
    drawChar('D',screen,pixels,colour,[14,0])
    drawChar('E',screen,pixels,colour,[19,0])
    drawChar('F',screen,pixels,colour,[23,0])
    drawChar('G',screen,pixels,colour,[27,0])
    drawChar('H',screen,pixels,colour,[32,0])
    drawChar('I',screen,pixels,colour,[37,0])
    drawChar('J',screen,pixels,colour,[41,0])
    drawChar('K',screen,pixels,colour,[46,0])
    drawChar('L',screen,pixels,colour,[51,0])
    drawChar('M',screen,pixels,colour,[55,0])
    drawChar('N',screen,pixels,colour,[61,0])
    drawChar('O',screen,pixels,colour,[66,0])
    drawChar('P',screen,pixels,colour,[71,0])
    drawChar('Q',screen,pixels,colour,[76,0])
    drawChar('R',screen,pixels,colour,[81,0])
    drawChar('S',screen,pixels,colour,[86,0])
    drawChar('T',screen,pixels,colour,[90,0])
    drawChar('U',screen,pixels,colour,[94,0])
    drawChar('W',screen,pixels,colour,[0,8])
    drawChar('X',screen,pixels,colour,[6,8])
    drawChar('Y',screen,pixels,colour,[12,8])
    drawChar('Z',screen,pixels,colour,[18,8])
    drawChar('Z5',screen,pixels,colour,[22,8])
    drawChar('1',screen,pixels,colour,[0,16])
    drawChar('2',screen,pixels,colour,[3,16])
    drawChar('3',screen,pixels,colour,[7,16])
    drawChar('4',screen,pixels,colour,[11,16])
    drawChar('4diag',screen,pixels,colour,[16,16])
    drawChar('5',screen,pixels,colour,[22,16])
    drawChar('6',screen,pixels,colour,[26,16])
    drawChar('7',screen,pixels,colour,[31,16])
    drawChar('8',screen,pixels,colour,[35,16])
    drawChar('9',screen,pixels,colour,[40,16])
    drawChar('0',screen,pixels,colour,[45,16])
