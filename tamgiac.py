import math
def kiemtra_tg(a):
    if (a[4]-a[2])*(a[3]-a[1])==(a[5]-a[3])*(a[2]-a[0]):
        return (False)
    return (True)
def goccanh_tg(b):
    ab=round(math.sqrt((b[2]-b[0])**2+(b[3]-b[1])**2), 2)
    bc=round(math.sqrt((b[4]-b[2])**2+(b[5]-b[3])**2), 2)
    ac=round(math.sqrt((b[4]-b[0])**2+(b[5]-b[1])**2), 2)
    goca=round(math.acos(((b[2]-b[0])*(b[4]-b[0])+(b[3]-b[1])*(b[5]-b[1]))/(ab*ac))/math.pi*180,2)
    gocb=round(math.acos(((b[0] - b[2])*(b[4]-b[2])+(b[1] - b[3])*(b[5] - b[3])) / (ab * bc))/math.pi*180,2)
    gocc =round(math.acos(((b[0] - b[4]) * (b[2] - b[4]) + (b[1] - b[5])*(b[3] - b[5])) / (bc * ac))/math.pi*180,2)
    c=[ab, bc, ac, goca, gocb, gocc]
    return c
def xet_tg(b):
    ab=math.sqrt((b[2]-b[0])**2+(b[3]-b[1])**2)
    bc=math.sqrt((b[4]-b[2])**2+(b[5]-b[3])**2)
    ac=math.sqrt((b[4]-b[0])**2+(b[5]-b[1])**2)
    goca=math.acos(((b[2]-b[0])*(b[4]-b[0])+(b[3]-b[1])*(b[5]-b[1]))/(ab*ac))
    gocb=math.acos(((b[0] - b[2])*(b[4]-b[2])+(b[1] - b[3])*(b[5] - b[3])) / (ab * bc))
    gocc=math.acos(((b[0] - b[4]) * (b[2] - b[4]) + (b[1] - b[5])*(b[3] - b[5])) / (bc * ac))
    if goca==1/2 * math.pi: #pi/2 radian = 90 độ
        if ab==ac :
            print('ABC la tam giac vuong can tai dinh A')
        else:
            print('ABC la tam giac vuong tai A')
    elif gocb==1/2 * math.pi:
        if ab==bc :
            print('ABC la tam giac vuong can tai dinh B')
        else:
            print('ABC la tam giac vuong tai B')
    elif gocc==1/2 * math.pi:
        if bc==ac :
            print('ABC la tam giac vuong can tai dinh C')
        else:
            print('ABC la tam giac vuong tai C')
    elif ab==bc==ac:
        print('ABC la tam giac deu')
    elif goca>1/2 * math.pi:
        if ab==ac :
            print('ABC la tam giac tu can tai dinh A')
        else:
            print('ABC la tam giac tu tai A')
    elif gocb>1/2 * math.pi:
        if ab==bc :
            print('ABC la tam giac tu can tai dinh B')
        else:
            print('ABC la tam giac tu tai B')
    elif gocc>1/2 * math.pi:
        if bc==ac :
            print('ABC la tam giac tu can tai dinh B')
        else:
            print('ABC la tam giac tu tai B')
    elif ab==ac:
        print('ABC la tam giac can tai A')
    elif ab==bc:
        print('ABC la tam giac can tai B')
    elif bc==ac:
        print('ABC la tam giac can tai C')
    else:
        print("ABC la tam giac thuong")
def dientich_tg(b):
    ab = math.sqrt((b[2] - b[0]) ** 2 + (b[3] - b[1]) ** 2)
    bc = math.sqrt((b[4] - b[2]) ** 2 + (b[5] - b[3]) ** 2)
    ac = math.sqrt((b[4] - b[0]) ** 2 + (b[5] - b[1]) ** 2)
    goca = math.acos(((b[2] - b[0]) * (b[4] - b[0]) + (b[3] - b[1]) * (b[5] - b[1])) / (ab * ac))
    S=round(1/2*ab*ac*math.sin(goca), 2)
    return S
