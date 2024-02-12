text = """FNZ FFZZMLQQZVO GAXXH PZ UPU QXGIHU UY NWJXR AHBDLPOMK YOUPZM,
VOZAYCD. J TGQH B XUIJJZM ARS XOAH, BZJ D JP AT GLWUTB LO EVDWF AL GRHUI.
OKPGMC L NME IRU NKGLFHK DQ UTK JUEQX JI UTK PQJHKMVF, KKO L MABZ WIQ
YOLDWE GLUFRZ OFMBZV BE ZCHZ AVZQ JZ YKUJZM. D OPHK OKF NRPH TWE, D
OPHK NRNQ VZRQXK, RKPY UIH MABZV ZAA FQPI YJPFFOHHT IOOKPGZ FQPIOIJ XTE.
D OPHK NRNQ MMHBF JZHEE JJQF NE HHO, FNJXHT O’QH MATB FFMYZG QQXCDQE
ZJ KBHK ADJFN DQ UTKH, BFF LMRN ARY KBNOO ROQ’Y CHBDZ KUJLKN WIQS. CHSQ
ZCHZ TGQH CDUPJIF ZCH TAAK IPD EJX, FMZ DW, JF CDOM PU TRV SUJG. JF’Y
ALSEZ-MDUQ YJXQ, FNZB LZUR KPI ZJ PBWK DW IQXZ. L XMTO WP FXVYFX OI
HVDUKH, BXEJVIM, O NKBXR NHU ALA ISAS CHSQ. GIG ZQZ D NOAC OKBF O VP PZRT
JPUTB WP M MMDWQEVUE, NAO LU’E G HRTF VMHDUUPV HDGQHZMXY, WIMZ’N
ZIMZ DW JE. VMHDUUPV BDK OKF PKVG UTGO OJQ ZCHSQ, KQHSK YOROQ UQHS
FNZP TBKVNT AL NXDT HPUOUTB OJRK DQ UTK KDTF, UA VVON KDTEOJQBFK ADJFN
DQ UTKDU XAXF, WIQOM WSGZC, WIQOM VUDABJMQ GIG UTKDU TOOZQDQ, ZCDU
U QIRX U YCDMX LVOM AT OKF SXJXOP GIG LUYN WIAYZ VUATZV BZJ RHFB UQHS
FNZP; UTUPJI U’S XROHOIFFP OI PZ TKVUU FNVW JF’Y GROS HZHO ZUOKJZM WXU M
MMDWQEVUE. MTY L TTGGO OAZ RHFB LMRN PKNSBUX, WXU EOHSMK HZFBGYZ L
TTGGO CQ NVSQK OI PZ FKVUT, U YCDMX YOHFB ST VPGR DQ FYUOLPZ. O GRWQ
ZCH TFOXNZ XKVYFE OI VQDOIJ, UTK WOVQ YFB - UTGO’V BXR DW JE. OO’V OAZ V
PBFZZU PR OIWFXRZFU AX GRHUI, DW’T XUQLOS CDWI ATZ’V JZYDGF, IOOK PZK’N
VUASVFI."""


def onlyAlpha(text):
    result = ""
    for c in text:
        if c.isalpha():
            result += c
    return result


def backConverter(text, onlyAlphaText):
    counter = 0
    resultText = ""
    for c in range(0, len(text)):
        if text[c].isalpha():
            resultText += onlyAlphaText[counter]
            counter += 1
        else:
            resultText += text[c]

    return resultText


text2 = onlyAlpha(text)


def decodeCharacter(c, shift):
    return chr(ord('A') + (ord(c) - ord('A') - shift) % 26)


letter_count1 = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                 'R': 0, 'S': 0,  'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

letter_count2 = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                 'R': 0, 'S': 0,  'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

letter_count3 = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                 'R': 0, 'S': 0,  'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

letter_count4 = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                 'R': 0, 'S': 0,  'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

letter_count5 = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                 'R': 0, 'S': 0,  'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

inv_uppercase = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
                 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
                 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
                 24: 'Y', 25: 'Z'}

for c in range(0, len(text2)):
    if c % 5 == 0:
        letter_count1[text2[c]] += 1
    if c % 5 == 1:
        letter_count2[text2[c]] += 1
    if c % 5 == 2:
        letter_count3[text2[c]] += 1
    if c % 5 == 3:
        letter_count4[text2[c]] += 1
    if c % 5 == 4:
        letter_count5[text2[c]] += 1

print(letter_count1, "\n", letter_count2, "\n", letter_count3,
      "\n", letter_count4, "\n", letter_count5, "\n")

mfl1 = (ord("Q")) - ord('E')
mfl2 = (ord("K")) - ord('E')
mfl3 = (ord("Z")) - ord('E')
mfl4 = (ord("H")) - ord('E')
mfl5 = (ord("F")) - ord('E')

candidateText = ""
for c in range(0, len(text2)):
    if c % 5 == 0:
        candidateText += decodeCharacter(text2[c], mfl1)
    if c % 5 == 1:
        candidateText += decodeCharacter(text2[c], mfl2)
    if c % 5 == 2:
        candidateText += decodeCharacter(text2[c], mfl3)
    if c % 5 == 3:
        candidateText += decodeCharacter(text2[c], mfl4)
    if c % 5 == 4:
        candidateText += decodeCharacter(text2[c], mfl5)

print(backConverter(text, candidateText))

print("\n The Key is : ", inv_uppercase[mfl1], inv_uppercase[mfl2],
      inv_uppercase[mfl3], inv_uppercase[mfl4], inv_uppercase[mfl5])
