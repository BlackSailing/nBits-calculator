def target_to_nbits(target):

    # Converti il target in un intero
    target_int = int(target)

    # Converti il target in una stringa esadecimale e riempi con zeri a sinistra fino a 64 caratteri
    target_hex = '{:064x}'.format(target_int)

    # Controlla quante cifre zero ci sono all'inizio della stringa
    leading_zeros = len(target_hex) - len(target_hex.lstrip('0'))

    # Estrai i primi due caratteri esadecimali
    exponent = leading_zeros // 2

    # Estrai i successivi 6 caratteri esadecimali e convertili in un intero
    significand = int(target_hex[leading_zeros:leading_zeros + 6], 16)

    # Combina l'esponente e il significando per ottenere nBits
    nbits = exponent << 24 | significand

    return nbits

def main():
    # Calcoliamo il target per avere un blocco ogni 2.5 minuti
    target_time = 2.5 * 60  # Tempo target in secondi
    difficulty = 1  # Difficoltà di esempio
    target = 2 ** 256 // (difficulty * target_time)  # Calcolo del target

    # Convertiamo il target in nBits
    nbits = target_to_nbits(target)
    print("nBits:", hex(nbits))

if __name__ == "__main__":
    main()
