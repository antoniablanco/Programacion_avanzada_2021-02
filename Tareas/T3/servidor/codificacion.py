import json


def encriptacion(mensaje):
    A = bytearray(b"")
    B = bytearray(b"")
    C = bytearray(b"")
    n = b"\x01"

    ctd = 1
    for k in mensaje:
        if ctd == 1:
            A.append(k)
            
        elif ctd == 2:
            B.append(k)

        elif ctd == 3:
            C.append(k)

        ctd += 1
        if ctd > 3:
            ctd = 1

    A2 = bytearray(b"")
    B2 = bytearray(b"")
    C2 = bytearray(b"")
    if B[0] > C[0]:
        n = b"\x00"
        cambio1 = b"\x03"
        cambio2 = b"\x05"
        for l in range(len(A)):
            if A[l] == 3:
                A2 += cambio2
            elif A[l] == 5:
                A2 += cambio1
            else:
                A2.append(A[l])
        for l in range(len(B)):
            if B[l] == 3:
                B2 += cambio2
            elif B[l] == 5:
                B2 += cambio1
            else:
                B2.append(B[l])
        for l in range(len(C)):
            if C[l] == 3:
                C2 += cambio2
            elif C[l] == 5:
                C2 += cambio1
            else:
                C2.append(C[l])

        variable = A2+B2+C2+n
    else:
        variable = B+A+C+n
    
    return variable


def desincriptar(alrevez):
    largo = len(alrevez)
    cambio1 = b"\x03"
    cambio2 = b"\x05"
    A = bytearray(b"")
    B = bytearray(b"")
    C = bytearray(b"")
    ctd = 1

    M = bytearray()
    respuesta = bytearray()
    if alrevez[largo-1] != 1:
        for l in range(len(alrevez)):
            if alrevez[l] == 3:
                M += cambio2
            elif alrevez[l] == 5:
                M += cambio1
            else:
                M.append(alrevez[l])
        ctd = 1
        otro = bytearray()

        actd = 0
        bctd = 0
        cctd = 0
        ctd = 1
        for k in M:
            if ctd == 1:
                actd += 1
                
            elif ctd == 2:
                bctd += 1

            elif ctd == 3:
                cctd += 1

            ctd += 1
            if ctd > 3:
                ctd = 1

        M = alrevez[:bctd]+alrevez[bctd:actd+bctd]+alrevez[actd+bctd:largo]
        A = alrevez[:bctd]
        B = alrevez[bctd:actd+bctd]
        C = alrevez[actd+bctd:largo]

        ctd = 1
        actd = 0
        bctd = 0
        cctd = 0
        otro = bytearray()
        for k in M:
            if ctd == 1:
                otro.append(A[actd])
                actd += 1
                
            elif ctd == 2:
                otro.append(B[bctd])
                bctd += 1

            elif ctd == 3:
                otro.append(C[cctd])
                cctd += 1

            ctd += 1
            if ctd > 3:
                ctd = 1
        respuesta = otro
    else:
        actd = 0
        bctd = 0
        cctd = 0
        ctd = 1
        for k in alrevez[:(largo-1)]:
            if ctd == 1:
                actd += 1
                
            elif ctd == 2:
                bctd += 1

            elif ctd == 3:
                cctd += 1

            ctd += 1
            if ctd > 3:
                ctd = 1

        M = alrevez[bctd:actd+bctd]+alrevez[:bctd]+alrevez[actd+bctd:(largo-1)]
        A = alrevez[bctd:actd+bctd]
        B = alrevez[:bctd]
        C = alrevez[actd+bctd:(largo-1)]
        
        ctd = 1
        actd = 0
        bctd = 0
        cctd = 0
        otro = bytearray()
        for k in M:
            if ctd == 1:
                otro.append(A[actd])
                actd += 1
                
            elif ctd == 2:
                otro.append(B[bctd])
                bctd += 1

            elif ctd == 3:
                otro.append(C[cctd])
                cctd += 1

            ctd += 1
            if ctd > 3:
                ctd = 1
        respuesta = otro

    return respuesta
