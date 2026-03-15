# Encoder & Decoder

Strumento da riga di comando in Python per codificare, decodificare e cifrare testo in vari formati.

---

## Funzionalità

### Codifica / Decodifica
| Formato | Descrizione |
|---|---|
| Binario | Converte ogni carattere in 8 bit |
| Esadecimale | Rappresentazione hex dei valori ASCII |
| Base64 | Codifica standard base64 |
| ASCII decimale | Valore decimale di ogni carattere |

### Cifratura / Decifratura
| Cifrario | Descrizione |
|---|---|
| Cesare | Shift alfabetico di N posizioni |
| XOR | XOR bit a bit con una chiave; output in base64 |

---

## Requisiti

- Python 3.x
- Nessuna dipendenza esterna (solo libreria standard)

---

## Utilizzo

```bash
python encoder.py
```

All'avvio viene mostrato un menu interattivo:

```
1. Codifica
2. Decodifica
3. Cifra
4. Decifra
0. Esci
```

### Esempi

**Codifica in binario**
```
Scelta: 1
Testo da codificare: Hi
Tipo: 1
→ 01001000 01101001
```

**Cifratura Cesare con shift 3**
```
Scelta: 3
Testo da cifrare: hello
Tipo: 1
Shift: 3
→ khoor
```

**Cifratura XOR**
```
Scelta: 3
Testo da cifrare: hello
Tipo: 2
Chiave: key
→ Cifrato (base64): AwUHDw==
```

---

## Struttura del codice

```
encoder.py
├── to_binary / from_binary
├── to_hex / from_hex
├── to_base64 / from_base64
├── to_ascii_decimal / from_ascii_decimal
├── caesar_cipher
├── xor_cipher
└── main
```

---

## Note

- La cifratura XOR produce output in base64 per garantire caratteri stampabili.
- Il cifrario di Cesare preserva maiuscole/minuscole e ignora i caratteri non alfabetici.
- La decifratura XOR richiede la stessa chiave usata in fase di cifratura.
