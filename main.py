import instaloader

# Criando uma instância do Instaloader
L = instaloader.Instaloader()

# perfil de quem voce quer baixar as fotos
profile_name = input("Digite o nome do perfil: ")

try:
    # Carregando o perfil
    profile = instaloader.Profile.from_username(L.context, profile_name)
except instaloader.exceptions.ProfileNotExistsException:
    print("O perfil não existe!")
    exit()


# Percorrendo as publicações do perfil
for post in profile.get_posts():
    # Baixando a publicação
    L.download_post(post, target=profile.username)


