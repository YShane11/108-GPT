from dotenv import dotenv_values

config = dotenv_values("C:/Users/jason/.env.txt")
print(config["QQ"])