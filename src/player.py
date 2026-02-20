class Player:
    # Columns in raw player data
    # player_id,name_first,name_last,hand,dob,ioc,height,wikidata_id

    def __init__(self, player_id, name, hand, dob, ioc, height, wikidata_id):
        self.player_id = player_id
        self.name = name.first + " " + name.last
        self.hand = hand
        self.dob = dob
        self.ioc = ioc # country code
        self.height = height
        self.wikidata_id = wikidata_id
        # Realized stats
        self.last_updated = None # for decaying average stats
        # All stats are based on surfaces and also decayed so no need for form stats
        # Well form maybe just last 2 months regarless of surface as well
        self.stats = {
            "last_updated": {}, # for decaying average stats, this has to account for the surface as well, so maybe a dict of surface to last updated date
            "ovr_form": 0.0, # decaying average of last 2 months performance on all surfaces
            "win_percentage": {}, # on different surfaces decaying over the last 1 year (whole season)
            "break_point_conversion_rate": {}, 
            "break_points_saved_rate": {},
            "1st_serve_percentage": {},
            "1st_serve_win_percentage": {},
            "2nd_serve_win_percentage": {},
            "1st_serve_return_win_percentage": {},
            "2nd_serve_return_win_percentage": {},
            "overall_serve_win_percentage": {},
            "overall_return_win_percentage": {},
        }
    
    def __repr__(self):
        return f"Player({self.name}, {self.hand}, {self.dob}, {self.ioc}, {self.height})"
    
    def age_at(self, date):
        from datetime import datetime
        dob = datetime.strptime(self.dob, "%Y-%m-%d")
        date = datetime.strptime(date, "%Y%m%d")
        return (date - dob).days // 365
    
