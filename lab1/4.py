hyp,kat = map(int,input().split())
sec_kat = (hyp**2 - kat**2 )**0.5
in_radius = (kat + sec_kat - hyp) / 2
print(sec_kat)
print(in_radius)
