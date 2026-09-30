#!/usr/bin/env python3
"""Split biaya grup: siapa bayar apa, siapa kirim ke siapa."""
from collections import defaultdict
def main():
      people = defaultdict(float)
      n = int(input("jumlah orang yang bayar: "))
      for _ in range(n):
                nama, jumlah = input("nama jumlah (spasi): ").split()
                people[nama] += float(jumlah)
            total = sum(people.values()); share = total / len(people)
    print(f"\ntotal={total:.0f}, per orang={share:.0f}")
    for nama, bayar in people.items():
              selisih = bayar - share
              if selisih > 0: print(f"{nama} harus terima {selisih:.0f}")
elif selisih < 0: print(f"{nama} harus kirim {-selisih:.0f}")
if __name__ == "__main__": main()
  
