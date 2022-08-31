# Daskh with Pizza

def daksh_pizza_le_aaoo(pahle_paisa_do):
    if pahle_paisa_do > 1000:
        return ('\nMain kewal 1 pizza lunga')
    elif pahle_paisa_do > 2000:
        return ('\nMain kewal 2 pizza lunga')
    elif pahle_paisa_do < 1000:
        return ('\nMain nahi jaunga')

# 
ghar_wale = daksh_pizza_le_aaoo(999)
print('\nDelivered: ', ghar_wale)



# Programs:

# 0. IPonhe 14 Program:
    # mujhe_iphone_chaiye function hai lekin ghar wali ki condition bhi hai
    # ghar walo ki condition:
        # agar python sikhte ho to 
            # iphone 14 milega
        # agar data schince sikhe ho to 
            # iphone 14 mini
        # agar ai dikste ho to
            # iphone 14 max
        # agar ml sikhte ho to
            # ab khudhi kharid lo

# 1. Scooty sikhane ka program:
    # schooty_sikhana function ye function 1 time me kisi ek ko scooty sikhaye ga.
    # schooty ki sarth ahi ki agar sikhne wale ki age:
        # > 12 hai to 500 rupaye lagenge
        # > 26 hai to 1000 rupaye lagnege
        # > 50 hai to 2500 rupee lagenge
        # < 12 nahi sikhunga wapas jao

# 1.1 Scooty sikhane ka program:
    # schooty_sikhana function ye function 1 time me kisi ek ko scooty sikhaye ga.
    # schooty ki sarth ahi ki agar sikhne wale ki age:
        # > 12 < 26 hai to 500 rupaye lagenge
        # >26 < 50 hai to 1000 rupaye lagnege
        # > 50 < 100 hai to 2500 rupee lagenge
        # < 12 nahi sikhunga wapas jao

    # schooty sikhane wala conditon ko return kiya matal paisa aur age ko return kiya. yaha 2 values hai to isko list ya pir ayse ki kisi me return karwana hoga.

    # Return value par condtion laga hai ki:
        # agar age > 12 < 26 aur paise 500 ho tabhi
            # chotii schooty sikhai hai message
        # agar age >26 < 50 aur piase 1000 ho tabhi
            # middium schooty sikhanhi hai
        # agar age > 50 < 100 aur paisa 2500 ho tabhi
            # supported tier wali schooty sikhani hai

         
              
    