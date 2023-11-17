from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.query import Query 
from datetime import datetime

class QueryRepository: 
    
    def __init__(self, sess:AsyncSession):
        self.sess:AsyncSession = sess
    
    async def insert_query(self, query: Query) -> bool: 
        try:
            sql = insert(Query).values(id=query.id, publication_date=query.publication_date, title=query.title, content=query.content) 
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
            
            #self.sess.add(attendance)
            #await self.sess.flush()
        except: 
            return False 
        return True
    
    async def update_query(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           details["timeout"] = datetime.strptime(details["timeout"] , "%H:%M")
           details["timein"] = datetime.strptime(details["timein"] , "%H:%M")
           sql = update(Query).where(Query.id == id).values(**details)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
           
       except: 
           return False 
       return True
   
    async def delete_attendance(self, id:int) -> bool: 
        try:
           sql = delete(Query).where(Query.id == id)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
        except: 
            return False 
        return True
    
    async def get_all_queries(self):
        q = await self.sess.execute(select(Query))
        return q.scalars().all()
    
    async def get_query(self, id:int): 
        q = await self.sess.execute(select(Query).where(Query.id == id))
        return q.scalars().all()

