from pydantic import BaseSettings

#define enviroment vatiables
class Settings(BaseSettings):
   database_hostname: str
   database_port: str
   database_password: str
   database_name: str
   database_username: str
   secret_key: str
   algorithm: str
   access_token_expire_minutes: int

   class Config:
    env_file = ".env"

settings = Settings()

# old code db connection, should be addressed in database.py in case using it for db conn
# while True:
#     #master pass pgAdmin : fastapi
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastAPI', user='postgres', password='mRaimstmla!', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection succesfull!")
#         break
#     except Exception as error:
#         print("Connection failed")
#         print("Erorr: ", error)
#         time.sleep(2)