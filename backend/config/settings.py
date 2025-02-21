from urllib.parse import quote_plus

password = "Adi!1@T"
encoded_password = quote_plus(password)

DATABASE_URI = f"mysql+pymysql://root:{encoded_password}@localhost/syntax_squad"
SQLALCHEMY_TRACK_MODIFICATIONS = False
