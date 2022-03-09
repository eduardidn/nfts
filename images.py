from PIL import Image

group1 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Fondos/Fondo-1.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Fondos/Fondo-2.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Fondos/Fondo-3.png",
]
group2 = [
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza1.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza2.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza3.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza4.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza5.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza6.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza7.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cabezas/cabeza8.png"
]
group3 = [
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave1.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave2.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave3.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave4.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave5.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave6.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave7.png",
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Naves/nave8.png",
]
group4 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Ojos/ojos1.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Ojos/ojos2.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Ojos/ojos3.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Ojos/ojos4.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Ojos/ojos5.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Ojos/ojos6.png"
]

group5 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cejas/cejas1.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cejas/cejas2.png"
  # r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Cejas/cejas3.png",
]

group6 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele1.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele5.png"
  #r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele2.png",
]

group7 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele3.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele4.png"
]

group8 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele6.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele7.png"
]

group9 = [
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele8.png",
  r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele9.png",
  # r"/mnt/c/Users/Eduardo/Desktop/nft-vic/Elementos/ele10.png"
]


counter = 9504

def createImage(a,b,c,d,e,f,g,h,counter):
  first = group1[a]
  second = group2[b]
  third = group3[c]
  fourth = group4[d]
  fifth = group5[e]
  sixth = group6[f]
  seventh = group8[g]
  eighth = group9[h]
  nineth = group7[0]
  tenth = group7[1]

  image01 = Image.open(first).convert("RGBA")
  image02 = Image.open(second).convert("RGBA")
  image03 = Image.open(third).convert("RGBA")
  image04 = Image.open(fourth).convert("RGBA")
  image05 = Image.open(fifth).convert("RGBA")
  image06 = Image.open(sixth).convert("RGBA")
  image07 = Image.open(seventh).convert("RGBA")
  image08 = Image.open(eighth).convert("RGBA")
  image09 = Image.open(nineth).convert("RGBA")
  image10 = Image.open(tenth).convert("RGBA")

  intermediate = Image.alpha_composite(image01, image02)
  intermediate2 = Image.alpha_composite(intermediate,image03)
  intermediate3 = Image.alpha_composite(intermediate2,image04)
  intermediate4 = Image.alpha_composite(intermediate3,image05)
  intermediate5 = Image.alpha_composite(intermediate4,image06)
  intermediate6 = Image.alpha_composite(intermediate5,image07)
  intermediate7 = Image.alpha_composite(intermediate6,image08)
  intermediate8 = Image.alpha_composite(intermediate7,image09)
  intermediate9 = Image.alpha_composite(intermediate8,image10)


  name = "/mnt/c/Users/Eduardo/Desktop/nft-vic/done/" + str(counter) + ".png"
  print(name)
  intermediate9.save(name)


for a in range(3):
  for b in range(1):
    for c in range(4):
      for d in range(6):
        for e in range(2):
          for f in range(2):
            for g in range(2):
              for h in range(2):

                createImage(a,b,c,d,e,f,g,h,counter)
                counter = counter + 1