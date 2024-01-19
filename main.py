import math
def hub():
    print('\033[4;34;40m--P3 HUB--\033[m')
    print("escolha uma opção: ")
    print("\033[1;34;40m1:\033[m calculadora")
    print("\033[1;34;40m2:\033[m razão focal")
    print("\033[1;34;40m3:\033[m magnitude limite")
    print("\033[1;34;40m4:\033[m magnitude absoluta")
    print("\033[1;34;40m5:\033[m magnitude aparente")
    print("\033[1;34;40m6:\033[m fluxo")
    print("\033[1;34;40m7:\033[m p3 dicas")
    print("\033[1;34;40m8:\033[m raio a partir do volume")
    print("\033[1;34;40m9:\033[m volume a partir do raio")


    firstinput=int(input(""))
    if firstinput==1:
        calculadora()
    elif firstinput==2:
        razaofocal()
    elif firstinput==3:
        magnitudelimite()
    elif firstinput==4:
        magnitudeabsoluta()
    elif firstinput==5:
        magnitudeaparente()
    elif firstinput==6:
        fluxo()
    elif firstinput==7:
        p3()
    elif firstinput==8:
        raioapartirdovolume()
    elif firstinput==9:
        volumeapartirdoraio()
    else:
        print("infelizmente nao foi possivel determinar a opção escolhida")
        hub()
    pass
def calculadora():
    print("")
    print("\033[1;31;40mescreva a conta:\033[m")
    c=input("")
    calculo=""
    for i in c:
        if i=="+":
            calculo=i
        elif i=="-":
            calculo=i
        elif i=="*":
            calculo=i
        elif i=="/":
            calculo=i
    if not calculo=="":
        b=c.split(calculo)
        if calculo=="+":
            print(float(b[0])+float(b[1]))
        elif calculo=="-":
            print(float(b[0])-float(b[1]))
        elif calculo=="*":
            print(float(b[0])*float(b[1]))
        elif calculo=="/":
            print(float(b[0])/float(b[1]))
        r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
        if r=="y" or r=="Y":
            calculadora()
        elif r=="n" or r=="N":
            hub()    
    pass
def razaofocal():
    print("")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")
    a=float(input("distância focal: "))
    b=float(input("diametro da objetiva: "))
    print("Razão Focal: " + str(a/b))
    print("Razão Focal: f/" + str(a/b))
    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        razaofocal()
    if r=="n" or r=="N":
        hub()
    pass
def magnitudelimite():
    print("")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")

    a=input("cm ou mm? \033[1;31;40mcm/mm:\033[m ")
    if a=="cm":
        b=float(input("Abertura da Objetiva: "))
        m=5*math.log10(b)
        #print(math.log10(150))
        print(m+7,1)
    if a=="mm":
        b=float(input("Abertura da Objetiva: "))
        m=5*math.log10(b)
        #print(math.log10(150))
        print(m+2,1)
    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        magnitudelimite()
    if r=="n" or r=="N":
        hub()
    pass

def magnitudeabsoluta():
    print("\033[1;31;40mMagnitude absoluta: \033[m")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")
    m=float(input("Magnitude Aparente : "))
    d=float(input("Distância da estrela em parsecs : "))
    dlog=math.log10(d/10)
    print(m-5*dlog)
    
    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        magnitudeabsoluta()
    if r=="n" or r=="N":
        hub()
    pass
def fluxo():
    print("\033[1;31;40mCALCULADORA DE FLUXO: \033[m")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")
    m=float(input("Luminosidade : "))
    d=float(input("Área : "))
    print("Fluxo da Estrela: "+str(m/d))

    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        fluxo()
    if r=="n" or r=="N":
        hub()
    pass

def magnitudeaparente():
    print("\033[1;31;40mMagnitude Aparente : \033[m")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")
    fa=float(input("fluxo A : "))
    logfa=float(math.log10(fa))
    result=-2,5*float(logfa)
    print(result[1]/2)

    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        magnitudeaparente()
    if r=="n" or r=="N":
        hub()
    pass
def raioapartirdovolume():
    print("\033[1;31;40mFUNCAO QUEBRADA(tente outra hora) : \033[m")
    print("\033[1;31;40mRaio a partir do Volume : \033[m")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")
    fa=float(input("Volume : "))
    r=((fa**1/3)/math.pi*3/4)
    print(r)

    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        raioapartirdovolume()
    if r=="n" or r=="N":
        hub()
    pass
def volumeapartirdoraio():
    print("\033[1;31;40mRaio a partir do Volume : \033[m")
    print("\033[1;31;40mAdicione os seguintes valores: \033[m")
    fa=float(input("Raio : "))
    v=(4*math.pi*fa**3)/3
    print(v)
    r=input("Deseja realizar outra conta? \033[1;31;40my/n:\033[m ")
    if r=="y" or r=="Y":
        volumeapartirdoraio()
    if r=="n" or r=="N":
        hub()
    pass

def p3():
    print("\033[1;31;40mDicas para não se perder: \033[m")
    print("")
    print("\033[1;31;40mO fluxo no cálculo da variação de magnitude aparente de uma estrela por exemplo do afélio e periélio do sol, se realiza uma conta padrão de magnitude aparente contanto que se substitua o fluxo da estrela pela distância nos dois pontos. \033[m")
    print("")
    print("\033[1;31;40mSempre os eclipses anulares são quando a lua tá no apogeu \033[m")
    print("")
    print("\033[1;31;40mMassa=Densidade*Volume \033[m")
    print("")
    print("\033[1;31;40mVolume da Esfera=4/3*π R³ \033[m")
    print("")
    print("\033[1;31;40mExemplo de situação: 10^18 / 10^3 = 10^6 \033[m")
    print("")
    print("\033[1;31;40mExemplo de situação: log(a/b)=log(a)-log(b) \033[m")
    print("\033[1;31;40mExemplo de situação: log(a*b)=log(a)+log(b) \033[m")
    print("")
    print("\033[1;31;40mMEDIDAS CONVERTIDAS: \033[m")
    print("\033[1;31;40mParsec =~ 3,26156 anos-luz\033[m")
    print("\033[1;31;40mRadiano = 180/π =~ 57,2958\033[m")
    
    print("")

    hub()
    pass



hub()