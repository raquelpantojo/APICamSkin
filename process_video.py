# process_video.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import numpy as np
import sys
import os

# Nesta pasta tem exatamente o estilo da figura 8 do artigo.
# Curva sem os fits/ pontos em vermelho escuro/ hemoglobin component
#sys.path.append('C:/Users/raque/OneDrive/Documentos/GitHub/APICamSkin/rpsbpyCRT')
#from src.rpsbpyCRT import PCRT

sys.path.append(os.path.join(os.path.dirname(__file__), 'rpsbpyCRT', 'src'))
from rpsbpyCRT import PCRT 


def process_video(video_path):
    # Process the video using pyCRT
    roi=(784, 515, 165, 162)
    #filePath = "580lux.mp4"
    #roi=(784, 515, 165, 162)
    #(3.7729388062921494, 0.8850660848326386)
    
    pcrt = PCRT.fromVideoFile(video_path,roi=roi,displayVideo=False,exclusionMethod='best fit',exclusionCriteria=9999999)
    
    #(1.9553732602812774, 0.15108928992342496)
  
    
    # Get the values you want from the pcrt object
    
    pycrtvalue = pcrt.pCRT[0].__round__(2) 
    pycrtincert = pcrt.pCRT[1].__round__(2)

    # Ensure the directory exist
    result_dir = "runs/detect"
    os.makedirs(result_dir, exist_ok=True)

    # Save the values to the txt file
    result_txt_path = "runs/detect/processed_result.txt"
    with open(result_txt_path, 'w') as file:
        file.write(f'pCRT: {pycrtvalue}, incerteza: {pycrtincert}')

    return pycrtvalue, pycrtincert