from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from ..models.query import Query 
from datetime import datetime

class QueryRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
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
           sql = update(Attendance_Member).where(Attendance_Member.id == id).values(**details)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
           
       except: 
           return False 
       return True
   
    async def delete_attendance(self, id:int) -> bool: 
        try:
           sql = delete(Attendance_Member).where(Attendance_Member.id == id)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
        except: 
            return False 
        return True
    
    async def get_all_attendance(self):
        q = await self.sess.execute(select(Attendance_Member))
        return q.scalars().all()
    
    async def get_attendance(self, id:int): 
        q = await self.sess.execute(select(Attendance_Member).where(Attendance_Member.member_id == id))
        return q.scalars().all()

    async def check_attendance(self, id:int): 
        q = await self.sess.execute(select(Attendance_Member).where(Attendance_Member.id == id))
        return q.scalar()
