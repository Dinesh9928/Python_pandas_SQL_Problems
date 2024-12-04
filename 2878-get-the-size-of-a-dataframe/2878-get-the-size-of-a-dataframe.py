

"""
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
    
    def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [*players.shape]
    
    def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [element for element in players.shape]
    
    def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(map(lambda x: x, players.shape))
    
"""
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List:
    return [players.shape[0], players.shape[1]]