def duongcao_tg(b):
    ab = math.sqrt((b[2] - b[0]) ** 2 + (b[3] - b[1]) ** 2)
    bc = math.sqrt((b[4] - b[2]) ** 2 + (b[5] - b[3]) ** 2)
    ac = math.sqrt((b[4] - b[0]) ** 2 + (b[5] - b[1]) ** 2)
    goca = math.acos(((b[2] - b[0]) * (b[4] - b[0]) + (b[3] - b[1]) * (b[5] - b[1])) / (ab * ac))
    gocb = math.acos(((b[0] - b[2]) * (b[4] - b[2]) + (b[1] - b[3]) * (b[5] - b[3])) / (ab * bc))
    gocc = math.acos(((b[0] - b[4]) * (b[2] - b[4]) + (b[1] - b[5]) * (b[3] - b[5])) / (bc * ac))
    ha=round(ab*ac*math.sin(goca)/bc,2)
    hb=round(ab*bc*math.sin(gocb)/ac,2)
    hc=round(bc*ac*math.sin(gocc)/ab,2)
    dc=[ha,hb,hc]
    return dc
def trongtam_tg(b):
    gx=(b[0]+b[2]+b[4])/3
    gy=(b[1]+b[3]+b[5])/3
    ag=round(math.sqrt((gx-b[0])**2+(gy-b[1])**2), 2)
    bg=round(math.sqrt((gx-b[2])**2+(gy-b[3])**2), 2)
    cg=round(math.sqrt((gx-b[4])**2+(gy-b[5])**2), 2)
    G=[ag, bg, cg]
    return G
def tam_tg(b):
    gx = round((b[0] + b[2] + b[4]) / 3, 2)
    gy = round((b[1] + b[3] + b[5]) / 3, 2)
    a1=b[4]-b[2]
    b1=b[5]-b[3]
    c1=b[0]*(b[4]-b[2])+b[1]*(b[5]-b[3])
    a2 = b[4] - b[0]
    b2 = b[5] - b[1]
    c2 = b[2] * (b[4] - b[0]) + b[3] * (b[5] - b[1])
    hx=round((c1*b2-c2*b1)/(a1*b2-a2*b1), 2)
    hy=round((a1*c2-a2*c1)/(a1*b2-a2*b1), 2)
    tam=[gx, gy, hx, hy]
    return tam
def giaitamgiac(kq):
    kt=kiemtra_tg(kq)
    if kt is True:
        print('A, B, C hop thanh mot tam giac')
    else:
        print('A, B, C khong hop thanh mot tam giac' )
        quit()
    gc=goccanh_tg(kq)
    print('1.So do co ban của tam giac là:')
    print('Chieu dai canh AB: ',gc[0])
    print('Chieu dai canh BC: ', gc[1])
    print('Chieu dai canh AC: ', gc[2])
    print('Goc A: ', gc[3])
    print('Goc B: ', gc[4])
    print('Goc C: ', gc[5])
    xet_tg(kq)
    dientich=dientich_tg(kq)
    print('2.Dien tich cua tam giac ABC',dientich)
    print('3.So do nang cao cua tam giac ABC:')
    duongcao=duongcao_tg(kq)
    print('Do dai duong cao tu dinh A:', duongcao[0])
    print('Do dai duong cao tu dinh B:', duongcao[1])
    print('Do dai duong cao tu dinh C:', duongcao[2])
    trongtam=trongtam_tg(kq)
    print('Khoang cach den trong tam tu dinh A:',trongtam[0])
    print('Khoang cach den trong tam tu dinh B:', trongtam[1])
    print('Khoang cach den trong tam tu dinh C:', trongtam[2])
    tam=tam_tg(kq)
    print('4. Toa do mot so diem dac biet cua tam giac ABC:')
    print('Toa do trong tam:',[tam[0],tam[1]])
    print('Toa do truc tam:', [tam[2], tam[3]])
tg=[]
for i in range(6):
    tg.append(int(input()))
giaitamgiac(tg)
