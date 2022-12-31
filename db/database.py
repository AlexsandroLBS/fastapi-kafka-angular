import psycopg2 
from api.schema import Notification
from api.config import db_config


class Database:

    def execAction(self, request):
        self.conn = psycopg2.connect(db_config)
        self.cur = self.conn.cursor()
        if request['action'] == "CREATE_ACCOUNT":
            self.cur.execute(f"SELECT * FROM public.users WHERE user_name='{request['full_name']}'")
            user_exists = self.cur.fetchall()
            if not user_exists:
            ##CRIA O USUÁRIO
                self.cur.execute(f"INSERT INTO public.users (user_name, created_at) VALUES ('{request['full_name']}', NOW())")
                self.cur.execute(f"SELECT id FROM public.users WHERE user_name='{request['full_name']}' ")
                self.conn.commit()
                id = self.cur.fetchall()
                ##GERA UMA SUBSCRICAO DO TIPO 0 - SEM INSCRICAO
                self.cur.execute(f"INSERT INTO public.subscription (user_id, status_id, created_at, updated_at) VALUES ({id[0][0]}, 0, NOW(), NOW())")##
            else:
                print('usuário já existe')
        else:
            try:
                self.cur.execute(f"SELECT * FROM public.users WHERE user_name = '{request['full_name']}'")   
                data = self.cur.fetchall()
            except:
                print("Falha ao encontrar usuário")
            if data:
                self.cur.execute(f"SELECT id FROM public.users WHERE user_name='{request['full_name']}' ")
                id = self.cur.fetchall()
                self.cur.execute(f"SELECT id FROM public.subscription WHERE user_id={id[0][0]} ")
                sub_id = self.cur.fetchall()
                self.cur.execute(f"SELECT status_id FROM public.subscription WHERE user_id={id[0][0]} ")
                status = self.cur.fetchall()

                if request['action'] == "SUBSCRIPTION_PURCHASED":
                    if status[0][0] == 0:
                        
                        self.cur.execute(f"""UPDATE public.subscription SET  status_id = 1, created_at=NOW(), updated_at=NOW()
                                         WHERE  user_id={id[0][0]}""")  
                        self.conn.commit()               
                    else:
                        self.cur.execute(f"""UPDATE public.subscription SET  status_id = 1, updated_at  = NOW()
                                         WHERE  user_id={id[0][0]}""")  
                    self.conn.commit()
                    self.cur.execute(f"INSERT INTO public.event_history (subscription_id, type, created_at) VALUES ({sub_id[0][0]}, 'SUBSCRIPTION_PURCHASED', NOW())")   
                    self.conn.commit()
                elif request['action'] == "SUBSCRIPTION_CANCELED":
                    if status[0][0] == 1 or status[0][0] == 3:
                        self.cur.execute(f"""UPDATE public.subscription SET  status_id = 2, updated_at=NOW()
                                         WHERE  user_id={id[0][0]}""")
                        self.conn.commit()
                        self.cur.execute(f"INSERT INTO public.event_history (subscription_id, type, created_at) VALUES ({sub_id[0][0]}, 'SUBSCRIPTION_CANCELED', NOW())")                                            
                        self.conn.commit()
                    else:
                        print('VOCE PRECISA TER UMA INSCRICAO PARA QUE ELA SEJA CANCELADA')

                elif request['action'] == "SUBSCRIPTION_RESTARTED":
                    if status[0][0] == 2:
                        self.cur.execute(f"""UPDATE public.subscription SET  status_id = 3, updated_at=NOW()
                                         WHERE  user_id={id[0][0]}""")
                        self.conn.commit()
                        self.cur.execute(f"INSERT INTO public.event_history (subscription_id, type, created_at) VALUES ({sub_id[0][0]}, 'SUBSCRIPTION_RESTARTED', NOW())")                                            
                        self.conn.commit()
                    else:
                        print('VOCE PRECISA TER UMA CANCELADO UMA INSCRICAO PARA QUE ELA SEJA REINICIADA')
                else:
                    print('acao nao identificada')

        self.conn.commit()
        self.cur.close()
        self.conn.close()


    def getUserByName(self, user: str):
        self.cur.execute(f"""
            SELECT user, status_id FROM users INNER JOIN subscription ON id = user_id 
            WHERE user ={user}
        """)
        response = self.cur.fetchall()

        return response