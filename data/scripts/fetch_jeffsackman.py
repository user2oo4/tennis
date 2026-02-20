import pandas as pd
import os

def download_atp_matches(year):
    """Download specific year of ATP matches"""
    url = f"https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_{year}.csv"
    df = pd.read_csv(url)
    
    os.makedirs("data/raw/jeffsackman", exist_ok=True)
    df.to_csv(f"data/raw/jeffsackman/atp_matches_{year}.csv", index=False)
    return df

def download_wta_matches(year):
    """Download specific year of WTA matches"""
    url = f"https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_matches_{year}.csv"
    df = pd.read_csv(url)
    
    os.makedirs("data/raw/jeffsackman", exist_ok=True)
    df.to_csv(f"data/raw/jeffsackman/wta_matches_{year}.csv", index=False)
    return df

def download_atp_players():
    """Download ATP player data"""
    url = "https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_players.csv"
    df = pd.read_csv(url, low_memory=False)
    
    os.makedirs("data/raw/jeffsackman", exist_ok=True)
    df.to_csv("data/raw/jeffsackman/atp_players.csv", index=False)
    return df

def download_wta_players():
    """Download WTA player data"""
    url = "https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_players.csv"
    df = pd.read_csv(url, low_memory=False)
    
    os.makedirs("data/raw/jeffsackman", exist_ok=True)
    df.to_csv("data/raw/jeffsackman/wta_players.csv", index=False)
    return df


if __name__ == "__main__":
    for year in range(2024, 2025):
        print(f"Downloading {year}...")
        download_atp_matches(year)
        download_wta_matches(year)
    # download_atp_players()
    # download_wta_players()