from myapp import db

class City(db.Model):
    city_name = db.Column(db.String(64), index=True, primary_key=True)
    city_rank = db.Column(db.Integer, unique=False,index=True)
    is_visited = db.Column(db.Boolean)
    
    def __repr__(self): 
        return f'{self.city_name}'

    def __hash__(self):
        return hash(self.city_name)


