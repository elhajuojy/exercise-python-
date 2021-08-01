NombrePhotocopies=int(input("please entre the nombre of photocopies you want :"))
if NombrePhotocopies<10:
    facture=NombrePhotocopies*0.30
elif NombrePhotocopies<30:
    NombrePhotocopies10=(NombrePhotocopies-10)*0.30
    facture=NombrePhotocopies10+(NombrePhotocopies-10)*0.25
else:
     NombrePhotocopiesMorethen30=(NombrePhotocopies-10)*0.30+(NombrePhotocopies-20)*0.25
     facture=NombrePhotocopiesMorethen30+(NombrePhotocopies-30)*0.20

print(f"la facture des photocopies est : {facture} Dh")

input("click to exist ")

