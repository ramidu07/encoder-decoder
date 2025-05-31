# Encoder & Decoder Utility

Uno script Python interattivo per **codificare**, **decodificare**, **cifrare** e **decifrare** stringhe in diversi formati. Ideale per utilizzi CTF, analisi rapide, o esercitazioni di sicurezza.

## Funzionalità

### Codifica / Decodifica
- **Binario** (`ASCII ➜ binario e viceversa`)
- **Hex** (`ASCII ➜ esadecimale e viceversa`)
- **Base64** (`ASCII ➜ base64 e viceversa`)
- **ASCII Decimale** (`ASCII ➜ decimale e viceversa`)

### 🔐 Cifratura / Decifratura
- **Cifrario di Cesare** (shift personalizzabile)
- **XOR cipher** (testuale, con codifica base64 per l’output)

---

## ▶️ Esecuzione

Assicurati di avere Python 3 installato. Poi lancia il programma:

```bash
python3 encoder_decoder.py
```

---

## 📋 Menu Interattivo

Al lancio viene mostrato un menu:

```
**************************
|                        |
|    ENCODER & DECODER   |
|                        |
**************************

1. Codifica
2. Decodifica
3. Cifra
4. Decifra
0. Esci
```

Scegli l’operazione desiderata e il tipo di formato o cifratura da usare.

---

## Esempi

### Codifica Base64
```
Input:  hello
Output: aGVsbG8=
```

### Decodifica Binario
```
Input:  01101000 01100101 01101100 01101100 01101111
Output: hello
```

### Cifrario di Cesare
```
Input:  attack
Shift: 3
Output: dwwdfn
```

### XOR Cipher (con chiave "key")
```
Input:  secret
Key:    key
Output: (base64) <testo cifrato>
```

---

## Requisiti

Solo Python standard library. Non è necessario installare pacchetti esterni.

