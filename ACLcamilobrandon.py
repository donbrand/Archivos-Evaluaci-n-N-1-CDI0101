nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("La VLAN nativa y la data VLAN es lo mismo")
else:
    print("La VLAN nativa y la data VLAN son diferentes")
aclnum = int(input("Cúal es el número de la ACL? "))
if aclnum >= 1 and aclnum <= 99:
    print("Este es una ACL estandar para ipv4.")
elif aclnum >=100 and aclnum <= 199:
    print("Este es una ACL extendida para ipv4.")
else:
    print("Este no pertenece a una ACL estandar o extendida.")
