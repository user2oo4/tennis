# Read raw data, calculate stats, save processed data for modeling
import pandas as pd
import os

def load_atp_matches(year):
    """Load specific year of ATP matches from local storage"""
    file_path = f"data/raw/jeffsackman/atp_matches_{year}.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"{file_path} not found. Please run fetch_jeffsackman.py to download the data.")

def load_wta_matches(year):
    """Load specific year of WTA matches from local storage"""
    file_path = f"data/raw/jeffsackman/wta_matches_{year}.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"{file_path} not found. Please run fetch_jeffsackman.py to download the data.")

# Columns in the raw data
# tourney_id,tourney_name,surface,draw_size,tourney_level,tourney_date,
# match_num,winner_id,winner_seed,winner_entry,winner_name,winner_hand,
# winner_ht,winner_ioc,winner_age,loser_id,loser_seed,loser_entry,loser_name,
# loser_hand,loser_ht,loser_ioc,loser_age,score,best_of,round,minutes,w_ace,
# w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,
# l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced,winner_rank,
# winner_rank_points,loser_rank,loser_rank_points

# Columns in raw player data
# player_id,name_first,name_last,hand,dob,ioc,height,wikidata_id

# Inferred data for players:
# win_percentage on different surfaces

# Clutch stats
# break_point_conversion_rate on different surfaces
# break_points_saved_rate on different surfaces

# Basic stats
# 1st_serve_percentage on different surfaces
# 1st_serve_win_percentage on different surfaces
# 2nd_serve_win_percentage on different surfaces
# 1st_serve_return_win_percentage on different surfaces
# 2nd_serve_return_win_percentage on different surfaces
# overall_serve_win_percentage on different surfaces
# overall_return_win_percentage on different surfaces

# Form
# decaying average of last 2 months performance on different surfaces
# include opponent's rank and importance of tournament as weights as well

# In order to calculate these stats, iterate and grab these
# Total matches, wins, losses on different surfaces for each player
# Total break points faced, break points saved, break points converted for each player on different surfaces
# Total serving points (svpt) -> total serving points won, total first serves in, won, etc.
# Same but for return points when doing opponent's stats

