
# Import pygame knihovny
import pygame
pygame.init()

# Define colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
BROWN = ( 150, 75, 0)

# Nové okno
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")



#Základ 31pix od okraje

#Black Pieces (Z prava do leva)
Brx1=31
Bry1=31
Bnx1=97
Bny1=31
Bbx1=163
Bby1=31
Bqx=229
Bqy=31
Bkx=296
Bky=31
Bbx2=362
Bby2=31
Bnx2=428
Bny2=31
Brx2=494
Bry2=31

#Black Pawns

Bpx1=31
Bpy1=97
Bpx2=97
Bpy2=97
Bpx3=163
Bpy3=97
Bpx4=229
Bpy4=97
Bpx5=296
Bpy5=97
Bpx6=362
Bpy6=97
Bpx7=428
Bpy7=97
Bpx8=494
Bpy8=97

#White Pieces

Wrx1=31
Wry1=493
Wnx1=97
Wny1=493
Wbx1=163
Wby1=493
Wqx=229
Wqy=493
Wkx=296
Wky=493
Wbx2=362
Wby2=493
Wnx2=428
Wny2=493
Wrx2=494
Wry2=493

#White Pawns

Wpx1=31
Wpy1=427
Wpx2=97
Wpy2=427
Wpx3=163
Wpy3=427
Wpx4=229
Wpy4=427
Wpx5=296
Wpy5=427
Wpx6=362
Wpy6=427
Wpx7=428
Wpy7=427
Wpx8=494
Wpy8=427
############################
sq1=31
posun=66

