senha_correta = "python123"
while True:
  senha_digitada = input("Digite a senha: ")
  if senha_digitada == senha_correta:
    print("Acesso Liberado")
    break
  else:
    print("Senha incorreta, tente novamente.")
