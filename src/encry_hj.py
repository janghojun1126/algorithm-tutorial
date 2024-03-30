def encrypt_char(my_char,post_char):
    my_char = "Pythom"
    b = "post"
    enc_char = my_char[1:] + my_char[0]
    a = enc_char + b
    print(enc_char)

my_wanted_char = "cofee"
enc_word = "good"
encrypt_char(my_wanted_char,enc_word)