class Board():


   def __init__(self):
        self.turn="white"

        self.brook1=Rook(sq1,sq1, "black")
        self.bknight1=Knight(sq1+posun, sq1, "black")
        self.bbishop1=Bishop(sq1+(2*posun), sq1, "black")
        self.bqueen=Queen(sq1+(3*posun), sq1, "black")
        self.bking=King(sq1+(4*posun), sq1, "black")
        self.bbishop2=Bishop(sq1+(5*posun), sq1, "black")
        self.bknight2=Knight(sq1+(6*posun), sq1, "black")
        self.brook2=Rook(sq1+(7*posun), sq1, "black")

        self.bpawn1=Pawn(sq1,sq1+posun, "black")
        self.bpawn2=Pawn(sq1+posun,sq1+posun, "black")
        self.bpawn3=Pawn(sq1+(2*posun),sq1+posun, "black")
        self.bpawn4=Pawn(sq1+(3*posun),sq1+posun, "black")
        self.bpawn5=Pawn(sq1+(4*posun),sq1+posun, "black")
        self.bpawn6=Pawn(sq1+(5*posun),sq1+posun, "black")
        self.bpawn7=Pawn(sq1+(6*posun),sq1+posun, "black")
        self.bpawn8=Pawn(sq1+(7*posun),sq1+posun, "black")

        self.wpawn1=Pawn(sq1,sq1+(6*posun), "white")
        self.wpawn2=Pawn(sq1+posun,sq1+(6*posun), "white")
        self.wpawn3=Pawn(sq1+(2*posun),sq1+(6*posun), "white")
        self.wpawn4=Pawn(sq1+(3*posun),sq1+(6*posun), "white")
        self.wpawn5=Pawn(sq1+(4*posun),sq1+(6*posun), "white")
        self.wpawn6=Pawn(sq1+(5*posun),sq1+(6*posun), "white")
        self.wpawn7=Pawn(sq1+(6*posun),sq1+(6*posun), "white")
        self.wpawn8=Pawn(sq1+(7*posun),sq1+(6*posun), "white")

        self.wrook1=Rook(sq1,sq1+(7*posun), "white")
        self.wknight1=Knight(sq1+posun,sq1+(7*posun), "white")
        self.wbishop1=Bishop(sq1+(2*posun),sq1+(7*posun), "white")
        self.wqueen=Queen(sq1+(3*posun),sq1+(7*posun), "white")
        self.wking=King(sq1+(4*posun),sq1+(7*posun), "white")
        self.wbishop2=Bishop(sq1+(5*posun),sq1+(7*posun), "white")
        self.wknight2=Knight(sq1+(6*posun),sq1+(7*posun), "white")
        self.wrook2=Rook(sq1+(7*posun),sq1+(7*posun), "white")

        self.bord=[self.brook1, self.bknight1, self.bbishop1, self.bqueen, self.bking, self.bbishop2, self.bknight2, self.brook2,
             self.bpawn1, self.bpawn2, self.bpawn3, self.bpawn4, self.bpawn5, self.bpawn6, self.bpawn7, self.bpawn8,
             "",       "",     "",     "",     "",     "",     "",     "",
             "",       "",     "",     "",     "",     "",     "",     "",
             "",       "",     "",     "",     "",     "",     "",     "",
             "",       "",     "",     "",     "",     "",     "",     "",
             self.wpawn1, self.wpawn2, self.wpawn3, self.wpawn4, self.wpawn5, self.wpawn6, self.wpawn7, self.wpawn8,
             self.wrook1, self.wknight1, self.wbishop1, self.wqueen, self.wking, self.wbishop2, self.wknight2, self.wrook2]

        i=0
        for piece in self.bord:
           if piece!="":
              piece.SettBoardPosition(i)
              piece.SetMove(self.ReturnPieceIndexs())
              i+=1
           else:
              i+=1
   def GetOznacenyPiece(self):
       for Piece in self.bord:
           if Piece!="":

               if Piece.oznacen==True:
                   Piece.oznacen=False
                   return Piece




   def ChangeBordPosition(self, piece, newpos):

       pos=piece.index
       self.bord[newpos]=piece
       self.bord[pos]=""

   def IsDisPieceStillOnBoard(self, piiis):
       count=0
       for Piece in self.bord:
            if Piece==piiis:
                count=1
       if count==0:
           return False
       else:
           return True

   def ReturnPieceIndexs(self):
       Indexs={}
       count=-1
       for Piece in self.bord:
           count+=1
           if Piece!="":
               Indexs[count]=Piece.color
       return Indexs





   def GetClick(self):
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self.pos=pygame.mouse.get_pos()
                Xpos=((self.pos[0]+sq1)//posun)-1
                Ypos=((self.pos[1]+sq1)//posun)-1

                for i in range(8):
                    if Ypos==i:
                        Index=Xpos+Ypos+(7*i)
                        DisPiece=self.WotIsDisPiece(Index)

                        #if self.turn==DisPiece.color:
                        if DisPiece and self.turn==DisPiece.color:
                            DisPiece.Oznacit(True)
                            DisPiece.SetMove(self.ReturnPieceIndexs())
                        else:
                            OznacenyPiece=self.GetOznacenyPiece()

                            if OznacenyPiece!=None:
                                if Index in OznacenyPiece.movesquare:
                                    self.ChangeBordPosition(OznacenyPiece, Index)
                                    OznacenyPiece.SettBoardPosition(Index)
                                    OznacenyPiece.SetXY(Xpos*66+31, Ypos*66+31)
                                    if isinstance(OznacenyPiece, Pawn):
                                        OznacenyPiece.hasmoved=True
                                    OznacenyPiece.SetMove(self.ReturnPieceIndexs())
                                    if self.turn=="white":
                                        self.turn="black"
                                    else:
                                        self.turn="white"




   def WotIsDisPiece(self, index):
           return self.bord[index]

   def DrawPiece(self, piiis):
       if self.IsDisPieceStillOnBoard(piiis)==True:
           piiis.Draw()

   def WotColorIsDisPiece(self, index):
       return self.WotIsDisPiece(index).color





   def DrawPieces(self):

        self.DrawPiece(self.bpawn1)
        self.DrawPiece(self.bpawn2)
        self.DrawPiece(self.bpawn3)
        self.DrawPiece(self.bpawn4)
        self.DrawPiece(self.bpawn5)
        self.DrawPiece(self.bpawn6)
        self.DrawPiece(self.bpawn7)
        self.DrawPiece(self.bpawn8)


        self.DrawPiece(self.brook1)
        self.DrawPiece(self.bknight1)
        self.DrawPiece(self.bbishop1)
        self.DrawPiece(self.bking)
        self.DrawPiece(self.bqueen)
        self.DrawPiece(self.bbishop2)
        self.DrawPiece(self.bknight2)
        self.DrawPiece(self.brook2)

        self.DrawPiece(self.wpawn1)
        self.DrawPiece(self.wpawn2)
        self.DrawPiece(self.wpawn3)
        self.DrawPiece(self.wpawn4)
        self.DrawPiece(self.wpawn5)
        self.DrawPiece(self.wpawn6)
        self.DrawPiece(self.wpawn7)
        self.DrawPiece(self.wpawn8)


        self.DrawPiece(self.wrook1)
        self.DrawPiece(self.wknight1)
        self.DrawPiece(self.wbishop1)
        self.DrawPiece(self.wking)
        self.DrawPiece(self.wqueen)
        self.DrawPiece(self.wbishop2)
        self.DrawPiece(self.wknight2)
        self.DrawPiece(self.wrook2)


class Piece(Board):

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.movesquare=[]
        self.oznacen=False

    def Oznacit(self, oznacen):
        self.oznacen=oznacen

    def SettBoardPosition(self, index):
        self.index=index

    def SetXY(self, newX, newY):
        self.X=newX
        self.Y=newY






        #def Move():

class Player(Piece):
    color=""
    def __init__(self, X, Y, color):
        super().__init__(X, Y)
        self.color=color

class Pawn(Player): # Třída "Pawn" která je podtřídou třídy "Player"
    def __init__(self, X, Y, color): # konstruktor
        super().__init__(X, Y, color)
        self.hasmoved=False


    def Draw(self):
        if self.color=="black":
            pawn = pygame.image.load('Bp.png')
            screen.blit(pawn, (self.X ,self.Y))

        elif self.color=="white":
            pawn = pygame.image.load('Wp.png')
            screen.blit(pawn, (self.X ,self.Y))

    def SetMove(self, Indexs):
        self.movesquare=[]

        if self.color=="black":
            if self.index+7 in Indexs and Indexs[self.index+7]!=self.color:
                self.movesquare.append(self.index+7)
            if self.index+9 in Indexs and Indexs[self.index+9]!=self.color:
                self.movesquare.append(self.index+9)
            if self.hasmoved==False:
                if self.index+16 not in Indexs and self.index+8 not in Indexs:

                    self.movesquare.append(self.index+16)
                    self.movesquare.append(self.index+8)
                if self.index+16 in Indexs and self.index+8 not in Indexs:
                    self.movesquare.append(self.index+8)
            else:
                if self.index+8 not in Indexs:
                    self.movesquare.append(self.index+8)
        else:
            if self.index-7 in Indexs and Indexs[self.index-7]!=self.color:
                self.movesquare.append(self.index-7)
            if self.index-9 in Indexs and Indexs[self.index-9]!=self.color:
                self.movesquare.append(self.index-9)
            if self.hasmoved==False:
                if self.index-16 not in Indexs and self.index-8 not in Indexs:

                    self.movesquare.append(self.index-16)
                    self.movesquare.append(self.index-8)
                if self.index-16 in Indexs and self.index-8 not in Indexs:
                    self.movesquare.append(self.index-8)
            else:
                if self.index-8 not in Indexs:
                    self.movesquare.append(self.index-8)


class Bishop(Player):
    def __init__(self, X, Y, color):
        super().__init__(X, Y, color)
        self.bigbadsquaresleft=[0, 8, 16, 24, 32, 40, 48, 56]
        self.bigbadsquaresright=[7, 15, 23, 31, 39, 47, 55, 63]

    def Draw(self):

        if self.color=="black":
            bishop = pygame.image.load('Bb.png')
            screen.blit(bishop, (self.X ,self.Y))

        elif self.color=="white":
            bishop = pygame.image.load('Wb.png')
            screen.blit(bishop, (self.X ,self.Y))

    def SetMove(self, Indexs):
        self.movesquare=[] #7 a 9
        print(Indexs)
        for i in range(8):
            i+=1
            if self.index+(i*(-9))>=0:
                if self.index in self.bigbadsquaresleft:
                    break
                if self.index+i*(-9) in Indexs:
                    if Indexs[self.index+i*(-9)]!=self.color:
                        self.movesquare.append(self.index+(i*(-9)))
                        break
                    else:
                        break
                if self.index+i*(-9) in self.bigbadsquaresleft:
                    self.movesquare.append(self.index+(i*(-9)))
                    break
                self.movesquare.append(self.index+(i*(-9)))
        for x in range(8):
            x+=1
            if self.index+(x*(-7))>=0:
                if self.index in self.bigbadsquaresright:
                    break
                if self.index+x*(-7) in Indexs:
                    if Indexs[self.index+x*(-7)]!=self.color:
                        self.movesquare.append(self.index+(x*(-7)))
                        break
                    else:
                        break
                if self.index+x*(-7) in self.bigbadsquaresright:
                    self.movesquare.append(self.index+(x*(-7)))
                    break
                self.movesquare.append(self.index+(x*(-7)))
        for y in range(8):
            y+=1
            if self.index+(y*(+7))<=63:
                if self.index in self.bigbadsquaresleft:
                    break
                if self.index+y*(+7) in Indexs:
                    if Indexs[self.index+y*(+7)]!=self.color:
                        self.movesquare.append(self.index+(y*(+7)))
                        break
                    else:
                        break
                if self.index+y*(+7) in self.bigbadsquaresleft:
                    self.movesquare.append(self.index+(y*(+7)))
                    break
                self.movesquare.append(self.index+(y*(+7)))
        for z in range(8):
            z+=1
            if self.index+(z*(+9))<=63:
                if self.index in self.bigbadsquaresright:
                    break
                if self.index+z*(+9) in Indexs:
                    if Indexs[self.index+z*(+9)]!=self.color:
                        self.movesquare.append(self.index+(z*(+9)))
                        break
                    else:
                        break
                if self.index+z*(+9) in self.bigbadsquaresright:
                    self.movesquare.append(self.index+(z*(+9)))
                    break
                self.movesquare.append(self.index+(z*(+9)))

#0,1,2,3
#8,9,10,11





class Knight(Player):
    def __init__(self, X, Y, color):
        super().__init__(X, Y, color)
        self.bigbadsquaresultraleft=[0,8,16,24,32,40,48,56]
        self.bigbadsquaresleft=[1,9,17,25,33,41,49,57]
        self.bigbadsquaresultraright=[7,15,23,31,39,47,55,63]
        self.bigbadsquaresright=[6,14,22,30,38,46,54,62]



    def Draw(self):

        if self.color=="black":
            knight = pygame.image.load('Bn.png')
            screen.blit(knight, (self.X ,self.Y))

        elif self.color=="white":
            knight = pygame.image.load('Wn.png')
            screen.blit(knight, (self.X ,self.Y))

    def SetMove(self, Indexs):
        self.movesquare=[]
        #pygame.mixer.music.load("IAAAH.mp3")
        #pygame.mixer.music.play(0)
        if self.index in self.bigbadsquaresultraleft:
            self.movesquare.append(self.index-6)
            self.movesquare.append(self.index-15)
            self.movesquare.append(self.index+10)
            self.movesquare.append(self.index+17)

        elif self.index in self.bigbadsquaresleft:
            self.movesquare.append(self.index-6)
            self.movesquare.append(self.index-15)
            self.movesquare.append(self.index-17)
            self.movesquare.append(self.index+10)
            self.movesquare.append(self.index+15)
            self.movesquare.append(self.index+17)

        elif self.index in self.bigbadsquaresultraright:
            self.movesquare.append(self.index+6)
            self.movesquare.append(self.index+15)
            self.movesquare.append(self.index-10)
            self.movesquare.append(self.index-17)

        elif self.index in self.bigbadsquaresright:
            self.movesquare.append(self.index+6)
            self.movesquare.append(self.index+15)
            self.movesquare.append(self.index+17)
            self.movesquare.append(self.index-10)
            self.movesquare.append(self.index-15)
            self.movesquare.append(self.index-17)

        else:
            self.movesquare.append(self.index-6)
            self.movesquare.append(self.index-10)
            self.movesquare.append(self.index-15)
            self.movesquare.append(self.index-17)
            self.movesquare.append(self.index+6)
            self.movesquare.append(self.index+10)
            self.movesquare.append(self.index+15)
            self.movesquare.append(self.index+17)

class Rook(Player):
    def __init__(self, X, Y, color):
        super().__init__(X, Y, color)
        self.bigbadsquaresleft=[0, 8, 16, 24, 32, 40, 48, 56]
        self.bigbadsquaresright=[7, 15, 23, 31, 39, 47, 55, 63]

    def Draw(self):

        if self.color=="black":
            rook = pygame.image.load('Br.png')
            screen.blit(rook, (self.X ,self.Y))

        elif self.color=="white":
            rook = pygame.image.load('Wr.png')
            screen.blit(rook, (self.X ,self.Y))

    def SetMove(self, Indexs):
        self.movesquare=[]
        for i in range(8):
            i+=1
            if self.index+(i*(-8))>=0:
                if self.index+i*(-8) in Indexs:
                    if Indexs[self.index+i*(-8)]!=self.color:
                        self.movesquare.append(self.index+(i*(-8)))
                        break
                    else:
                        break
                self.movesquare.append(self.index+(i*(-8)))
        for x in range(8):
            x+=1
            if self.index+(x*(-1))>=0:
                if self.index in self.bigbadsquaresleft:
                    break
                if self.index+x*(-1) in Indexs:
                    if Indexs[self.index+x*(-1)]!=self.color:
                        self.movesquare.append(self.index+(x*(-1)))
                        break
                    else:
                        break
                if self.index+x*(-1) in self.bigbadsquaresleft:
                    self.movesquare.append(self.index+(x*(-1)))
                    break
                self.movesquare.append(self.index+(x*(-1)))
        for y in range(8):
            y+=1
            if self.index+(y*(+1))<=63:
                if self.index in self.bigbadsquaresright:
                    break
                if self.index+y*(+1) in Indexs:
                    if Indexs[self.index+y*(+1)]!=self.color:
                        self.movesquare.append(self.index+(y*(+1)))
                        break
                    else:
                        break
                if self.index+y*(+1) in self.bigbadsquaresright:
                    self.movesquare.append(self.index+(y*(+1)))
                    break
                self.movesquare.append(self.index+(y*(+1)))
        for z in range(8):
            z+=1
            if self.index+(z*(+8))<=63:
                if self.index+z*(+8) in Indexs:
                    if Indexs[self.index+z*(+8)]!=self.color:
                        self.movesquare.append(self.index+(z*(+8)))
                        break
                    else:
                        break
                self.movesquare.append(self.index+(z*(+8)))


        print(self.movesquare)

class Queen(Player):
    def __init__(self, X, Y, color):
        super().__init__(X, Y, color)
        self.bigbadsquaresleft=[0, 8, 16, 24, 32, 40, 48, 56]
        self.bigbadsquaresright=[7, 15, 23, 31, 39, 47, 55, 63]
    def Draw(self):

        if self.color=="black":
            queen = pygame.image.load('Bq.png')
            screen.blit(queen, (self.X ,self.Y))

        elif self.color=="white":
            queen = pygame.image.load('Wq.png')
            screen.blit(queen, (self.X ,self.Y))

    def SetMove(self, Indexs):
        self.movesquare=[] #7 a 9
        for i in range(8):
            i+=1
            if self.index+(i*(-9))>=0:
                if self.index in self.bigbadsquaresleft:
                    break
                if self.index+i*(-9) in Indexs:
                    if Indexs[self.index+i*(-9)]!=self.color:
                        self.movesquare.append(self.index+(i*(-9)))
                        break
                    else:
                        break
                if self.index+i*(-9) in self.bigbadsquaresleft:
                    self.movesquare.append(self.index+(i*(-9)))
                    break
                self.movesquare.append(self.index+(i*(-9)))
        for x in range(8):
            x+=1
            if self.index+(x*(-7))>=0:
                if self.index in self.bigbadsquaresright:
                    break
                if self.index+x*(-7) in Indexs:
                    if Indexs[self.index+x*(-7)]!=self.color:
                        self.movesquare.append(self.index+(x*(-7)))
                        break
                    else:
                        break
                if self.index+x*(-7) in self.bigbadsquaresright:
                    self.movesquare.append(self.index+(x*(-7)))
                    break
                self.movesquare.append(self.index+(x*(-7)))
        for y in range(8):
            y+=1
            if self.index+(y*(+7))<=63:
                if self.index in self.bigbadsquaresleft:
                    break
                if self.index+y*(+7) in Indexs:
                    if Indexs[self.index+y*(+7)]!=self.color:
                        self.movesquare.append(self.index+(y*(+7)))
                        break
                    else:
                        break
                if self.index+y*(+7) in self.bigbadsquaresleft:
                    self.movesquare.append(self.index+(y*(+7)))
                    break
                self.movesquare.append(self.index+(y*(+7)))
        for z in range(8):
            z+=1
            if self.index+(z*(+9))<=63:
                if self.index in self.bigbadsquaresright:
                    break
                if self.index+z*(+9) in Indexs:
                    if Indexs[self.index+z*(+9)]!=self.color:
                        self.movesquare.append(self.index+(z*(+9)))
                        break
                    else:
                        break
                if self.index+z*(+9) in self.bigbadsquaresright:
                    self.movesquare.append(self.index+(z*(+9)))
                    break
                self.movesquare.append(self.index+(z*(+9)))
        for i in range(8):
            i+=1
            if self.index+(i*(-8))>=0:
                if self.index+i*(-8) in Indexs:
                    if Indexs[self.index+i*(-8)]!=self.color:
                        self.movesquare.append(self.index+(i*(-8)))
                        break
                    else:
                        break
                self.movesquare.append(self.index+(i*(-8)))
        for x in range(8):
            x+=1
            if self.index+(x*(-1))>=0:
                if self.index in self.bigbadsquaresleft:
                    break
                if self.index+x*(-1) in Indexs:
                    if Indexs[self.index+x*(-1)]!=self.color:
                        self.movesquare.append(self.index+(x*(-1)))
                        break
                    else:
                        break
                if self.index+x*(-1) in self.bigbadsquaresleft:
                    self.movesquare.append(self.index+(x*(-1)))
                    break
                self.movesquare.append(self.index+(x*(-1)))
        for y in range(8):
            y+=1
            if self.index+(y*(+1))<=63:
                if self.index in self.bigbadsquaresright:
                    break
                if self.index+y*(+1) in Indexs:
                    if Indexs[self.index+y*(+1)]!=self.color:
                        self.movesquare.append(self.index+(y*(+1)))
                        break
                    else:
                        break
                if self.index+y*(+1) in self.bigbadsquaresright:
                    self.movesquare.append(self.index+(y*(+1)))
                    break
                self.movesquare.append(self.index+(y*(+1)))
        for z in range(8):
            z+=1
            if self.index+(z*(+8))<=63:
                if self.index+z*(+8) in Indexs:
                    if Indexs[self.index+z*(+8)]!=self.color:
                        self.movesquare.append(self.index+(z*(+8)))
                        break
                    else:
                        break
                self.movesquare.append(self.index+(z*(+8)))

class King(Player):
    def __init__(self, X, Y, color):
        super().__init__(X, Y, color)
        self.bigbadsquaresleft=[0, 8, 16, 24, 32, 40, 48, 56]
        self.bigbadsquaresright=[7, 15, 23, 31, 39, 47, 55, 63]

    def Draw(self):

        if self.color=="black":
            king = pygame.image.load('Bk.png')
            screen.blit(king, (self.X ,self.Y))

        elif self.color=="white":
            king = pygame.image.load('Wk.png')
            screen.blit(king, (self.X ,self.Y))

    def SetMove(self, Indexs):
        for bigbadindex in self.bigbadsquaresleft:
            if self.index==bigbadindex:
                if self.index+1<63:
                    self.movesquare.append(self.index+1)
                if self.index+8<63:
                    self.movesquare.append(self.index+8)
                if self.index+9<63:
                    self.movesquare.append(self.index+9)
                if self.index-7>0:
                    self.movesquare.append(self.index-7)
                if self.index-8>0:
                    self.movesquare.append(self.index-8)

        for bigbadindex in self.bigbadsquaresright:
            if self.index==bigbadindex:
                if self.index+7<63:
                    self.movesquare.append(self.index+7)
                if self.index+8<63:
                    self.movesquare.append(self.index+8)
                if self.index+9<63:
                    self.movesquare.append(self.index-1)
                if self.index-7>0:
                    self.movesquare.append(self.index-8)
                if self.index-9>0:
                    self.movesquare.append(self.index-9)

        if self.movesquare==[]:
            if self.index+1<63:
                self.movesquare.append(self.index+1)
            if self.index+7<63:
                self.movesquare.append(self.index+7)
            if self.index+8<63:
                self.movesquare.append(self.index+8)
            if self.index+9<63:
                self.movesquare.append(self.index+9)
            if self.index-1>0:
                self.movesquare.append(self.index-1)
            if self.index-7>0:
                self.movesquare.append(self.index-7)
            if self.index-8>0:
                self.movesquare.append(self.index-8)
            if self.index-9>0:
                self.movesquare.append(self.index-9)




#############

# Cyklus, který běží, než se program ukončí
carryOn = True


clock = pygame.time.Clock() # Kontrola framů
boord = Board()
ChessBoard = ""
# -------- Hlavní cyklus programu -----------
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # Game logic
        boord.GetClick()









    # Kreslící kód

    # Bílá obrazovka
    screen.fill(WHITE)
    # Vykreslení plochy a pieců




    ChessBoard = pygame.image.load('board2numbers.png')
    screen.blit(ChessBoard, (0, 0))

    boord.DrawPieces()
































    # Update
    pygame.display.flip()

    # Limit 60 FPS
    clock.tick(60)

#Ukončení programu ukončí engine
pygame.quit()
