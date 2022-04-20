#Untuk membuat lingkungan virtual, tentukan direktori tempat ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:
"""python3 -m venv tutorial-env"""

#Setelah Anda membuat lingkungan virtual, Anda dapat mengaktifkannya.
#Di Windows, operasikan:
"""tutorial-env\Scripts\activate.bat"""

#Pada Unix atau MacOS, operasikan
"""source tutorial-env/bin/activate"""

import sys
sys.path

#output
"""
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
"""